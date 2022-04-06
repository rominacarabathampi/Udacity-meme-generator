"""Module for Quote Model Class."""


class QuoteModel:
    """The template for quotes."""

    def __init__(self, author, body):
        """Create a new Quote model.

        :param body: content of the quote
        :param author: author of the quote"""
        self.author = author
        self.body = body

    def __repr__(self):
        """Return an easier text to read of the quote: text - author."""
        return f"{self.body} - {self.author}"
