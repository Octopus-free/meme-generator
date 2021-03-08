class QuoteModel:
    """The class define QuoteModel object.

    The class overrides __repr__ method to concatenate
    body_text and author of outer data sources.

    """
    def __init__(self, body_text, author):
        self.body_text = body_text
        self.author = author

