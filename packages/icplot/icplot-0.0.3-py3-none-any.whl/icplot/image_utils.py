import logging
from pathlib import Path

from wand.image import Image
from wand.color import Color

logger = logging.getLogger(__name__)


def pdf_to_png(source_path: Path):
    png_filename = source_path.parent / f"{source_path.stem}.png"
    with Image(filename=source_path, resolution=300) as img:
        img.format = "png"
        img.background_color = Color("white")
        img.alpha_channel = "remove"
        img.save(filename=png_filename)
