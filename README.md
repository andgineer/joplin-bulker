[![CI status](https://github.com/andgineer/joplin-bulker/workflows/CI/badge.svg)](https://github.com/andgineer/joplin-bulker/actions)
# Joplin assorted automation

## Functions

### Import books reviews from goodreads

Work in progress, see `import_goodreads.py`.

### Bulk tags remover

Python script to bulk remove tags from [Joplin](https://joplinapp.org) files.

It works with local files and does not use API.
So better to have the local Joplin files in some kind of auto-sync folder (Dropbox etc).

In this case all changes in the folder will auto-propagate to all your devices 
with Joplin installed.

        python src/tag.py --rm=<tag name to remove> 

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
