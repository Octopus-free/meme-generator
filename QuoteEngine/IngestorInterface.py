"""A class to parsing files."""

from .QuoteModel import QuoteModel
from abc import ABC, abstractmethod
from typing import List


class IngestorInterface(ABC):
    """Class for parsing files.

    The class implement two methods:
    1. To verify if the file type is compatible with the ingestor class.
    2. To parse a file content.
    """

    input_files_formats = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Determine a file extension."""
        file_extension = path.split('.')[-1]
        return file_extension in cls.input_files_formats

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a file content."""
        pass