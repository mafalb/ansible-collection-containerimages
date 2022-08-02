import sys
import yaml
import json

data = yaml.load(sys.stdin, Loader=yaml.Loader)

json.dump(data, sys.stdout)
