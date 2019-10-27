# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="pyflatted",
    version="0.0.1",
    description="Port of npm flatted library to Python",
    license="MIT",
    author="efabless Corporation",
    packages=["pyflatted"],
    install_requires=[],
    long_description=open("./Readme.md").read(),
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ]
)
