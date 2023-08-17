import re
from datetime import datetime


def parse_image_filename_to_datetime(filename: str) -> datetime:
    """Parse the date and time from the image file name.

    Args:
        filename (str): The file name of the image.

    Returns:
        datetime: The date and time parsed from the file name.

    Raises:
        ValueError: If the file name does not match any of the patterns.
    """
    # Define regular expression for different file name patterns
    patterns = [
        r"(\d{8})_(\d{6})",
        r"(\d{8})-(\d{6})",
        r"-(\d{8})-",
        r"(\d{4}-\d{2}-\d{2}) (\d{2}\.\d{2}\.\d{2})",
        r"(\d{4}-\d{2}-\d{2})-(\d{2}-\d{2}-\d{2})",
    ]
    combined_pattern = "|".join(patterns)

    if match := re.search(combined_pattern, filename):
        match_groups = [match for match in match.groups() if match is not None]
        if match_groups:
            date_str = match_groups[0].replace("-", "")
            time_str = match_groups[1].replace(".", "") if len(match_groups) > 1 else None

            date = datetime.strptime(date_str, "%Y%m%d")

            # If time is present, use it. Otherwise, set time to 00:00:00
            if time_str and len(time_str) == 6:
                time = datetime.strptime(time_str, "%H%M%S")
                return datetime.combine(date, time.time())

            return date.replace(hour=0, minute=0, second=0)

    # If no pattern matches
    raise ValueError("filename did not match any pattern.")
