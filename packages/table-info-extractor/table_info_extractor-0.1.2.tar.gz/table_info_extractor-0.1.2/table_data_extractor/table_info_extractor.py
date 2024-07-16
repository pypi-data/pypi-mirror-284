from pdf2image import convert_from_path
from img2table.ocr import TesseractOCR
from img2table.document import Image
from img2table.document import PDF
from IPython.display import display, HTML
from collections import OrderedDict
from PIL import ImageOps, ImageEnhance, Image as image_pil
from io import BytesIO
import pytesseract
import pandas as pd
import re
import os
import cv2
import warnings
import base64

warnings.filterwarnings("ignore")

# Suppress DecompressionBombWarning in Pillow
image_pil.MAX_IMAGE_PIXELS = None  # Disable decompression bomb error

#=================================================================================== < Preprocessing Image > ==================================================================

def preprocess_image(image):
    """
    Preprocesses an image by converting it to grayscale, enhancing contrast,
    and applying thresholding.

    Args:
    - image (PIL.Image.Image): Input image object.

    Returns:
    - PIL.Image.Image: Preprocessed image.
    """
    grayscale_image = ImageOps.grayscale(image)
    enhancer = ImageEnhance.Contrast(grayscale_image)
    enhanced_image = enhancer.enhance(2)
    threshold_image = enhanced_image.point(lambda p: p > 128 and 255)
    
    return threshold_image

#=================================================================================== < Table Text Rotation Checker > ============================================================

def auto_rotation_checker(image):
    """
    Checks and corrects the rotation angle of a given image based on OCR output.

    Args:
    - image (PIL.Image.Image): Input image object.

    Returns:
    - int: Corrected rotation angle in degrees.
    """
    try:
        osd = pytesseract.image_to_osd(image)
        rotation_angle = int(re.search('(?<=Rotate: )\d+', osd).group(0))
        
        if rotation_angle == 0:
            correction_angle = 0
        elif rotation_angle == 90:
            correction_angle = 270  # counterclockwise
        elif rotation_angle == 180:
            correction_angle = 180
        elif rotation_angle == 270:
            correction_angle = 90  # clockwise
        else:
            correction_angle = 0
        
    except Exception as e:
        print(f"Error detecting orientation: {e}")
        correction_angle = 0
    
    return correction_angle

#=================================================================================== < Table into Convert Dataframe > ============================================================

def table_to_dataframe(table):
    """
    Converts a table object into a pandas DataFrame.

    Args:
    - table (Table object): Input table object.

    Returns:
    - pandas.DataFrame: DataFrame containing table data.
    """
    rows = []
    for row_idx, row_cells in table.content.items():
        row = []
        for cell in row_cells:
            row.append(cell.value)
        rows.append(row)

    df = pd.DataFrame(rows)
    if df.empty or df.columns.empty:
        print("The DataFrame is empty or columns are not properly set.")
        return df

    df.columns = df.iloc[0]
    df = df[1:]

    if df.columns is None:
        print("Columns are None, cannot process further.")
        return df

    df.columns = df.columns.str.replace('\n', ' ')
    df = df.replace('\n', ' ', regex=True)

    return df

#=================================================================================== < Image to Table Extraction > ============================================================

def image_to_table_extract(image_path, auto_rotation=False):
    """
    Extracts tables from an image file.

    Args:
    - image_path (str): Path to the input image file.
    - auto_rotation (bool): Whether to automatically correct image rotation.

    Returns:
    - list: List of pandas DataFrames, each representing a table extracted from the image.
    """
    image = image_pil.open(image_path).convert("RGB")
    
    rotated_angle = 0
    if auto_rotation:
        rotated_angle = auto_rotation_checker(image)
        
    rotated_image = image.rotate(rotated_angle, expand=True)
    preprocessed_image = preprocess_image(rotated_image)
    
    buffer = BytesIO()
    preprocessed_image.save(buffer, format="JPEG")
    buffer.seek(0)
    
    ocr = TesseractOCR(n_threads=1, lang="eng")
    doc = Image(buffer)
    
    extracted_tables = doc.extract_tables(ocr=ocr,
                                          implicit_rows=False,
                                          borderless_tables=False,
                                          min_confidence=50)
    
    tables_data = [table_to_dataframe(table) for table in extracted_tables]
    return tables_data

#=================================================================================== < PDF to Table Extraction > ============================================================

def pdf_to_table_extract(pdf_path, page_number, auto_rotation=False):
    """
    Extracts tables from a specific page of a PDF file.

    Args:
    - pdf_path (str): Path to the input PDF file.
    - page_number (int): Page number from which to extract tables (1-based index).
    - auto_rotation (bool): Whether to automatically correct image rotation.

    Returns:
    - list: List of pandas DataFrames, each representing a table extracted from the PDF page.
    """
    pages = convert_from_path(pdf_path)

    for i, page in enumerate(pages, start=1):
        if i == page_number:
            rotated_angle = 0
            if auto_rotation:
                rotated_angle = auto_rotation_checker(page)

            rotated_image = page.rotate(rotated_angle, expand=True)

            with BytesIO() as image_stream:
                rotated_image.save(image_stream, format='JPEG')
                image_stream.seek(0)
                extracted_tables_from_pdf = image_to_table_extract(image_stream)

                return extracted_tables_from_pdf
