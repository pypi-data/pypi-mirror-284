# -*- coding: UTF-8 -*-
"""
Created on 07.11.22

:author:     Martin Dočekal
"""
from dataclasses import fields
from typing import Sequence, Optional, Dict, Any, TypeVar, Type, Callable, Tuple, Union, Iterable, Generic, AbstractSet

import evaluate

from oarelatedworkevaluator.results.result import EmptyResult

R = TypeVar("R", bound=EmptyResult)


class Evaluator(Generic[R]):
    """
    Class for evaluation of results.
    It is using metadata field "eval" of result dataclass to identify prediction and references.
    Set "eval": "reference" or "eval": "prediction" to mark reference field or prediction field respectively.
        You can also specify multiple reference and prediction fields. In that case use eval value with string prefix
        "reference" or "prediction".
    """

    def __init__(self, metric: Union[evaluate.Metric, Iterable[evaluate.Metric], Dict[str, evaluate.Metric]], result_type: Type[R],
                 transform: Optional[Union[Callable[[R], R], Dict[str, Callable[[R], R]]]] = None,
                 reference_field: Union[str, Dict[str, str]] = None, prediction_field: Union[str, Dict[str, str]] = None,
                 batch_transform: Optional[Union[Callable[[Sequence, Sequence], Tuple[Sequence, Sequence]], Dict[str, Callable[[Sequence, Sequence], Tuple[Sequence, Sequence]]]]] = None):
        """
        Initializes evaluator of given result type with provided metric.

        :param metric: metric that should be used for evaluation
            if it is iterable then each metric is reported separately
                if multiple metrics haves same key in their results then next one overrides the previous one
            when dict is provided then you can specify arguments for each metric in compute method by key
                also the results are formatted as dict
        :param result_type: type of results
        :param transform: performs transformation of results for evaluation
            you can specify transformation for each metric by using dict
        :param reference_field:
            name of the reference field
            by default it is None which means that it will be automatically determined from metadata
            you can specify name of the reference field for each metric by using dict
        :param prediction_field:
            name of the prediction field
            by default it is None which means that it will be automatically determined from metadata
            you can specify name of the prediction field for each metric by using dict
        :param batch_transform: transformation that is called on input to add_batch method of metric
            you can specify transformation for each metric by using dict
            First argument of the transformation is predictions and second is references.
        """
        if not isinstance(metric, dict):
            if isinstance(transform, dict):
                raise RuntimeError("If transform is dict then metric must be dict too.")

            if isinstance(reference_field, dict):
                raise RuntimeError("If reference_field is dict then metric must be dict too.")

            if isinstance(prediction_field, dict):
                raise RuntimeError("If prediction_field is dict then metric must be dict too.")

        self.metric = metric
        self._transform = transform

        if reference_field is None or prediction_field is None:
            auto_prediction_fields, auto_reference_fields = self.get_eval_fields(result_type)

        if isinstance(reference_field, str):
            self.reference_fields = [reference_field]
        elif isinstance(reference_field, dict):
            self.reference_fields = list(reference_field.values())
        else:
            self.reference_fields = [auto_reference_fields]

        if isinstance(prediction_field, str):
            self.prediction_fields = [prediction_field]
        elif isinstance(prediction_field, dict):
            self.prediction_fields = list(prediction_field.values())
        else:
            self.prediction_fields = [auto_prediction_fields]

        self.reference_field_for_metric = auto_reference_fields if reference_field is None else reference_field
        self.prediction_field_for_metric = auto_prediction_fields if prediction_field is None else prediction_field

        if isinstance(self.metric, dict):
            # assign auto fields, if necessary, for each metric
            if isinstance(self.reference_field_for_metric, str):
                self.reference_field_for_metric = {k: self.reference_field_for_metric for k in self.metric}

            if isinstance(self.prediction_field_for_metric, str):
                self.prediction_field_for_metric = {k: self.prediction_field_for_metric for k in self.metric}

        self.batch_transform = batch_transform

    @property
    def transform(self) -> Optional[Union[Callable[[R], R], Dict[str, Callable[[R], R]]]]:
        """
        Which transformation is used for results for evaluation.
        """
        return self._transform

    @transform.setter
    def transform(self, value: Optional[Union[Callable[[R], R], Dict[str, Callable[[R], R]]]]):
        """
        Sets transformation of results for evaluation.
        """
        self._transform = value

        if isinstance(self._transform, dict) and not isinstance(self.metric, dict):
            raise RuntimeError("If transform is dict then metric must be dict too.")

    @staticmethod
    def get_eval_fields(result_type: Type[EmptyResult]) -> Tuple[str, str]:
        """
        Returns prediction and reference field names for given result type.

        :param result_type: result type
        :return: prediction and reference field names
        :raises RuntimeError: if there is missing prediction or reference field
        """
        prediction_field = None
        reference_field = None

        for f in fields(result_type):
            if "eval" in f.metadata:
                if f.metadata["eval"] == "reference":
                    if reference_field is not None:
                        raise RuntimeError(
                            f"There are multiple reference fields for result type {result_type.__name__}."
                        )
                    reference_field = f.name
                elif f.metadata["eval"] == "prediction":
                    if prediction_field is not None:
                        raise RuntimeError(
                            f"There are multiple prediction fields for result type {result_type.__name__}."
                        )
                    prediction_field = f.name

        if prediction_field is None:
            raise RuntimeError(f"There is missing prediction field for result type {result_type.__name__}.")

        if reference_field is None:
            raise RuntimeError(f"There is missing reference field for result type {result_type.__name__}.")

        return prediction_field, reference_field

    def add_batch_to_metric(self, metric: evaluate.Metric, metric_name: str, predictions: Sequence, references: Sequence):
        """
        Adds batch to metric. Applies batch_transform if specified.

        :param metric: metric to which batch should be added
        :param metric_name: name of the metric, that is used to determine batch_transform when it is dict
        :param predictions: predictions
        :param references: references
        """

        if self.batch_transform is not None:
            if isinstance(self.batch_transform, dict):
                if metric_name in self.batch_transform:
                    predictions, references = self.batch_transform[metric_name](predictions, references)
            else:
                predictions, references = self.batch_transform(predictions, references)

        metric.add_batch(predictions=predictions, references=references)

    def __call__(self, results: Sequence[R]):
        """
        Adds result for evaluation

        :param results: results that should be evaluated
        """
        # metric.add was problematic for some metric (ROUGE) thus we use the add_batch which works
        # I've posted this problem to the forum: https://huggingface.co/spaces/evaluate-metric/rouge/discussions/3

        if self._transform is not None and isinstance(self._transform, dict):
            # transform is dict thus metric is dict too
            predictions = {k: [] for k in self.prediction_fields}    # used only when there is a metric without transformation
            references = {k: [] for k in self.reference_fields}     # used only when there is a metric without transformation

            predictions_transformed = {k: {f: [] for f in self.prediction_fields} for k in self._transform}
            references_transformed = {k: {f: [] for f in self.reference_fields} for k in self._transform}

            metric_without_transform = len(set(self.metric.keys()) - set(self._transform.keys())) > 0

            for r in results:
                if metric_without_transform:
                    for k in self.prediction_fields:
                        predictions[k].append(getattr(r, k))
                    for k in self.reference_fields:
                        references[k].append(getattr(r, k))

                for k, t in self._transform.items():
                    trans_r = t(r)
                    for f in self.prediction_fields:
                        predictions_transformed[k][f].append(getattr(trans_r, f))
                    for f in self.reference_fields:
                        references_transformed[k][f].append(getattr(trans_r, f))

            for k, m in self.metric.items():
                if k in self._transform:
                    self.add_batch_to_metric(m, k,
                                             predictions=predictions_transformed[k][self.prediction_field_for_metric[k]],
                                             references=references_transformed[k][self.reference_field_for_metric[k]])
                else:
                    self.add_batch_to_metric(m, k,
                                             predictions=predictions[self.prediction_field_for_metric[k]],
                                             references=references[self.reference_field_for_metric[k]])

        else:
            predictions = {k: [] for k in self.prediction_fields}
            references = {k: [] for k in self.reference_fields}

            for r in results:
                if self._transform is not None:
                    r = self._transform(r)
                for k in self.prediction_fields:
                    predictions[k].append(getattr(r, k))
                for k in self.reference_fields:
                    references[k].append(getattr(r, k))

            if isinstance(self.metric, evaluate.Metric):
                self.add_batch_to_metric(self.metric, "",
                                         predictions=predictions[self.prediction_field_for_metric],
                                         references=references[self.reference_field_for_metric])
            elif isinstance(self.metric, dict):
                for k, m in self.metric.items():
                    self.add_batch_to_metric(m, k,
                                             predictions=predictions[self.prediction_field_for_metric[k]],
                                             references=references[self.reference_field_for_metric[k]])
            else:   # iterable
                for m in self.metric:
                    self.add_batch_to_metric(m, "",
                                             predictions=predictions[self.prediction_field_for_metric],
                                             references=references[self.reference_field_for_metric])

    def compute(self, results: Optional[Sequence[R]] = None, **for_metric) -> Dict[str, Any]:
        """
        Computes the evaluation metrics.
        The evaluator is reset to the initial state.

        :param results: Optionally you can add results that should be added to results provided so far.
        :param for_metric: additional arguments that would be passed directly to metric compute
            the arguments are specified by metric key
            e.g.:
             for metric accuracy pass:
                accuracy={"threshold": 0.5}
        :return: evaluation metrics
        """
        if results is not None:
            self(results)

        if isinstance(self.metric, evaluate.Metric):
            return self.metric.compute(**for_metric)

        res = {}

        if isinstance(self.metric, dict):
            for k, m in self.metric.items():
                res[k] = m.compute(**(for_metric[k] if k in for_metric else {}))
        else:
            for m in self.metric:
                res.update(m.compute(**for_metric))

        return res
