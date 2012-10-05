#!/usr/bin/python
# Extract as much as we can from the NDBX files for the reference documentation.

from glob import glob
import os

from ndbx import *

SITE_ROOT = os.path.dirname(os.path.abspath(__file__))
PROJECTS_ROOT = os.path.dirname(SITE_ROOT)
NODE_LIBRARIES_DIRECTORY = os.path.join(PROJECTS_ROOT, 'nodebox', 'libraries')

library_directories = glob(os.path.join(NODE_LIBRARIES_DIRECTORY, '*'))
all_libraries = [Library.from_directory(dirname) for dirname in library_directories]

LIBRARY_NAME_MAP = {
  'corevector': 'geometry',
  'coreimage': 'image'
}

def human_library_name(name):
  return humanize(LIBRARY_NAME_MAP.get(name, name))

def humanize(name):
   return ' '.join([s.capitalize() for s in name.split('_')])

print """---
layout: documentation
title: Node Reference
---"""

for library in all_libraries:
  library_name = human_library_name(library.name)
  print library_name
  print '-' * len(library_name)
  for node in library.nodes:
    print "* [%s](%s/%s.html): %s""" % (humanize(node.name), library.name, node.name, node.description)
  print

