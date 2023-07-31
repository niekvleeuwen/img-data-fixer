import shutil
from pathlib import Path

from loguru import logger


def create_dir(directory: Path, clean_dir: bool) -> None:
    """Create a directory with the given name if it does not exist.

    Args:
        directory (str): The name of the directory to create.
        clean_dir (bool, optional): Whether to delete the directory if it already exists. Defaults to False.
    """
    if Path.exists(directory):
        if not clean_dir:
            raise FileExistsError(f"Directory {directory} already exists.")
        shutil.rmtree(directory)

    # Create the directory
    Path.mkdir(directory)


def files_in_dir(directory: Path) -> list:
    """Get all files in the directory.

    Args:
        directory (Path): The path to the directory.

    Returns:
        list: The list of files in the directory.
    """
    return [x for x in directory.glob("**/*") if x.is_file()]


def copy_files_to_dir(files: list[Path], destination_dir: Path) -> list[Path]:
    """Copies the files to the destination directory.

    Args:
        files (list): The list of files to move.
        destination_dir (Path): The path to the directory.

    Returns:
        list: The list of files in the directory.
    """
    copied_files = []

    if not destination_dir.exists() or not destination_dir.is_dir():
        raise ValueError("Destination directory does not exist or is not a directory.")

    for file_path in files:
        if not file_path.exists() or not file_path.is_file():
            logger.info(f"Skipping {file_path} - File does not exist.")
            continue

        destination_path = destination_dir / file_path.name
        shutil.copy(file_path, destination_path)
        copied_files.append(destination_path)

    return copied_files
