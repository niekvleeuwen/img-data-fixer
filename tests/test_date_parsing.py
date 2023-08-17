from datetime import datetime

import pytest

from img_date_fixer.main import parse_image_filename_to_datetime


# Define test cases
@pytest.mark.parametrize(
    "filename, expected",
    [
        ("20151127_074841.jpg", datetime(2015, 11, 27, 7, 48, 41)),
        ("IMG_20160908_115420.jpg", datetime(2016, 9, 8, 11, 54, 20)),
        ("Screenshot_20171228-111228.png", datetime(2017, 12, 28, 11, 12, 28)),
        ("IMG-20160714-WA0001.jpg", datetime(2016, 7, 14, 0, 0, 0)),
        ("2014-07-25 14.54.55.jpg", datetime(2014, 7, 25, 14, 54, 55)),
    ],
)
def test_parse_image_filenames_to_datetime(filename, expected):
    result = parse_image_filename_to_datetime(filename)
    assert result == expected


def test_invalid_parse_image_filenames_to_datetime():
    with pytest.raises(ValueError):
        parse_image_filename_to_datetime("9edfe7a10a6845bb7043ab1e56d741b4.jpg")
