# -*- coding: UTF-8 -*-
""""
Created on 08.08.22
Module for reading a working with datasets.

:author:     Martin Dočekal
"""
from abc import abstractmethod
from enum import Enum
from typing import Sequence

from torch.utils.data import Dataset as TorchDataset

from oarelatedworkevaluator.etl.sample import MultiDocumentSummarizationSample, Sample, SummarizationSample, \
    QueryBasedMultiDocumentSummarizationSample, PreparedFeaturesClassificationSample, \
    MultiStructuredDocumentSummarizationSample, StructuredDocumentSummarizationSample, \
    QueryBasedMultiStructuredDocumentSummarizationSample, GroupedMultiDocumentSummarizationSample, \
    GroupedMultiStructuredDocumentSummarizationSample, SequenceClassificationSample


class Split(Enum):
    """
    Enum that allows to identify supported splits of a dataset.
    """
    TRAIN = "train"
    VALIDATION = "validation"
    TEST = "test"


class ToyValSplit(Enum):
    """
    Enum that allows to identify supported splits of a dataset.
    Is contains additional split for toy validation.
    """
    TRAIN = "train"
    VALIDATION = "validation"
    TEST = "test"
    VALIDATION_TOY = "validation_toy"


class NoTestSplit(Enum):
    """
    Enum that allows to identify supported splits of a dataset that doesn't have test set.
    """
    TRAIN = "train"
    VALIDATION = "validation"


class Dataset(Sequence[Sample], TorchDataset):
    """
    Provider of data for machine learning models and their evaluation.
    Is used as additional level of abstraction that provides task oriented samples created from raw data.
    """

    @abstractmethod
    def __len__(self) -> int:
        ...

    @abstractmethod
    def __getitem__(self, item: int) -> Sample:
        ...

class MultiDocumentSummarizationDataset(Dataset):
    """
    Dataset for multi document general summarization.
    """

    @abstractmethod
    def __getitem__(self, item: int) -> MultiDocumentSummarizationSample:
        ...


class MultiStructuredDocumentSummarizationDataset(Dataset):
    """
    Dataset for multi document general summarization from structured documents.
    """

    @abstractmethod
    def __getitem__(self, item: int) -> MultiStructuredDocumentSummarizationSample:
        ...


class SummarizationDataset(MultiDocumentSummarizationDataset):
    """
    Dataset for single document general summarization. The basic variant of summarization.
    """

    @abstractmethod
    def __getitem__(self, item: int) -> SummarizationSample:
        ...


class StructuredDocumentSummarizationDataset(MultiStructuredDocumentSummarizationDataset):
    """
    Dataset for single document general summarization from structured documents. The basic variant of summarization.
    """

    @abstractmethod
    def __getitem__(self, item: int) -> StructuredDocumentSummarizationSample:
        ...


class QueryBasedMultiDocumentSummarizationDataset(MultiDocumentSummarizationDataset):
    """
    Dataset for query based multi document summarization.
    """

    @abstractmethod
    def __getitem__(self, item: int) -> QueryBasedMultiDocumentSummarizationSample:
        ...


class QueryBasedMultiStructuredDocumentSummarizationDataset(MultiStructuredDocumentSummarizationDataset):
    """
    Dataset for query based multi structured document summarization.
    """

    @abstractmethod
    def __getitem__(self, item: int) -> QueryBasedMultiStructuredDocumentSummarizationSample:
        ...


class PreparedFeaturesClassificationDataset(Dataset):
    """
    Dataset for classification that is based on prepared features.
    """

    @abstractmethod
    def __getitem__(self, item: int) -> PreparedFeaturesClassificationSample:
        ...


class GroupedMultiDocumentSummarizationDataset(Dataset):
    """
    Dataset for multi document summarization, where the inputs are grouped.
    """

    @abstractmethod
    def __getitem__(self, item: int) -> GroupedMultiDocumentSummarizationSample:
        ...


class GroupedMultiStructuredDocumentSummarizationDataset(Dataset):
    """
    Dataset for multi structured document summarization, where the inputs are grouped.
    """

    @abstractmethod
    def __getitem__(self, item: int) -> GroupedMultiStructuredDocumentSummarizationSample:
        ...


class SequenceClassificationDataset(Dataset):
    """
    Dataset for sequence classification.
    """

    @abstractmethod
    def __getitem__(self, item: int) -> SequenceClassificationSample:
        ...

