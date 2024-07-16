# -*- coding: UTF-8 -*-
"""
Created on 07.11.22
Module for result classes.

:author:     Martin Dočekal
"""
from dataclasses import dataclass, field, fields
from typing import Sequence, Optional, Union, List

import torch


@dataclass(slots=True)
class EmptyResult:
    """
    Empty result class.
    """

    @classmethod
    def from_dict(cls, d: dict) -> "EmptyResult":
        """
        Loads the data from dictionary.

        :param d: dictionary with data
        """
        kargs = {}
        for f in fields(cls):
            if f.name not in d:
                raise ValueError(f"Missing key {f.name} in dictionary.")

            kargs[f.name] = d[f.name]

        return cls(**kargs)


@dataclass(slots=True)
class Result(EmptyResult):
    """
    Base class for a task result.
    """
    sample_id: int  #: Unique identifier of a sample

@dataclass(slots=True)
class MultiDocumentSummarizationResult(Result):
    gt_summary: Optional[str] = field(metadata={"unk_test_time": True, "input": True,
                                                "eval": "reference"})  #: target summary, optional only for prediction  when the target is not available
    summary: str = field(metadata={"input": False, "eval": "prediction"})  #: generated summary
    inputs: Sequence[str] = field(metadata={"input": True})  #: texts to be summarized


@dataclass(slots=True)
class QueryBasedMultiDocumentSummarizationResult(MultiDocumentSummarizationResult):
    query: str = field(metadata={"input": True})  #: query for summary specification


@dataclass(slots=True)
class ClassificationResult(Result):
    gt_label: Union[int, str] = field(
        metadata={"unk_test_time": True, "input": True, "eval": "reference"})  #: label of a sample
    label: Union[int, str] = field(metadata={"input": False, "eval": "prediction"})  #: predicted label of a sample
    probabilities: Union[float, Sequence[float]] = field(metadata={"input": False})  #: probabilities of all classes


@dataclass(slots=True)
class PreparedFeaturesClassificationResult(ClassificationResult):
    features: Sequence[float] = field(metadata={"input": True})


@dataclass(slots=True)
class MultiStructuredDocumentSummarizationResult(Result):
    gt_sequence: Optional[str] = field(metadata={"unk_test_time": True, "input": True,
                                                "eval": "reference"})  #: target summary, optional only for prediction  when the target is not available
    sequence: str = field(metadata={"input": False, "eval": "prediction"})  #: generated summary
    input_doc_ids: Sequence[int] = field(metadata={"input": True})  #: just document ids


@dataclass(slots=True)
class QueryBasedMultiStructuredDocumentSummarizationResult(MultiStructuredDocumentSummarizationResult):
    query: str = field(metadata={"input": True})  #: query for summary specification


@dataclass(slots=True)
class MultiStructuredDocumentSummarizationTargetOnlyResult(Result):
    gt_sequence: Optional[str] = field(metadata={"unk_test_time": True, "input": True,
                                                 "eval": "reference"})  #: target summary, optional only for prediction  when the target is not available
    sequence: str = field(metadata={"input": False, "eval": "prediction"})  #: generated summary


@dataclass(slots=True)
class GroupedMultiStructuredDocumentSummarizationResult(Result):
    gt_sequence: Optional[str] = field(metadata={"unk_test_time": True, "input": True,
                                                "eval": "reference"})  #: target summary, optional only for prediction  when the target is not available
    sequence: str = field(metadata={"input": False, "eval": "prediction"})  #: generated summary
    input_doc_ids: Sequence[Sequence[int]] = field(metadata={"input": True})  #: ids of input documents for each group


@dataclass(slots=True)
class ExtSummarizationResult(Result):
    gt_summary: Optional[str] = field(metadata={"unk_test_time": True, "input": True,
                                                "eval": "reference"})  #: target summary, optional only for prediction  when the target is not available
    summary: str = field(metadata={"input": False, "eval": "prediction"})  #: generated summary
    gt_classification: Optional[List[int]] = field(metadata={"unk_test_time": True, "input": True})  #: target classification, optional only for prediction  when the target is not available
    classification: List[int] = field(metadata={"input": False})


@dataclass(slots=True)
class SequenceGenerationResult(Result):
    gt_sequence: Optional[str] = field(metadata={"unk_test_time": True, "input": True,
                                                "eval": "reference"})  #: target sequence, optional only for prediction  when the target is not available
    sequence: str = field(metadata={"input": False, "eval": "prediction"})  #: generated sequence
