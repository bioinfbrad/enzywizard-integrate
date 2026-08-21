#!/usr/bin/env python
from setuptools import setup, find_packages
import os

# Read the version from version.py without importing the package
version_file = os.path.join(os.path.dirname(__file__), 'src', 'enzywizard_integrate', 'version.py')
with open(version_file) as f:
    exec(f.read())  # defines __version__

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="enzywizard-integrate",
    version=__version__,                     # dynamically read from version.py (1.0.1)
    author="bioinfbrad",
    description=(
        "Integrate multiple EnzyWizard JSON reports and construct a protein / "
        "protein-substrate graph representation."
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bioinfbrad/enzywizard-integrate",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.10",
    install_requires=[
        "biopython>=1.86",          # for sequence handling (Bio.Data.IUPACData)
        "numpy>=1.23.5,<2",         # numerical operations (used in common_utils)
        # No other third-party dependencies are used; all other imports are from the standard library.
    ],
    entry_points={
        "console_scripts": [
            "enzywizard-integrate = enzywizard_integrate.cli:main",
        ],
    },
    include_package_data=True,
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ],
)
