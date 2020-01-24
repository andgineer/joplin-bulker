# Jopling bulk tags remover

As discussed in [Joplin forum](https://discourse.joplinapp.org/t/add-or-remove-tags-for-multiple-notes/4368/6)
there are no tools for tags bulk removing.

So I write this small util.

In fact I am pretty sure there is something in command line Joplin tools but
it was fun just to beter understand Joplin files structure.

And now we have code that we can adjust for our purposes.

For example it would be easy to filter by note title or to find all
dangling tags and so on.

Usage:

        python3 tag.py --rm=<tag name to remove> 
        