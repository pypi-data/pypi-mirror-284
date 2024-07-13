from setuptools import setup, find_packages

# Read content from README.md
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="easy_passgen",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    author="easyPete",
    description="An easy to use password generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
)
