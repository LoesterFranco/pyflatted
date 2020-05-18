# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("Readme.md").read()
except IOError:
    long_description = ""

setup(
    name="pyflatted",
    version="0.1.0",
    description="Port of the npm 'flatted' library to python",
    license="MIT",
    author="efabless Corporation",
    packages=["pyflatted"],
    install_requires=[],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ]
)
