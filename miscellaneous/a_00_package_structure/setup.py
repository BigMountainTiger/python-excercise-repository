import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="mypack",
    version="1.0.0",
    description="My Test Python Package",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/BigMountainTiger/python-excercise-repository",
    author="Song Li",
    author_email="da_tou_li@yahoo.com",
    license="MIT",
    classifiers=[
        "License :: MIT License",
        "Programming Language :: Python :: 3.8"
    ],
    packages=["mypack"],
    include_package_data=True,
    install_requires=[],
    entry_points={},
)