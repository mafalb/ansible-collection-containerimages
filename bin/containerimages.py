#!/bin/python3

if __name__ == '__main__':
    import argparse
    import yaml

    import os
    import sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '../plugins/module_utils/containerimages'))
    import schema

    # Initialize parser
    parser = argparse.ArgumentParser(description='containerimages')

    # Adding optional argument
    parser.add_argument("-f", "--file", help="use file as input", default=sys.stdin)
    parser.add_argument("action")
    parser.add_argument("--os", default=None)
    parser.add_argument("--flavor", default=None)
    parser.add_argument("--json", action='store_true')
    parser.add_argument("--attribute")

    arguments = parser.parse_args()

    images = schema.Containerimages(arguments.file)

    if arguments.action == 'yaml2json':
        images.yaml_to_json()
    elif arguments.action == 'listos' and arguments.json:
        images.list_os(format='json')
    elif arguments.action == 'listos':
        images.list_os()
    elif arguments.action == 'listimages':
        images.list_images(arguments.os)
    elif arguments.action == 'children':
        images.get_children(arguments.os, arguments.flavor)
    elif arguments.action == 'parentimage':
        images.get_parentimage(arguments.os, arguments.flavor)
    elif arguments.action == 'parent':
        images.get_parent(arguments.os, arguments.flavor)
    elif arguments.action == 'attribute':
        images.get_attribute(arguments.os, arguments.flavor, arguments.attribute)
