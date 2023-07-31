from pathlib import Path

import click
from loguru import logger

from img_date_fixer.date_parsing import parse_image_filename_to_datetime
from img_date_fixer.file_utils import copy_files_to_dir, create_dir, files_in_dir
from img_date_fixer.img_fixer import set_image_date_taken


def correct_image_date(file: Path, dry_run: bool = False) -> None:
    """Correct the date taken in the image metadata.

    Args:
        file (Path): The path to the image.
        dry_run (bool, optional): Whether to actually change the image metadata. Defaults to False.
    """
    try:
        date_str = parse_image_filename_to_datetime(file.name)
    except ValueError as e:
        logger.warning(f"{file.name}: {e}")
        return

    if not dry_run:
        # Set the date taken in the image metadata
        set_image_date_taken(file, date_str)
        logger.info(f"Corrected {file} to date {date_str}")
    else:
        logger.info(f"Parsed {file} to date {date_str}")


@click.command()
@click.argument("original_dir", type=click.Path(exists=True))
@click.argument("corrected_dir", type=click.Path(), default="data/corrected/")
@click.option(
    "--clean",
    is_flag=True,
    help="Delete the corrected directory if it already exists.",
    default=False,
)
@click.option(
    "--inplace",
    is_flag=True,
    help="Overwrite the original images with the corrected images.",
    default=False,
)
@click.option(
    "--dry-run",
    is_flag=True,
    help="Does not change the image metadata, but logs the changes that would be made.",
    default=False,
)
def main(original_dir: str, corrected_dir: str, clean: bool, inplace: bool, dry_run: bool) -> None:
    """Correct image dates in the metadata and copy the images to the corrected directory."""
    original_directory = Path(original_dir)
    corrected_directory = Path(corrected_dir)

    if not dry_run:
        logger.info("Correcting target directory...")
        create_dir(corrected_directory, clean)

    logger.info("Gathering files...")
    files = files_in_dir(original_directory)
    logger.info(f"Found {len(files)} files")

    if not dry_run and not inplace:
        logger.info("Copying files to corrected directory...")
        files = copy_files_to_dir(files, corrected_directory)

    for file in files:
        correct_image_date(file, dry_run)


if __name__ == "__main__":
    main()
