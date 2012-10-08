#!/usr/bin/python
# Extract as much as we can from the NDBX files for the reference documentation.

from glob import glob
import os

from ndbx import Library

SITE_ROOT = os.path.dirname(os.path.abspath(__file__))
PROJECTS_ROOT = os.path.dirname(SITE_ROOT)
NODE_LIBRARIES_DIRECTORY = os.path.join(PROJECTS_ROOT, 'nodebox', 'libraries')

library_directories = glob(os.path.join(NODE_LIBRARIES_DIRECTORY, '*'))
all_libraries = [Library.from_directory(dirname) for dirname in library_directories]

LIBRARY_NAME_MAP = {
    'corevector': 'geometry',
}

def human_library_name(name):
    return humanize(LIBRARY_NAME_MAP.get(name, name))

def humanize(name):
    return ' '.join([s.capitalize() for s in name.split('_')])

def reference_index_page():
    s = '''---
layout: documentation
title: Node Reference
notes: AUTO-GENERATED - DO NOT EDIT. Use the extract_reference.py script to re-generate this file.
---
'''

    for library in all_libraries:
        library_name = human_library_name(library.name)
        s += library_name + '\n'
        s += '-' * len(library_name) + '\n'
        for node in library.nodes:
            s += '* [%s](%s/%s.html): %s\n' % (humanize(node.name), library.name, node.name, node.description)
        s += '\n'
    return s

if __name__=='__main__':
    with open('node/reference/index.md', 'w') as f:
        f.write(reference_index_page())