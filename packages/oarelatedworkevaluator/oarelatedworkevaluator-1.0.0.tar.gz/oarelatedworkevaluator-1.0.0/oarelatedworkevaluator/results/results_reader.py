# -*- coding: UTF-8 -*-
"""
Created on 01.03.23
Reader of results with defined type and file format

:author:     Martin Dočekal
"""
import csv
import json
from dataclasses import fields
from typing import Type, Iterable, Optional

from tqdm import tqdm

from oarelatedworkevaluator.results.result import EmptyResult
from oarelatedworkevaluator.utils.general_entities import FileFormat

# the default is too small: 131072, lets set it to 100MB
csv.field_size_limit(100 * 1024 * 1024)


class JSONLReader:
    """
    Class for reading JSONL files.
    """
    def __init__(self, lines: Iterable[str]):
        """
        Initialization of JSONL reader.

        :param lines: lines of JSONL file
        """
        self.lines = lines

    def __iter__(self):
        for line in self.lines:
            yield json.loads(line)


class ResultsReader:
    """
    Class for results reading. It will read all results into memory.
    Usage:
    >>> for result in ResultsReader(path_to, result_type, format):
    >>>     print(result)


    """

    def __init__(self, path_to: str, result_type: Type[EmptyResult], f: Optional[FileFormat] = None,
                 headline: bool = True, verbose: bool = False):
        """
        Initialization of results reader for given result type.

        :param path_to: path to file with results
        :param result_type: result class that is used to determine result fields
        :param f: format of output file, if None it will be determined from the file extension
        :param headline: whether the headline is present (only for formats with voluntary headline)
        :param verbose: Whether to print progress.
        """

        self.path_to = path_to
        self.result_type = result_type
        self.format = f
        if self.format is None:
            for f in FileFormat:
                if path_to.endswith(f.value):
                    self.format = f
                    break
            else:
                raise ValueError("Unknown file format.")

        self.headline = headline

        self.results = []
        with open(path_to, "r") as f:
            if self.format == FileFormat.JSONL:
                reader = JSONLReader(f)
            elif self.format == FileFormat.CSV or self.format == FileFormat.TSV:
                fieldnames = None if self.headline else [f.name for f in fields(result_type)]
                reader = csv.DictReader(f, delimiter="," if self.format == FileFormat.CSV else "\t",
                                        fieldnames=fieldnames)
            else:
                raise AttributeError("unsupported format")

            field_types = {f.name: f.type for f in fields(result_type)}
            aliases_map = {}

            for f in fields(result_type):
                if "aliases" in f.metadata:
                    for a in f.metadata["aliases"]:
                        if a in aliases_map or a in field_types:
                            raise ValueError(f"Alias {a} is already used for field {aliases_map[a]}.")
                        aliases_map[a] = f.name

            for row in tqdm(reader, desc="Reading results", disable=not verbose):
                # pass only arguments that are in result_type
                param_val_map = {}
                for k, v in row.items():
                    k = aliases_map.get(k, k)

                    if k in field_types:
                        param_val_map[k] = v

                        # convert to proper types
                        try:
                            if field_types[k] is not None and v is not None:
                                param_val_map[k] = field_types[k](v)
                        except TypeError:
                            ...

                self.results.append(self.result_type(**param_val_map))

    def __len__(self):
        return len(self.results)

    def __iter__(self):
        return iter(self.results)

    def __getitem__(self, item):
        return self.results[item]
