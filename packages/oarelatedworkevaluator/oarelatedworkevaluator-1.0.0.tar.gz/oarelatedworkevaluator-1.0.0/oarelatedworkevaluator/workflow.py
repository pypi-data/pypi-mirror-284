# -*- coding: UTF-8 -*-
"""
Created on 09.11.22

:author:     Martin Dočekal
"""
import dataclasses
import json
from contextlib import nullcontext
from dataclasses import field
from typing import Type

from oarelatedworkevaluator.datasets.oa_related_work import OARelatedWork
from oarelatedworkevaluator.evaluation.evaluator import Evaluator
from oarelatedworkevaluator.evaluation.utils import convert_citations_and_reference_spans_for_evaluation, \
    convert_to_blocks
from oarelatedworkevaluator.metrics.bertscorehfwrapper.bert_score import BertScore
from oarelatedworkevaluator.metrics.blockmatching.block_matching import BlockMatchingMetric
from oarelatedworkevaluator.metrics.huggingfacerouge.rouge import Rouge
from oarelatedworkevaluator.metrics.intextcitations.in_text_citations import InTextCitationsMetric
from oarelatedworkevaluator.results.result import Result
from oarelatedworkevaluator.results.results_reader import ResultsReader
from oarelatedworkevaluator.utils.general_entities import FileFormat


@dataclasses.dataclass()
class InputResult(Result):
    summary: str = field(metadata={"eval": "prediction", "aliases": {"sequence"}})  #: generated summary


@dataclasses.dataclass()
class EvalResult(InputResult):
    gt_summary: str = field(metadata={"eval": "reference"})  #: target summary


class EvalWorkflow:
    def __init__(self, dataset: OARelatedWork, evaluate: str, results: str, inp_type: Type[Result],
                 eval_type: Type[Result],
                 file_format: FileFormat, verbose: bool, block_metrics: bool = True, batch_size: int = 4):
        self.dataset = dataset
        self.results = results
        self.inp_type = inp_type
        self.eval_type = eval_type
        self.file_format = file_format

        bert_score = BertScore(rescale_with_baseline=True, aggregate=True, batch_size=batch_size)
        bert_score_for_block = BertScore(rescale_with_baseline=True, aggregate=False, batch_size=batch_size,
                                         model=bert_score.model)
        metrics = {
            
            "citations": InTextCitationsMetric(),
            "rouge": Rouge(verbose=verbose),
            "bert_score": bert_score
            
        }
        transforms = {
            "rouge": convert_citations_and_reference_spans_for_evaluation,
            "bert_score": convert_citations_and_reference_spans_for_evaluation,
        }
        if block_metrics:
            metrics["block_bert_score"] = BlockMatchingMetric(bert_score_for_block, sel_key="score")
            transforms["block_bert_score"] = lambda x: convert_to_blocks(convert_citations_and_reference_spans_for_evaluation(x))

        self.evaluator = Evaluator(metrics, self.eval_type)
        self.evaluator.transform = transforms

        self.results_samples = []
        with self.dataset if hasattr(self.dataset, "__enter__") else nullcontext():
            # get id to index mapping
            id_2_idx = {s.sample_id: i for i, s in enumerate(self.dataset)}

            # transform input results to eval results
            for r in ResultsReader(evaluate, self.inp_type, self.file_format, verbose=verbose):
                self.results_samples.append(self.eval_type(sample_id=r.sample_id,
                                                           gt_summary=self.dataset[id_2_idx[r.sample_id]].summary,
                                                           summary=r.summary))

            if set(id_2_idx.keys()) != set([r.sample_id for r in self.results_samples]):
                raise ValueError("The set of sample ids in the results file and in the dataset are not the same.")

    def __call__(self):
        with open(self.results, "w") as out:
            print(
                json.dumps(
                    self.evaluator.compute(
                        self.results_samples,
                        rouge={
                            "use_stemmer": True,
                            "split_summaries": True
                        }
                    )
                ),
                file=out
            )

