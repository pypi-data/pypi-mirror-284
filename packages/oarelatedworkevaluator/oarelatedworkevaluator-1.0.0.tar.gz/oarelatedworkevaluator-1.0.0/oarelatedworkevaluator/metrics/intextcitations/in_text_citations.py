# -*- coding: UTF-8 -*-
"""
Created on 16.10.23

Evaluation metric for in-text citations.

:author:     Martin Dočekal
"""
from collections import Counter
from typing import Sequence, Dict, Tuple, Generator

import datasets
import evaluate
import re

from tqdm import tqdm

_DESCRIPTION = """
Metric for in-text citations.

It is searching citations spans in reference and prediction. Every citation span is expected to have given format
by default it is:
     <cite>ID<sep>TITLE<sep>OTHER...</cite>
where <cite> and </cite> are citation tags, <sep> is separator and ID and TITLE are citation id and title. Instead of
ID there could be UNK. In that case the title is used for matching.

Two types of evaluation are performed. First one focuses on whether a work was cited at all, no matter how many times. 
Second one (in results it is marked with prefix span_*) is more strict as it is working on 
a span level, and when a work has multiple citation spans in reference, then it is checked whether same amount of the 
same citation spans is in prediction.

For each type of evaluation there are computed recall, precision and f1 score.

recall = intersection set of cited works in reference and prediction / set of cited works in reference
precision = intersection set of cited works in reference and prediction / set of cited works in prediction
f1 = 2 * recall * precision / (recall + precision)

span_recall = intersection multiset of cited works in reference and prediction / multiset of cited works in reference
span_precision = intersection multiset of cited works in reference and prediction / multiset of cited works in prediction
span_f1 = 2 * span_recall * span_precision / (span_recall + span_precision)

Reported values are sample average of recall, precision and f1 scores.
"""

_KWARGS_DESCRIPTION = """
Args:
    predictions: Predicted 
    references: References
    Returns:
        recall, precision and f1 score
        span_recall, span_precision and span_f1 score
Examples:
    >>> metric = InTextCitationsMetric()
    >>> metric.compute(references=[
            ["I am citing <cite>123<sep>Title of 123</cite> and <cite>456<sep>Title of 456</cite>, the <cite>123<sep>Title of 123</cite> is cited twice"]
        ], predictions=[
            ["I am also citing <cite>123<sep>Title of 123</cite>, but I not the other one"]
        ])
    {'recall': 0.5, 'precision': 1.0, 'f1': 0.666666, 'span_recall': 0.3333333, 'span_precision': 1.0, 'span_f1': 0.5}

"""


class InTextCitationsMetric(evaluate.Metric):
    """
    Metric for in-text citations.

    It is searching citations spans in reference and prediction. Every citation span is expected to have given format
    by default it is:
         <cite>ID<sep>TITLE<sep>OTHER...</cite>
    where <cite> and </cite> are citation tags, <sep> is separator and ID and TITLE are citation id and title. Instead of
    ID there could be UNK. In that case the title is used for matching.

    Two types of evaluation are performed. First one checks whether given work from reference was cited in prediction,
    no matter how many times. Second one (in results it is marked with prefix span_*) is more strict as it is working on
    a span level, and when a work has multiple citation spans in reference, then it is checked whether same amount of the
    same citation spans is in prediction.
    """

    def __init__(self, span_regex: str = r"<cite>(.+?)<\/cite>", sep: str = "<sep>", verbose: bool = True, **kwargs):
        """
        :param span_regex: Regex that is used to find citation spans in reference and prediction.
        :param sep: Separator that is used to split citation span into id and title.
        :param verbose: If True then progress bar is shown.
        """
        super().__init__(**kwargs)
        self.span_regex = span_regex
        self.sep = sep
        self.verbose = verbose

    def _info(self):
        return evaluate.MetricInfo(
            description=_DESCRIPTION,
            inputs_description=_KWARGS_DESCRIPTION,
            citation="",
            features=datasets.Features({
                "predictions": datasets.Value("string"),
                "references": datasets.Value("string")
            }),
        )

    def extract_citation_spans(self, text: str) -> Generator[Tuple[str, str], None, None]:
        """
        Extracts citation spans from given text.

        :param text: Text that contains citation spans.
        :return: generator of tuples (id, title).
        """
        for m in re.finditer(self.span_regex, text):
            parts = m.group(1).split(self.sep)
            if len(parts) <= 1:
                continue

            yield parts[0], parts[1]

    def _compute(self, references: Sequence[str], predictions: Sequence[str]) -> Dict[str, float]:
        """
        Computes blocks similarity.

        :param references: References
        :param predictions: Predictions
        :return: sample average of recall, precision and f1 score
        """

        res = {
            "recall": 0.0,
            "precision": 0.0,
            "f1": 0.0,
            "span_recall": 0.0,
            "span_precision": 0.0,
            "span_f1": 0.0
        }

        for ref, pred in tqdm(zip(references, predictions), disable=not self.verbose, total=len(references),
                              desc="Computing InTextCitationsMetric"):
            ref_spans = list((s[0].upper(), s[1].upper()) if s[0].upper() == "UNK" else s[0] for s in self.extract_citation_spans(ref))
            pred_spans = list((s[0].upper(), s[1].upper()) if s[0].upper() == "UNK" else s[0] for s in self.extract_citation_spans(pred))

            at_least_one_ref_spans = set(ref_spans)
            at_least_one_pred_spans = set(pred_spans)

            multiset_ref_spans = Counter(ref_spans)
            multiset_pred_spans = Counter(pred_spans)

            intersection_len = len(at_least_one_ref_spans & at_least_one_pred_spans)
            multiset_intersection_len = sum((multiset_ref_spans & multiset_pred_spans).values())

            recall = 0.0
            precision = 0.0
            span_recall = 0.0
            span_precision = 0.0

            if len(ref_spans) == 0 or len(pred_spans) == 0:
                if len(pred_spans) == 0 and len(ref_spans) == 0:
                    # no spans in reference and prediction is ok
                    recall = 1.0
                    span_recall = 1.0
                    precision = 1.0
                    span_precision = 1.0

                # else all values are zero
            else:
                recall += intersection_len / len(at_least_one_ref_spans)
                span_recall += multiset_intersection_len / sum(multiset_ref_spans.values())

                precision += intersection_len / len(at_least_one_pred_spans)
                span_precision += multiset_intersection_len / sum(multiset_pred_spans.values())

            res["recall"] += recall
            res["precision"] += precision
            res["f1"] += 2 * recall * precision / (recall + precision) if recall + precision > 0 else 0.0

            res["span_recall"] += span_recall
            res["span_precision"] += span_precision
            res["span_f1"] += 2 * span_recall * span_precision / (span_recall + span_precision) if span_recall + span_precision > 0 else 0.0

        for k in res:
            res[k] /= len(references)

        return res


