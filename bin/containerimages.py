#!/usr/bin/env python

if __name__ == '__main__':
    import argparse

    import os as os_module
    import sys
    sys.path.append(os_module.path.join(os_module.path.dirname(__file__), '../plugins/module_utils/containerimages'))
    import schema

    # Initialize parser
    parser = argparse.ArgumentParser(description='containerimages')

    # Adding optional argument
    parser.add_argument("-f", "--file", help="use file as input", default=None)
    parser.add_argument("action")
    parser.add_argument("--os", default=None)
    parser.add_argument("--flavor", default=None)
    parser.add_argument("--json", action='store_true')
    parser.add_argument("--attribute")

    arguments = parser.parse_args()
    images = schema.Containerimages(arguments.file)

    if arguments.action == 'yaml2json':
        print(images.yaml_to_json(images))
    elif arguments.action == 'listos' and arguments.json:
        print(images.list_os())
    elif arguments.action == 'listos' and not arguments.json:
        oses = images.list_os()
        for os in oses:
            print(os)
    elif arguments.action == 'listimages':
        imagelist = images.list_images(arguments.os)
        for image in imagelist:
            print(image)
    elif arguments.action == 'children':
        for child in images.get_children(arguments.os, arguments.flavor):
            print(child)
    elif arguments.action == 'parentimage':
        print(images.get_parentimage(arguments.os, arguments.flavor))
    elif arguments.action == 'parent':
        print(images.get_parent(arguments.os, arguments.flavor))
    elif arguments.action == 'attribute':
        print(images.get_attribute(arguments.os, arguments.flavor, arguments.attribute))
