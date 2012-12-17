#!/usr/bin/python
# Extract as much as we can from the NDBX files for the reference documentation.

from glob import glob
from shutil import copyfile
import os

from ndbx import Library

SITE_ROOT = os.path.dirname(os.path.abspath(__file__))
PROJECTS_ROOT = os.path.dirname(SITE_ROOT)
NODE_LIBRARIES_DIRECTORY = os.path.join(PROJECTS_ROOT, 'nodebox', 'libraries')
NODE_REFERENCE_DIRECTORY = os.path.join(SITE_ROOT, 'node', 'reference')
NODE_REFERENCE_INDEX = os.path.join(NODE_REFERENCE_DIRECTORY, 'index.md')

library_directories = glob(os.path.join(NODE_LIBRARIES_DIRECTORY, '*'))
all_library_names = ['corevector', 'string', 'color', 'math', 'list', 'data', 'core']
all_libraries = [Library.from_directory(os.path.join(NODE_LIBRARIES_DIRECTORY, library_name)) \
    for library_name in all_library_names]

LIBRARY_NAME_MAP = {
    'corevector': 'geometry',
}

def humanize_library_name(name):
    """Make a human-readable name out of a library name."""
    return humanize(LIBRARY_NAME_MAP.get(name, name))

def humanize(name):
    """Make a human-readable name out of a node name."""
    return ' '.join([s.capitalize() for s in name.split('_')])

def page_name(fname):
    """Given a filename, returns the page name."""
    fname = os.path.basename(fname)
    return os.path.splitext(fname)[0]

def find_library_by_name(library_name):
    for l in all_libraries:
        if l.name == library_name:
            return l
    return None

def library_index(library, show_header=True):
    library_name = humanize_library_name(library.name)
    s = ''
    if show_header:
        s += library_name + '\n'
        s += '-' * len(library_name) + '\n'
    for node in library.nodes:
        s += '* [%s](/node/reference/%s/%s.html): %s\n' % (humanize(node.name), library.name, node.name, node.description)
    s += '\n'
    return s

def global_index_page():
    """Return the contents of the global reference index page."""
    s = '''---
layout: documentation
title: Node Reference
notes: AUTO-GENERATED - DO NOT EDIT. Use the autoref.py script to re-generate this file.
---
'''

    for library in all_libraries:
        s += library_index(library)
    return s

def library_index_page(library):
    """Return the contents of the library reference index page."""
    s = '''---
layout: documentation
library: %s
title: %s
notes: AUTO-GENERATED - DO NOT EDIT. Use the autoref.py script to re-generate this file.
---
''' % (library.name, humanize_library_name(library.name))
    s += library_index(library, show_header=False)
    return s

def _write_page(fname, contents, dry_run=False):
    """Write a page to the filesystem."""
    print "Generating %s" % fname
    if dry_run:
        print contents
    else:
        ensure_directory(os.path.dirname(fname))
        with open(fname, 'w') as f:
            f.write(contents)

def write_global_index_page(dry_run=False):
    """Generate the global reference index page."""
    _write_page(NODE_REFERENCE_INDEX, global_index_page(), dry_run)

def write_library_index_page(library_name=None, dry_run=False):
    """Generate the library reference index page."""
    library = find_library_by_name(library_name)
    fname = os.path.join(NODE_REFERENCE_DIRECTORY, library.name, 'index.md')
    _write_page(fname, library_index_page(library), dry_run)

def stub_page(library, node):
    """Return the contents of a stub documentation page."""
    s = '''---
layout: reference
library: %s
node: %s
title: %s
image: %s
---
%s

''' % (node.library.name, node.name, humanize(node.name), node.image, node.description)
    for port in node.ports:
        s += '* **%s**: %s\n' % (humanize(port.name), port.description)
    return s

def generate_stub_page(library, node, dry_run=False):
    """Generate a stub documentation for the given library and node."""
    fname = os.path.join(NODE_REFERENCE_DIRECTORY, library.name, node.name + '.md')
    print "%s %s/%s " % (fname, library.name, node.name)
    if dry_run:
        print stub_page(library, node)
    else:
        ensure_directory(os.path.join(NODE_REFERENCE_DIRECTORY, library.name))
        with open(fname, 'w') as f:
            f.write(stub_page(library, node))


def generate_stub_pages(library_name=None, dry_run=False):
    """Generate stub documentation pages."""
    amount = 0
    for library in all_libraries:
        if library_name is not None and library.name != library_name: continue
        ref_dir = os.path.join(NODE_REFERENCE_DIRECTORY, library.name)
        existing_page_files = glob(os.path.join(ref_dir, '*.md'))
        existing_page_names = [page_name(f) for f in existing_page_files]
        for node in library.nodes:
            if node.name not in existing_page_names:
                amount += 1
                generate_stub_page(library, node, dry_run)

    print "%s stub page(s) generated." % amount

def ensure_directory(dir):
    """Ensure the given directory exists."""
    try:
        os.makedirs(dir)
    except OSError, e:
        if e.errno == 17:
            pass
        else:
            raise e

def copy_icons(library_name=None, dry_run=False):
    """Copy node icons from the source to the documentation."""
    for library in all_libraries:
        if library_name is not None and library.name != library_name: continue
        src_dir = os.path.join(NODE_LIBRARIES_DIRECTORY, library.name)
        for node in library.nodes:
            src_icon = os.path.join(src_dir, node.image)
            dst_icon = os.path.join(NODE_REFERENCE_DIRECTORY, library.name, node.image)
            if not os.path.exists(src_icon):
                print "WARNING source icon %s for node %s/%s does not exist!" % (node.image, library.name, node.name)
                continue
            if os.path.exists(dst_icon):
                continue
            print "Copy %s to %s" % (src_icon, dst_icon)
            if not dry_run:
                ensure_directory(os.path.join(NODE_REFERENCE_DIRECTORY, library.name))
                copyfile(src_icon, dst_icon)

def is_empty(s):
    """Check if the string has only whitespace in it."""
    if s is None: return True
    return len(s.strip()) == 0

def check_reference(library_name=None):
    """Check the NDBX files for documentation errors."""
    for library in all_libraries:
        if library_name is not None and library.name != library_name: continue
        for node in library.nodes:
            if is_empty(node.description):
                print '%s/%s: Node has no description.' % (library.name, node.name)
            elif not node.description.endswith('.'):
                print '%s/%s: Node description does not end with period. ("%s")' % (library.name, node.name, node.description)
            for port in node.ports:
                if is_empty(port.description):
                    print '%s/%s.%s: Port has no description.' % (library.name, node.name, port.name)
                elif not port.description.endswith('.'):
                    print '%s/%s.%s: Port description does not end with period. ("%s")' % (library.name, node.name, port.name, port.description)
            if node.image is None:
                print "%s/%s: No icon specified." % (library.name, node.name)
            else:
                icon_fname = os.path.join(NODE_LIBRARIES_DIRECTORY, library.name, node.image)
                if not os.path.exists(icon_fname):
                    print "%s/%s: Icon %s does not exist." % (library.name, node.name, node.image)
 
command_docs='''Commands:
    index: Generate the reference index page.
    stub:  Generate stub API pages for all nodes that do not have a page yet.
    check: Check the NDBX files for missing or faulty descriptions.
    icons: Copy icons from the nodebox project to the website.
'''

if __name__=='__main__':
    import sys
    import argparse

    parser = argparse.ArgumentParser(description=command_docs, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('command', help='The command to run. Either index, stub or check.')
    parser.add_argument('--library', help='If specified, only generate/check this library.', required=False)
    parser.add_argument('--dry-run', action='store_true', help='Don\'t actually create the files, just show the contents.')
    args = parser.parse_args()

    if args.command == 'index':
        if args.library is None:
            write_global_index_page(args.dry_run)
            for library in all_libraries:
                write_library_index_page(library.name, args.dry_run)
        else:
            write_library_index_page(args.library, args.dry_run)
    elif args.command == 'stub':
        generate_stub_pages(args.library, args.dry_run)
    elif args.command == 'icons':
        copy_icons(args.library, args.dry_run)
    elif args.command == 'check':
        check_reference(args.library)
    else:
        print 'Unknown command "%s".' % command
        print usage()

