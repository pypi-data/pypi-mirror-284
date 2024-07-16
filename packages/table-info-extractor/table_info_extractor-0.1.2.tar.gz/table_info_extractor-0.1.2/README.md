# Table Info Extractor

Table Info Extractor is a Python package designed for extracting tables from images and PDFs using OCR (Optical Character Recognition). It supports automatic rotation detection, image preprocessing, and conversion of extracted tables into pandas DataFrames.

## Features

- Extract tables from images and PDFs.
- Automatically detect and correct image orientation.
- Enhance OCR results with preprocessing techniques (grayscale conversion, contrast enhancement, thresholding).
- Convert extracted tables into pandas DataFrames for easy data manipulation and analysis.

## Installation

You can install Table Info Extractor via pip:

```bash

pip install table_info_extractor

```

## Usage

### Image To Table Extraction

``` python
from table_info_extractor import image_to_table_extract

# Example: Extract tables from an image
extracted_tables_from_image = image_to_table_extract("path_to_your_image.jpg", auto_rotation=True)
print(extracted_tables_from_image)

```


### PDF To Table Extraction

```python
from table_info_extractor import pdf_to_table_extract

# Example: Extract tables from a PDF
extracted_tables_from_pdf = pdf_to_table_extract("path_to_your_pdf.pdf", page_number=1, auto_rotation=True)
print(extracted_tables_from_pdf)

```

## Function Documentation

### `image_to_table_extract(image_path, auto_rotation=False)`

Extracts tables from an image file.

- `image_path` (str): Path to the input image file.
- `auto_rotation` (bool): Whether to automatically correct image rotation.

Returns:
- List of pandas DataFrames, each representing a table extracted from the image.

### `pdf_to_table_extract(pdf_path, page_number, auto_rotation=False)`

Extracts tables from a specific page of a PDF file.

- `pdf_path` (str): Path to the input PDF file.
- `page_number` (int): Page number from which to extract tables (1-based index).
- `auto_rotation` (bool): Whether to automatically correct image rotation.

Returns:
- List of pandas DataFrames, each representing a table extracted from the PDF page.

## Contribution

Contributions are welcome! To contribute to Table Info Extractor, please follow these steps:

1. Fork the repository and clone it to your local machine.
2. Create a new branch for your feature or bug fix: `git checkout -b feature/my-feature`.
3. Make your changes and commit them with a descriptive message.
4. Push your changes to the branch: `git push origin feature/my-feature`.
5. Submit a pull request detailing your changes and why they should be included.

## GitHub Repository

[Table Data Extractor on GitHub](https://github.com/raselmeya94/table_info_extractor)
