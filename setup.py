"""
Script for pip install
"""

import setuptools

setuptools.setup(
    name="joplin-bulker",
    description="Joplin assorted automation",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
)
