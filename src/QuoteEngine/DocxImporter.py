from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.QuoteModel import QuoteModel
import docx
from typing import List


class DocxImporter(IngestorInterface):
    """Module to read Docx files."""

    allowed_extensions = ["docx"]

    @classmethod
    def parse(cls, path) -> List[QuoteModel]:
        """Parse the Docx file containing the quotes."""
        if not cls.can_ingest(path):
            raise Exception(f"File type not supported for {path}")

        quotes = []
        document = docx.Document(path)

        for paragraph in document.paragraphs:
            if paragraph.text != "":
                parse = paragraph.text.split("-")
                new_quote = QuoteModel(parse[0], parse[1])
                quotes.append(new_quote)
        return quotes
