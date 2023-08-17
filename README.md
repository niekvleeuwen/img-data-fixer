# Image Date Fixer

Small Python CLI application to fill missing metadata of images based on the filename. This tool takes advantage of the filename structure to infer and correct metadata attributes for each image. The CLI offers various options to control the behavior of the correction process.

Example filename structures:

- 20151127_074841.jpg
- IMG_20160908_115420.jpg
- Screenshot_20171228-111228.png
- IMG-20160714-WA0001.jpg
- 2014-07-25 14.54.55.jpg

## Motivation

Managing and organizing a large collection of images can be a challenging task, especially when dealing with missing or incorrect metadata. I noticed that some of my images had missing metadata, but the correct date was present in the filename. So I decided to write a small CLI application to correct the metadata based on the filename. 

## Installation

Before using the program, you need to have Python and pip installed on your system. You can then install the CLI using the following steps:

1. Clone this repository or download the source code.
2. Open a terminal and navigate to the root directory of the repository.
3. Run the following command to install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

The application provides several options to customize the correction process. Here is the usage information for each parameter and option:

```bash
Usage: img_date_fixer [OPTIONS] ORIGINAL_DIR [CORRECTED_DIR]

  Correct image dates in the metadata and copy the images to the corrected
  directory.

Options:
  --clean    Delete the corrected directory if it already exists.
  --inplace  Overwrite the original images with the corrected images.
  --dry-run  Does not change the image metadata, but logs the changes that
             would be made.
  --help     Show this message and exit.
```

### Parameters

- `ORIGINAL_DIR`: The path to the directory containing the original images with missing metadata.
- `CORRECTED_DIR` (optional): The path to the directory where corrected images will be saved. Default is `"data/corrected/"`.

### Options

- `--clean`: If this flag is provided, the contents of the `CORRECTED_DIR` will be deleted before saving corrected images.
- `--inplace`: If this flag is provided, the original images will be overwritten with the corrected images.
- `--dry-run`: If this flag is provided, no actual changes will be made to the images. Instead, the CLI will log the changes that would be made.

### Examples

1. Basic usage with default settings:

```bash
img_date_fixer /path/to/original/images/
```

2. Specifying the corrected directory and using the inplace option:

```bash
img_date_fixer --inplace /path/to/original/images/ /path/to/corrected/images/
```

3. Performing a dry run to see the changes without actually modifying the images:

```bash
img_date_fixer --dry-run /path/to/original/images/
```

## Notes

- The CLI uses the filename structure to infer and correct metadata attributes. Make sure your filenames are appropriately formatted for accurate metadata correction.
- Always make sure to have backups of your original images before performing any modifications.
- The CLI may not be able to accurately correct all metadata attributes. Review the changes carefully before applying them to your images.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to reach out for any issues, suggestions, or contributions.