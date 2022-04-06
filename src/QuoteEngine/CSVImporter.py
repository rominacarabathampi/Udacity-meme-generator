from QuoteEngine.IngestorInterface import IngestorInterface
import sys
import pandas as pd
from typing import List
from QuoteEngine.QuoteModel import QuoteModel

sys.path.append("src/data/quote_engine")


class CSVImporter(IngestorInterface):
    """Module to read CSV files."""

    allowed_extensions = ["csv"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the CSV files containing the quotes."""
        if not cls.can_ingest(path):
            raise Exception(f"File type not supported for {path}")

        quotes = []
        df = pd.read_csv(path, header=0)

        for index, row in df.iterrows():
            new_dog_quote = QuoteModel(row["body"], row["author"])
            quotes.append(new_dog_quote)
        return quotes
