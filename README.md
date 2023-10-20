[![CI status](https://github.com/andgineer/joplin-bulker/workflows/CI/badge.svg)](https://github.com/andgineer/joplin-bulker/actions)
[![Coverage](https://raw.githubusercontent.com/andgineer/joplin-bulker/python-coverage-comment-action-data/badge.svg)](https://htmlpreview.github.io/?https://github.com/andgineer/joplin-bulker/blob/python-coverage-comment-action-data/htmlcov/index.html)
# Joplin assorted automation
(!) manipulate with old Joplin files, now this is only Export RAW.
Does not support last versions that use SQLite.

I happyly migrated to the Obsidian and do not use Joplin anymore, so this is unlikely to be developed further.

## Istallation

I had not published this package to PyPI, so you need to clone the repo and install it from sources:

    . ./activate.sh
    joplin-bulker --help

Note first dot, it is important.

## Functions

### Bulk tags remover

Python script to bulk remove tags from [Joplin](https://joplinapp.org) files.

        joplin-bulker tag ---rm=<tag name to remove>

## Usage

### Installation

To run the script you need [Python 3.10 or higher](https://www.python.org/getit/).

Install dependencies with

    . ./activate.sh

### Configuration

Specify `folder` with you Joplin files in `config.yaml`.

For the Joplin API to work you should enable Joplin Web Clipper Service - in Joplin Desktop application open `Preferences`
and enable it in `Web Clipper section`:

![](img/enable_clipper.png).

## Rationale

As discussed in [Joplin forum](https://discourse.joplinapp.org/t/add-or-remove-tags-for-multiple-notes/4368/6)
in UI there is no command for tags bulk removing.

There is [Joplin command line](https://joplinapp.org/terminal/) but I wanted simple
code in Python that I could easily modify for my purposes.

As a bonus here we have Python code that can be
adjusted by anybody who prefer Python.
For example it would be easy to filter by note title or to find all
dangling tags and so on.

## Implementation

We use [Joppy](https://github.com/marph91/joppy) to communicate with Joplin API.
