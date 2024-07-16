# -*- coding: UTF-8 -*-
"""
Created on 01.03.23

:author:     Martin Dočekal
"""
from enum import Enum


class FileFormat(Enum):
    """
    Defines format of results file.
    """
    CSV = "csv"
    TSV = "tsv"
    JSONL = "jsonl"

    def file_extension(self) -> str:
        """
        Returns file extension for the format.

        :return: File extension.
        """
        return self.value
