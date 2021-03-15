"""Ingest text files using the native file library."""

from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
from typing import List


class TextIngestor(IngestorInterface):
    """Class to parse txt files."""

    input_files_formats = ['txt']


