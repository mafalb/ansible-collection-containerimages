#!/usr/bin/env python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
from ansible.module_utils.basic import AnsibleModule

try:
    import yaml
except ImportError as e:
    YAML_IMPORT_ERROR = e
else:
    YAML_IMPORT_ERROR = None

import json
import sys


class Containerimages:

    def __init__(self, datafile=None):
        if datafile:
            datafile = open(datafile, 'r')
            self.data = yaml.load(datafile, Loader=yaml.Loader)
        else:
            self.data = yaml.load(sys.stdin, Loader=yaml.Loader)
        if datafile:
            datafile.close()

    def yaml_to_json(self, images):
        """Return json."""
        return json.dumps(self.data)

    def list_os(self, format='text'):
        """Return Operating Systems."""
        return list(self.data["images"].keys())

    def list_images(self, os):
        """Return a list of images for a given Operating System."""
        images = []
        for image in self.data["images"][os]:
            images.append(image['flavor'])
        return images

    def get_attribute(self, os, flavor, attribute):
        """Return an attribute for a given image."""
        for __flavor in self.data['images'][os]:
            if (__flavor['flavor'] == flavor):
                __data = __flavor
        if (attribute in __data.keys()):
            return __data[attribute]

    def get_children(self, os, flavor):
        """Return a list of child images, i.e. dependent images."""
        children = []
        for __flavor in self.data['images'][os]:
            if (__flavor['flavor'] == flavor):
                __data = __flavor
        if ('children' in __data.keys()):
            for child in __data['children']:
                children.append(child)
                children.extend(self.get_children(os, child))
        return children

    def get_parentimage(self, os, flavor):
        """Return the parentimage for a given image."""
        __parentdata = {}
        for __flavor in self.data['images'][os]:
            if (__flavor['flavor'] == flavor):
                __data = __flavor
        if 'parent' in __data.keys():
            parent = __data['parent']
            for __flavor in self.data['images'][os]:
                if (__flavor['flavor'] == parent):
                    __parentdata = __flavor
            if 'base_image' in __parentdata.keys():
                return __parentdata['base_image']
            else:
                return None
        else:
            return None

    def get_parent(self, os, flavor):
        """Return the parent image of an image."""
        for __flavor in self.data['images'][os]:
            if (__flavor['flavor'] == flavor):
                __data = __flavor
        if 'parent' in __data.keys():
            return __data['parent']
        else:
            return None
