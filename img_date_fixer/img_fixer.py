from datetime import datetime
from pathlib import Path

import piexif
from loguru import logger
from PIL import Image


def set_image_date_taken(path: Path, datetime_taken: datetime) -> None:
    """Set the date taken in the image metadata.

    Args:
        path (Path): The path to the image.
        datetime_taken (datetime): The date and time to set in the image metadata.
    """
    path = str(path)

    # Format the datetime as a string
    datetime_taken_str = datetime_taken.strftime("%Y:%m:%d %H:%M:%S")

    # Load the EXIF data
    try:
        exif_dict = piexif.load(path)
    except piexif.InvalidImageDataError:
        # If the image is not a JPG, convert it to JPG
        convert_to_jpg(path)
        exif_dict = piexif.load(path)

    # Set the date taken in the EXIF data
    exif_dict["0th"][piexif.ImageIFD.DateTime] = datetime_taken_str
    exif_dict["Exif"][piexif.ExifIFD.DateTimeOriginal] = datetime_taken_str
    exif_dict["Exif"][piexif.ExifIFD.DateTimeDigitized] = datetime_taken_str

    exif_bytes = piexif.dump(exif_dict)
    piexif.insert(exif_bytes, path)


def convert_to_jpg(path: str) -> None:
    """Convert the image to JPG format.

    Args:
        path (str): The path to the image.
    """
    logger.info(f"Converting {path} to JPG")
    im = Image.open(path)
    im = im.convert("RGB")
    im.save(path, "jpeg")
