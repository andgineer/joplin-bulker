# Jopling bulk tags remover

As discussed in [Joplin forum](https://discourse.joplinapp.org/t/add-or-remove-tags-for-multiple-notes/4368/6)
there are no tools for tags bulk removing.

So I write this small util.

Of cause you can use [Joplin command line](https://joplinapp.org/terminal/) 
command 

    tag remove
    
But writing this util was easy and fun.
Also I wanted to get better understanding of the
Joplin files structure.

As a bonus here we have Python code that can be
adjusted by anybody who prefer Python.

For example it would be easy to filter by note title or to find all
dangling tags and so on.

Usage:

        python3 tag.py --rm=<tag name to remove> 
        