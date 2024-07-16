#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Created on 25.10.23
Module containing wrapped eval workflow into a function.

:author:     Martin Dočekal
"""

from oarelatedworkevaluator.datasets.oa_related_work import OARelatedWork, OARWConfig
from oarelatedworkevaluator.etl.dataset import Split
from oarelatedworkevaluator.utils.general_entities import FileFormat
from oarelatedworkevaluator.workflow import InputResult, EvalResult, EvalWorkflow


def eval_oa_related_work(evaluate: str, results: str, cache_dir: str = None,
                         file_format: FileFormat = FileFormat.CSV,
                         batch_size: int = 4,
                         verbose: bool = True):
    """
    Runs evaluation of results on oa_related_work dataset.
    It is expected that the evaluate file contains two fields:
        sample_id - is used to obtain the ground truth summary
        summary - generated summary in markdown like text format

    :param evaluate: Path to the file with generated summaries.
    :param results: Path to the file where the evaluation results will be stored.
    :param cache_dir: Path to the huggingface cache directory.
    :param file_format: File format of results that should be evaluated
    :param batch_size: Batch size for evaluators that supports batching.
    :param verbose: Whether to print progress of the evaluation.
    """
    dataset = OARelatedWork(
        path="BUT-FIT/OARelatedWork",
        cache_dir=cache_dir,
        config_name=OARWConfig.ABSTRACTS,
        split=Split.TEST,
        mask_formulas_in_references=None,
        mask_formulas="<eq>",
        use_title_in_query=False,
        use_abstract_in_query=False,
        use_rest_of_paper_in_query=False,
        add_unk_cit_to_input=False)

    workflow = EvalWorkflow(
        dataset=dataset,
        evaluate=evaluate,
        results=results,
        inp_type=InputResult,
        eval_type=EvalResult,
        file_format=file_format,
        batch_size=batch_size,
        verbose=verbose)

    workflow()


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Evaluation of oa_related_work dataset.")
    parser.add_argument("evaluate", help="Path to the file with generated summaries.")
    parser.add_argument("results", help="Path to the file where the evaluation results will be stored.")
    parser.add_argument("--cache_dir", help="Path to the huggingface cache directory.")
    parser.add_argument("--file_format", help="File format of results that should be evaluated.",
                        choices=[f.name for f in FileFormat], default=FileFormat.CSV.name)
    parser.add_argument("--batch_size", help="Batch size for evaluators that supports batching.", type=int, default=4)
    parser.add_argument("--verbose", help="Whether to print progress of the evaluation.", action="store_true")

    args = parser.parse_args()

    eval_oa_related_work(args.evaluate, args.results, args.cache_dir, FileFormat[args.file_format], args.batch_size,
                         args.verbose)


if __name__ == "__main__":
    main()
