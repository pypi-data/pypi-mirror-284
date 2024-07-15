from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="gsheet-manager",
    version="0.3.0",
    author="Seong Joon Oh",
    author_email="coallaoh@gmail.com",
    description="A Google Sheets manager for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/coallaoh/gsheet-manager",
    packages=find_packages(),
    install_requires=[
        "gspread>=5.0.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)