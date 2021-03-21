"""Crop an image, add a text and save it."""

import os
from PIL import Image, ImageDraw, ImageFont
from random import randint


class MemeGenerator:
    """Change an image and save it."""

    def __init__(self, output_dir):
        """Initialize the class state."""
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Make a meme."""
        # load an image
        input_image = Image.open(img_path)

        # transform the image parameters
        transform_width = min(width, 500)
        transform_ratio = transform_width/float(input_image.size[0])
        transform_height = int(transform_ratio * float(input_image.size[1]))

        # resize an input image
        resized_image = input_image.resize(
            (transform_width, transform_height), Image.NEAREST
        )

        # add a text to the resized image
        text_length = len(text) + len(author)
        text_body = f'{text} {author}'
        draw_image = ImageDraw.Draw(resized_image)
        font_image = ImageFont.truetype(
            './_data/fonts/LilitaOne-Regular.ttf',
            size=18)
        draw_image.text(
            (randint(0, text_length), randint(0, text_length)),
            text_body,
            font=font_image,
            fill='white'
        )

        # write the image with the text do a disk
        out_path = os.path.join(self.output_dir,
                           f'{text_body} on an image.png')

        resized_image.save(out_path)

        return out_path
