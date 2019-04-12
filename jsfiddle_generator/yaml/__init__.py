#!/usr/bin/env python
import os
import public
import yaml


@public.add
def load(path):
    """return a dictorinary with yaml data"""
    if not os.path.exists(path):
        return {}
    with open(path, 'r') as stream:
        return yaml.load(stream)


@public.add
def save(path, data):
    """save a dictionary to a yaml file"""
    if "resources" in data and not data.get("resources", []):
        del data["resources"]
    with open(path, 'w') as outfile:
        yaml.dump(data, outfile, default_flow_style=False)
