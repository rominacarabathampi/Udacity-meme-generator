"""Module to declare the absctract class interface."""
from abc import ABC, abstractmethod
from typing import List
from QuoteEngine.QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """Abstract class for file ingestion."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Verify the path is valid for each ingester class."""
        ext = path.split(".")[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Abstract method to parse each type of file. This is customized by each ingester."""
        pass
