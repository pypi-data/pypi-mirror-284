from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="mac-ocr-cli",
    version="0.1.0",
    author="dielect",
    author_email="dielectric.army@gmail.com",
    description="A CLI tool for OCR on macOS using FastAPI and ocrmac",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dielect/mac-ocr-api",
    packages=find_packages(),
    install_requires=[
        "typer",
        "fastapi",
        "uvicorn",
        "pillow",
        "ocrmac",
        "pydantic",
        "rich",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "mac-ocr=macocr_cli.__main__:cli",
        ],
    },
)