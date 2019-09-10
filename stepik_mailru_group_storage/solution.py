# -*- coding: UTF-8 -*-
import os
import argparse
import tempfile
import json

parser = argparse.ArgumentParser()
parser.add_argument("--key")
parser.add_argument("--val", nargs="*")

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
args = parser.parse_args()
try:
    with open(storage_path, 'r') as f:
        data = f.read()
        if len(data) > 0: data = json.loads(data)
        else: data = dict()
except IOError:
    with open(storage_path, "w") as f:
        data = dict()

if args.val:
    if args.key in data:
        data.update({args.key: data.get(args.key) + args.val})
    else:
        data.update({args.key: args.val })
    with open(storage_path, "w") as f:
        f.write(json.dumps(data))
else:
    if args.key in data:
        print(", ".join(data.get(args.key)))
    else:
        print("None")
