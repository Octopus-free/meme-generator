"""Available for CLI execution."""

import os
import random
import argparse

from QuoteEngine import QuoteModel, Ingestor
from MemeGenerator import MemeGenerator


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given an path and a quote."""
    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path[0]

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeGenerator('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    cli_arguments = argparse.ArgumentParser(description='Meme generator')
    cli_arguments.add_argument('--path',
                               type=str,
                               help='a path to an image file')
    cli_arguments.add_argument('--body',
                               type=str,
                               help='a body to add to the image')
    cli_arguments.add_argument('--author',
                               type=str,
                               help='an author to add to the image')

    args = cli_arguments.parse_args()
    print(generate_meme(args.path, args.body, args.author))
