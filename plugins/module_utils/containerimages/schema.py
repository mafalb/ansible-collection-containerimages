#!/bin/python3

import yaml
import json
import sys


class Containerimages:

    def __init__(self, datafile=None):
        if datafile:
            datafile = open(datafile, 'r')
        self.data = yaml.load(datafile, Loader=yaml.Loader)
        if datafile:
            datafile.close()

    def yaml_to_json(self):
        """Return json."""
        json.dump(self, sys.stdout)

    def list_os(self, format='text'):
        """Print Operating Systems."""
        if format == 'json':
            json.dump(list(self.data["images"].keys()), sys.stdout)
        else:
            for os in self.data["images"].keys():
                print(os)

    def list_images(self, os):
        """Print a list of images for a given Operating System."""
        for image in self.data["images"][os]:
            print(image['flavor'])

    def get_attribute(self, os, flavor, attribute):
        """Print a attribute for a given image."""
        for __flavor in self.data['images'][os]:
            if (__flavor['flavor'] == flavor):
                __data = __flavor
        if (attribute in __data.keys()):
            print(__data[attribute])

    def get_children(self, os, flavor):
        """Print all images that the given image is a dependency for."""
        children = self.__get_children(os, flavor)
        for child in children:
            print(child)

    def __get_children(self, os, flavor):
        """Helper function for get_children()."""
        children = []
        for __flavor in self.data['images'][os]:
            if (__flavor['flavor'] == flavor):
                __data = __flavor
        if ('children' in __data.keys()):
            for child in __data['children']:
                children.append(child)
                children.extend(self.__get_children(os, child))
        return children

    def get_parentimage(self, os, flavor):
        """Print the parentimage for a given image."""
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
                parentimage = __parentdata['base_image']
                print(parentimage)
            else:
                print("None")
        else:
            print("None")

    def get_parent(self, os, flavor):
        """Print the parent image of an image."""
        for __flavor in self.data['images'][os]:
            if (__flavor['flavor'] == flavor):
                __data = __flavor
        if 'parent' in __data.keys():
            print(__data['parent'])
        else:
            print('None')
