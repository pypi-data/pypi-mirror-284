# coding: utf-8

# CodeArena Python SDK
# Author: Mingzhe Du (mingzhe@nus.edu.sg / mingzhe001@ntu.edu.sg)
# Date: 14 / 07 / 2024

from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='codearena',
    version='0.0.4',
    description='CodeArena Python SDK',
    author='Mingzhe Du',
    author_email='mingzhe@nus.edu.sg',
    url='https://codellm.club',
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3',
    install_requires=[],
)