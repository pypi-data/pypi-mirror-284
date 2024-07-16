# -*- coding: UTF-8 -*-
"""
Created on 21.11.22

:author:     Martin Dočekal
"""
import copy
import re
from typing import Tuple

from oarelatedworkevaluator.evaluation.evaluator import Evaluator
from oarelatedworkevaluator.results.result import EmptyResult

CITE_REGEX = re.compile("<cite>.+<\/cite>")
REF_REGEX = re.compile("<ref>.+<\/ref>")


def convert_to_blocks(result: EmptyResult) -> EmptyResult:
    """
    It will simply split the text by new line. Every line will be stripped and empty lines will be removed.

    :param result: Result to be converted.
    :return: New result with converted fields.
    """
    new_res = copy.copy(result)
    pred_f_name, gt_f_name = Evaluator.get_eval_fields(result.__class__)
    gt = getattr(new_res, gt_f_name).split("\n")
    pred = getattr(new_res, pred_f_name).split("\n")

    # strip and remove empty lines
    gt = [x.strip() for x in gt if x.strip()]
    pred = [x.strip() for x in pred if x.strip()]

    setattr(new_res, gt_f_name, gt)
    setattr(new_res, pred_f_name, pred)

    return new_res


def convert_citations_and_reference_spans_for_evaluation(result: EmptyResult) -> EmptyResult:
    """
    Converts citations and reference spans to unified format.

    :param result: Result to be converted.
    :return: New result with converted fields.
    """
    new_res = copy.copy(result)
    pred_f_name, gt_f_name = Evaluator.get_eval_fields(result.__class__)

    gt, pred = convert_citations_and_reference_spans_for_evaluation_raw(
        getattr(new_res, gt_f_name),
        getattr(new_res, pred_f_name))

    setattr(new_res, gt_f_name, gt)
    setattr(new_res, pred_f_name, pred)

    return new_res


def convert_citations_and_reference_spans_for_evaluation_raw(gt_summary: str, summary: str) -> Tuple[str, str]:
    """
    Converts citations and reference spans to unified format.

    :param gt_summary: Ground truth summary.
    :param summary: Generated summary.
    :return: Tuple of converted summaries. (gt_summary, summary)
    """

    return convert_citations_and_reference_spans_for_evaluation_in_string(gt_summary), \
             convert_citations_and_reference_spans_for_evaluation_in_string(summary)


def convert_citations_and_reference_spans_for_evaluation_in_string(s: str) -> str:
    """
    Converts citations and reference spans to unified format.

    :param s: String to be converted.
    :return: Converted string.
    """
    try:
        return REF_REGEX.sub("<ref>", CITE_REGEX.sub("<cite>", s))
    except Exception as e:
        print(s)
        raise e
