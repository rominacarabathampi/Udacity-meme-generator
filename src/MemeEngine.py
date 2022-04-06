from PIL import Image, ImageFont, ImageDraw
from PIL import Image, ImageDraw
from QuoteEngine.QuoteModel import QuoteModel
import os
import random


class InvalidFilePath(Exception):
    pass


class MemeEngine:
    """Generate a meme image."""

    def __init__(self, path):
        """Initialize meme engine with path name."""
        self.path = path
        if not os.path.exists(path):
            os.makedirs(path)
        self.temp_path = path

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Generate Meme using the image path and quote model."""
        out_file = f"{self.temp_path}/{random.randint(0,1000000)}.jpg"

        if width >= 500:
            width = 500
        try:
            with Image.open(img_path) as image:
                ratio = image.height / image.width
                height = image.width * ratio
                image = image.resize((int(width), int(height)))
                font_size = int(image.height/20)

                draw = ImageDraw.Draw(image)
                font = ImageFont.truetype(
                    './_data/NotoSerifDisplay-Black.ttf', font_size)

                x = random.randint(0, int(image.width/4))
                y = random.randint(0, int(image.height-font_size*2))

                draw.text((x, y), text, font=font, fill=(0, 0, 0))
                draw.text((int(x*1.2), y+font_size), ' - '+author, font=font)
                image.save(out_file, "JPEG")

        except Exception:
            raise InvalidFilePath("Invalid image path")

        return out_file
