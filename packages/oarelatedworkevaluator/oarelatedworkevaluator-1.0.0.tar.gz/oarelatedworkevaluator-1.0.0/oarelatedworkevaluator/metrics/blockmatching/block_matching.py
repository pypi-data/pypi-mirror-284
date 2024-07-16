# -*- coding: UTF-8 -*-
"""
Created on 15.09.23

:author:     Martin Dočekal
"""
from functools import lru_cache
from typing import Sequence, Dict, List, Tuple

import datasets
import evaluate
import munkres
import numpy as np
from tqdm import tqdm

_DESCRIPTION = """
Meta metric for calculating similarity of blocks.

It is comparing best matching blocks using given metric.

It is called meta metric because it is using other metrics operating on plain string level, 
but upgrades it to block level.
"""

_KWARGS_DESCRIPTION = """
Produces similarity of multiple text blocks.

Args:
    predictions: Predicted blocks. 
    references: References in form of blocks. 
    Returns:
        block similarity
Examples:
    >>> metric = BlockMatchingMetric(evaluate.load('rouge'), "rouge2")
    >>> metric.compute(references=[
            ["text of block 0", "text of block 1", "text of block 2"]
        ], predictions=[
            ["text of block 0", "text of block 1"]
        ])
    {'recall': 0.6666666666666666, 'precision': 1.0, 'f1': 0.8}

"""


class BlockMatchingMetric(evaluate.Metric):
    """
    Meta metric for calculating similarity of blocks.

    It is comparing best matching blocks using given metric.

    It is called meta metric because it is using other metrics operating on plain string level,
    but upgrades it to block level.
    """

    def __init__(self, metric: evaluate.Metric, sel_key: str, row_col_norm: bool = False, verbose: bool = True, **kwargs):
        """
        Initializes metric.

        :param metric: metric that should be used for string similarity
        :param sel_key: Key that will be used to select value from dictionary returned by metric.
        :param row_col_norm: If True then the final similarity will be normalized by sum of similarities in its row in
            case of recall and by sum of similarities in its column in case of precision.
        :param verbose: If True then progress bar is shown.
        """
        super().__init__(**kwargs)
        self.metric = metric
        self.sel_key = sel_key
        self.row_col_norm = row_col_norm
        self.verbose = verbose

    def _info(self):
        return evaluate.MetricInfo(
            description=_DESCRIPTION,
            inputs_description=_KWARGS_DESCRIPTION,
            citation="",
            features=datasets.Features({
                "predictions": datasets.Sequence(datasets.Value("string")),
                "references": datasets.Sequence(datasets.Value("string"))
            }),
        )

    @lru_cache(maxsize=1000)
    def cached_text_similarity(self, text1: str, text2: str) -> float:
        """
        Computes similarity of two texts.

        :param text1: First text.
            act as a reference.
        :param text2: Second text.
            act as a prediction.
        :return: Similarity of two texts.
        """
        return self.metric.compute(
            references=[text1],
            predictions=[text2]
        )[self.sel_key]

    def calc_similarities(self, x_blocks: Sequence[str], y_blocks: Sequence[str]) -> List[List[float]]:
        """
        Computes similarity matrix of two sets of blocks.

        :param x_blocks: First set of blocks.
            act as a reference.
        :param y_blocks: Second set of blocks.
            act as a prediction.
        :return: Similarity matrix.
        """
        references = [x for x in x_blocks for _ in y_blocks]
        predictions = [y for _ in x_blocks for y in y_blocks]

        all_similarities = self.metric.compute(
            references=references,
            predictions=predictions
        )[self.sel_key]

        return [
            [all_similarities[i * len(y_blocks) + j] for j in range(len(y_blocks))]
            for i in range(len(x_blocks))
        ]

    def match_blocks(self, ref_blocks: Sequence[str], pred_blocks: Sequence[str]) -> Tuple[float, float, float]:
        """
        Computes similarity of blocks.

        :param ref_blocks: Reference blocks.
        :param pred_blocks: Predicted blocks.
        :return: Tuple of recall, precision and f1 score.
        """

        similarities = self.calc_similarities(ref_blocks, pred_blocks)  # len(ref_blocks) x len(pred_blocks) matrix

        # will use Hungarian algorithm to find best matching blocks
        cost_matrix = munkres.make_cost_matrix(similarities)

        m = munkres.Munkres()
        indexes = m.compute(cost_matrix)

        if self.row_col_norm:
            np_sim = np.array(similarities)
            abs_val_sim = np.abs(np_sim)
            row_sum = abs_val_sim.sum(axis=1, keepdims=True) + 1e-10
            col_sum = abs_val_sim.sum(axis=0, keepdims=True) + 1e-10
            row_norm = np_sim / row_sum
            col_norm = np_sim / col_sum

            recall = 0
            precision = 0

            for i, j in indexes:
                recall += row_norm[i][j]
                precision += col_norm[i][j]

            recall /= len(ref_blocks)
            precision /= len(pred_blocks)
        else:
            score = sum(similarities[i][j] for i, j in indexes)

            recall = score / len(ref_blocks)
            precision = score / len(pred_blocks)

        f1 = 0 if precision + recall == 0 else 2 * (precision * recall) / (precision + recall)
        return recall, precision, f1

    def _compute(self, references: Sequence[Sequence[str]], predictions: Sequence[Sequence[str]]) -> Dict[str, float]:
        """
        Computes blocks similarity.

        :param references: Reference blocks.
        :param predictions: Predicted blocks.
        :return: block similarity.
        """

        # get average recall, precision and f1 score

        recall = []
        precision = []
        f1 = []

        for ref, pred in tqdm(zip(references, predictions), disable=not self.verbose, total=len(references),
                              desc="Computing BlockMatchingMetric"):
            r, p, f = self.match_blocks(ref, pred)
            recall.append(r)
            precision.append(p)
            f1.append(f)

        return {
            "recall": sum(recall) / len(recall),
            "precision": sum(precision) / len(precision),
            "f1": sum(f1) / len(f1)
        }

