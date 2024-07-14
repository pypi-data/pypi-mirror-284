#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ──────────────────────────────────────────────────────────────────────────────
import os

from setuptools import setup


# ──────────────────────────────────────────────────────────────────────────────
def _fread(fname: str):
    with open(
        os.path.join(os.path.dirname(__file__), fname), "r", encoding="utf-8"
    ) as fopen:
        return fopen.read()


# ──────────────────────────────────────────────────────────────────────────────

setup(
    name="richer_tqdm",
    version="0.0.2",
    description="Improved tqdm.rich decorator for iterators and associated machinery.",
    long_description=_fread("README.md"),
    long_description_content_type="text/markdown",
    keywords=["tqdm", "rich", "cli", "progress", "time", "bar", "progressbar"],
    author="Emanuele Ballarin",
    author_email="emanuele@ballarin.cc",
    url="https://github.com/emaballarin/richer_tqdm",
    license="MPL-2.0",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.7",
    include_package_data=False,
    zip_safe=True,
    install_requires=["tqdm>=4.66.4", "rich>=13.7.1", "safe_assert>=0.5.0"],
    packages=["richer_tqdm"],
)
