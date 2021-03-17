"""Define QuoteModel object.

A Python class that defines a QuoteMode object,
which contains text fields for body and author.
The class overrides the correct methods
to instantiate the class and print the model
contents as: ”body text” - author
"""


class QuoteModel:
    """The class define QuoteModel object.

    The class overrides __repr__ method to concatenate
    body_text and author of outer data sources.
    """

    def __init__(self, body_text, author):
        """Class constructor."""
        self.body_text = body_text
        self.author = author

    def __repr__(self):
        """Representation for a QuoteModel object."""
        return f'{self.body_text} - {self.author}'
