from setuptools import setup, find_packages
import os

# Ensure README.md can be read
with open(os.path.join(os.path.dirname(__file__), "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="carter-analytics-python-sdk",
    version="0.1.0",
    description=(
        "The Carter Analytics SDK is a powerful tool for tracking and analyzing user interactions in your "
        "Python applications. It provides a straightforward way to capture a wide range of events and send "
        "them to the Carter Analytics platform for processing and analysis."
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shyftlabs/carter-analytics-python-sdk",
    packages=find_packages(exclude=("tests", "docs")),
    install_requires=[
        "requests>=2.31.0",
        "setuptools>=69.2.0",
        "tenacity>=8.2.3",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
)
