#!/bin/python3

def yaml_to_json():
    json.dump(data, sys.stdout)

def list_os():
    if arguments.json:
        json.dump(list(data["images"].keys()), sys.stdout)
    else:
        for os in data["images"].keys():
            print(os)

def get_children(os, flavor):
    children = __get_children(os, flavor)
    for child in children:
        print(child)

def __get_children(os, flavor):
    children = []
    for __flavor in data['images'][os]:
        if (__flavor['flavor'] == flavor):
            __data = __flavor
    if ('children' in __data.keys()):
        for child in __data['children']:
            children.append(child)
            bla=__get_children(os, child)
            children.extend(__get_children(os, child))
    return children

def get_parentimage(os, flavor):
    __parentdata = {}
    for __flavor in data['images'][os]:
        if (__flavor['flavor'] == flavor):
            __data = __flavor
    if 'parent' in __data.keys():
        parent = __data['parent']
        for __flavor in data['images'][os]:
            if (__flavor['flavor'] == parent):
                __parentdata = __flavor
        if 'base_image' in __parentdata.keys():
            parentimage = __parentdata['base_image']
            print(parentimage)
        else:
            print("None")
    else:
        print("None")

def get_parent(os, flavor):
    for __flavor in data['images'][os]:
        if (__flavor['flavor'] == flavor):
            __data = __flavor
    if 'parent' in __data.keys():
        print(__data['parent'])
    else:
        print('None')
    
#    data=data['images'][os]
#    print(data['images'][os][flavor]['children'])
#    if (data['images'][os][flavor]['children']):
#        children = data['images'][os][flavor]['children']

#    print(children)
    
if __name__ == '__main__':
    import sys
    import yaml
    import json
    import argparse

    # Initialize parser
    parser = argparse.ArgumentParser(description = 'containerimages')

    # Adding optional argument
    parser.add_argument("-f", "--file", help = "use file as input", default = sys.stdin)
    parser.add_argument("action")
    parser.add_argument("--os", default=None)
    parser.add_argument("--flavor", default=None)
    parser.add_argument("--json", action='store_true')

    arguments=parser.parse_args()
#    print(arguments)

    data = yaml.load(arguments.file, Loader=yaml.Loader)

    if arguments.action == 'yaml2json':
        yaml_to_json()
    elif arguments.action =='listos':
        list_os()
    elif arguments.action =='children':
        get_children(arguments.os, arguments.flavor)
    elif arguments.action =='parentimage':
        get_parentimage(arguments.os, arguments.flavor)
    elif arguments.action == 'parent':
        get_parent(arguments.os, arguments.flavor)
