from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name=’TestLibrarySimpleMath’,
    version=’0.0.1',
    author=’Test’,
    description=’My first Python library’,
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/HugoORCA/TestLibrary1.git"
    packages= setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)