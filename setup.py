import codecs
import os
import os.path

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.in") as f:
    requirements = f.read().splitlines()

with open("requirements.dev.in") as f:
    tests_requirements = f.read().splitlines()


# Solution from https://packaging.python.org/guides/single-sourcing-package-version/
def read(rel_path: str) -> str:
    """Read file."""
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), "r") as fp:
        return fp.read()


def get_version(rel_path: str) -> str:
    """Parse version from file content."""
    for line in read(rel_path).splitlines():
        if line.startswith("VERSION"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")


setuptools.setup(
    name="joplin-bulker",
    version=get_version("src/joplin_bulker/version.py"),
    author="Andrey Sorokin",
    author_email="andrey@sorokin.engineer",
    description=("Assorted Joplin automation."),
    entry_points={
        "console_scripts": [
            "joplin-bulker=joplin_bulker.main:cli",
        ],
    },
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://andgineer.github.io/joplin-bulker/",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=requirements,
    extras_require={'test': tests_requirements},
    python_requires=">=3.9",
    keywords="Joplin",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
