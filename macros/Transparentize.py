# -*- coding: utf-8 -*-

import os
# import sys
import json
import FreeCAD
from pathlib import Path
from json.decoder import JSONDecodeError
from example_package import example

# sys.path.append('/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages')
# sys.path.pop()

import site
from importlib import reload
reload(site)

def get_objects_as_dict():
  """
  returns all document objects as a dictionary of lists, grouped by type.
  """
  obj_dict = dict()
  for obj in FreeCAD.ActiveDocument.Objects:
    # this extracts the term between the single quotes in the object type string
    obj_type = str(type(obj)).partition("'")[2].partition("'")[0]
    obj_dict[obj_type] = obj_dict.get(obj_type, [])
    obj_dict[obj_type].append(obj)
  return obj_dict

def get_objects_by_label(label):
  return App.ActiveDocument.getObjectsByLabel(label)

def get_objects_by_type(obj_type):
  obj_dict = get_objects_as_dict()
  return obj_dict.get(obj_type, [])

def set_objects_transparency(obj_type, percentage):
  sketch_objects = get_objects_by_type(obj_type)
  for obj in sketch_objects:
    obj.ViewObject.Transparency = percentage

def set_bodies_transparency(percentage):
  set_objects_transparency('PartDesign.Body', percentage)

def set_transparency():
  if transparency:
    set_bodies_transparency(int(transparency))

def prepare_env():
  global transparency
  transparency = FreeCAD.ActiveDocument.Comment

def main():
  print('wat')
  print(example.add_one(3))
  return 0
  prepare_env()
  set_transparency()


main()
