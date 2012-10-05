import os.path
from glob import glob
from xml.etree import ElementTree

def _find_by_name(objects, name):
    """Find an object in the list of objects that has a name attribute that matches the given name."""
    matching_objects = [o for o in objects if o.name == name]
    if len(matching_objects) == 1:
        return matching_objects[0]
    else:
        return None

class Library(object):

    @classmethod
    def from_directory(cls, dirname):
        library_name = os.path.basename(dirname)
        library_fname = os.path.join(dirname, '%s.ndbx' % library_name)
        library = Library(library_name)
        et = ElementTree.parse(open(library_fname))
        root_node = et.find('node')
        library.description = root_node.attrib.get('description', 'No description')
        # Can't use a list comprehension here since we need prototype nodes to be available in self.nodes.
        for e in root_node.findall('node'):
            library.nodes.append(Node.from_element(library, e))
        return library

    @classmethod
    def find(cls, name):
        return _find_by_name(all_libraries, name)

    def __init__(self, name):
        self.name = name
        self.nodes = []

    @property
    def absolute_url(self):
        return '/%s' % self.name

    @property
    def directory(self):
        return os.path.join(NODE_LIBRARIES_DIRECTORY, self.name)

    @property
    def file(self):
        return os.path.join(self.directory, '%s.ndbx' % self.name)
        
    def find_node(self, name):
        return _find_by_name(self.nodes, name)

class Node(object):
    
    @classmethod
    def from_element(cls, library, e):
        n = Node(library, e.attrib['name'])
        n.prototype = library.find_node(e.attrib.get('prototype'))
        n.description = e.attrib.get('description')
        n.function = e.attrib.get('function')
        n.slow = n.function is not None and n.function.startswith('py')
        n.image = e.attrib.get('image')
        n.output_type = e.attrib.get('outputType', n.prototype and n.prototype.output_type)
        n.ports = [Port.from_element(n.name, pe) for pe in e.findall('port')]
        return n
    
    def __init__(self, library, name):
        self.library = library
        self.name = name
        
    @property
    def image_url(self, branch='master'):
        if self.image is not None:
            return 'http://github.com/nodebox/nodebox/raw/%s/libraries/%s/%s' % (branch, self.library.name, self.image)
        else:
            return 'http://placehold.it/26x26'
        
class Port(object):
    
    @classmethod
    def from_element(cls, node, e):
        p = Port(node, e.attrib['name'])
        p.type = e.attrib.get('type')
        p.value = e.attrib.get('value')
        return p
        
    def __init__(self, node, name):
        self.node = node
        self.name = name

