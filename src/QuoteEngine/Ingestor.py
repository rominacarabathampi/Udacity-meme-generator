"""Encapsulate the ingestor models."""
from QuoteEngine.QuoteModel import QuoteModel
from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.CSVImporter import CSVImporter
from QuoteEngine.DocxImporter import DocxImporter
from QuoteEngine.PDFImporter import PDFImporter
from QuoteEngine.TextImporter import TextImporter
from typing import List


class Ingestor(IngestorInterface):
    """Encapsulate importer modules."""
    ingestors = [CSVImporter, DocxImporter, PDFImporter, TextImporter]

    @classmethod
    def parse(cls, path) -> List[QuoteModel]:
        """Parse files according to their file type."""
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
