#!/usr/bin/env python3
from setuptools import find_packages, setup
setup(
    name="lilt",
    version="1.0",
    author="Deep Learning and Vision Computing Lab, SCUT",
    packages=find_packages(where="lilt"),
    package_dir={'': 'lilt'},
    python_requires=">=3.10",
    extras_require={"dev": ["flake8", "isort", "black"]},
)