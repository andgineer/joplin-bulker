[![CI status](https://github.com/andgineer/joplin-bulker/workflows/CI/badge.svg)](https://github.com/andgineer/joplin-bulker/actions)
# Joplin bulk tags remover

Python script to bulk remove tags from [Joplin](https://joplinapp.org) files.

It works with local files and does not use API.
So better to have the local Joplin files in some kind of auto-sync folder (Dropbox etc).

In this case all changes in the folder will auto-propagate to all your devices 
with Joplin installed.
    
### Installation

#### Python

To run the script you need [Python 3.6 or higher](https://www.python.org/getit/).

Install dependencies with

    python3 -m pip install requirements.txt

#### Configuration 

Specify `folder` with you Joplin files in `config.yaml`. 
    
### Usage

        python3 src/tag.py --rm=<tag name to remove> 
    
### History

I wrote this script because I need bulk tag removing.
As discussed in [Joplin forum](https://discourse.joplinapp.org/t/add-or-remove-tags-for-multiple-notes/4368/6)
in UI there is no command for tags bulk removing.

There is [Joplin command line](https://joplinapp.org/terminal/) but I wanted simple
code in Python that I could easily modify for my purposes. 

Also I wanted to get better understanding of the Joplin files structure.

As a bonus here we have Python code that can be
adjusted by anybody who prefer Python.
For example it would be easy to filter by note title or to find all
dangling tags and so on.
Or automate any bulk operation you want.



        
