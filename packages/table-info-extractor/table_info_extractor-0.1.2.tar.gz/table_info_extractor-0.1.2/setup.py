from setuptools import setup, find_packages

setup(
    name="table_info_extractor",
    version="0.1.2",
    packages=find_packages(),
    install_requires=[
        "pdf2image",
        "img2table",
        "pytesseract",
        "Pillow",
        "ipython",
        "pandas",
        "opencv-python-headless",
    ],
    author="Rasel Meya",
    author_email="rhrasel94@gmail.com",
    description="A package for extracting tables from images and PDFs",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/raselmeya94/table_info_extractor",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
