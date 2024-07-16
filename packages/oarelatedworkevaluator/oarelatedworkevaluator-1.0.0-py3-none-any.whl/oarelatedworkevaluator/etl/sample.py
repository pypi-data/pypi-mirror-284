# -*- coding: UTF-8 -*-
""""
Created on 08.08.22
Contains class for a dataset sample.

:author:     Martin Dočekal
"""
from dataclasses import dataclass
from typing import Optional, Sequence, Union, List

from oarelatedworkevaluator.etl.data_structures.structured_document import StructuredDocument


@dataclass(slots=True)
class Sample:
    """
    Defines data sample for a task.
    """
    sample_id: int  #: Unique identifier of a sample


@dataclass(slots=True)
class MultiDocumentSummarizationSample(Sample):
    inputs: Sequence[str]  #: texts to be summarized
    summary: Optional[str]  #: target summary, optional only for prediction when the target is not available
    inputs_metadata: Sequence[Optional[dict]]  #: metadata for inputs


@dataclass(slots=True)
class MultiStructuredDocumentSummarizationSample(Sample):
    inputs: Sequence[StructuredDocument]  #: texts to be summarized
    summary: Optional[StructuredDocument]  #: target summary, optional only for prediction when the target is not available
    inputs_metadata: Sequence[Optional[dict]]  #: metadata for inputs


@dataclass(slots=True)
class SummarizationSample(MultiDocumentSummarizationSample):
    def __post_init__(self):
        if isinstance(self.inputs, str):
            self.inputs = [self.inputs]

    @property
    def input(self) -> str:
        """
        text to be summarized
        """
        return self.inputs[0]


@dataclass(slots=True)
class StructuredDocumentSummarizationSample(MultiStructuredDocumentSummarizationSample):
    def __post_init__(self):
        if isinstance(self.inputs, StructuredDocument):
            self.inputs = [self.inputs]

    @property
    def input(self) -> StructuredDocument:
        """
        text to be summarized
        """
        return self.inputs[0]


@dataclass(slots=True)
class QueryBasedMultiDocumentSummarizationSample(MultiDocumentSummarizationSample):
    query: Sequence[str]  #: query for summary specification


@dataclass(slots=True)
class QueryBasedMultiStructuredDocumentSummarizationSample(MultiStructuredDocumentSummarizationSample):
    query: Sequence[Union[str, StructuredDocument]]  #: query for summary specification


@dataclass(slots=True)
class PreparedFeaturesClassificationSample(Sample):
    features: Sequence[float]  #: features of a sample
    label: Union[int, str]  #: label of a sample


@dataclass(slots=True)
class GroupedMultiDocumentSummarizationSample(Sample):
    inputs: Sequence[Sequence[str]]  #: sequence of groups where each group is a sequence of texts to be summarized
    summary: Optional[str]  #: target summary, optional only for prediction when the target is not available
    inputs_metadata: Sequence[Optional[dict]]  #: metadata for inputs


@dataclass(slots=True)
class GroupedMultiStructuredDocumentSummarizationSample(Sample):
    inputs: Sequence[Sequence[StructuredDocument]]  #: sequence of groups where each group is a sequence of texts to be summarized
    summary: Optional[StructuredDocument]  #: target summary, optional only for prediction when the target is not available
    inputs_metadata: Sequence[Optional[dict]]  #: metadata for inputs
    auxiliary_embeddings: Optional[Sequence[Sequence[Optional[Sequence[float]]]]]  #: embeddings of inputs, that could be voluntary used as auxiliary features


@dataclass(slots=True)
class SequenceClassificationSample(Sample):
    sequence: Sequence[Union[int, str, List[str]]]
    label: Optional[Union[int, str]]  #: unknown during testing
