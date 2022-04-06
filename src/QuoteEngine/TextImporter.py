from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.QuoteModel import QuoteModel


class TextImporter(IngestorInterface):
    """Module to read TXT files"""

    allowed_extensions = ["txt"]

    @classmethod
    def parse(cls, path: str):
        """Parse the TXT files containing the quotes."""
        if not cls.can_ingest(path):
            raise Exception(f"File type not supported for {path}")

        quotes = []

        with open(path, 'r') as f:
            lines = f.readlines()

        for line in lines:
            body = line.split("-")[0].strip().strip('"')
            author = line.split("-")[1].strip()
            new_quote = QuoteModel(body, author)
            quotes.append(new_quote)
        return quotes
