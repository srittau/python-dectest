#!/usr/bin/env python

import os

from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="dectest",
    version="2.0.0",
    description="Improved TestCase class",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Sebastian Rittau",
    author_email="srittau@rittau.biz",
    url="https://github.com/srittau/python-dectest",
    packages=["dectest"],
    package_data={"dectest": ["py.typed"]},
    tests_require=["asserts >= 0.8.0, < 0.12"],
    python_requires=">=3.7"
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Software Development :: Testing",
    ],
)
