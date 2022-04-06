import os
import subprocess
import random
from typing import List

from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.QuoteModel import QuoteModel
from QuoteEngine.TextImporter import TextImporter


class PDFImporter(IngestorInterface):
    """Module to read PDF files."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path):
        text_file = './pdf_to_text.txt'
        with open('pdf_to_text.txt', 'w') as fp:
            pass
        cmd = f"./pdftotext -layout -nopgbrk {path} {text_file}"
        subprocess.call(cmd, shell=True, stderr=subprocess.STDOUT)
        quotes = TextImporter.parse(text_file)
        os.remove(text_file)
        return quotes
