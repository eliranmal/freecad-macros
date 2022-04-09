# -*- coding: utf-8 -*-

import FreeCAD
from pathlib import Path


def resolve_image_path(suffix = ''):
  project_path = Path(App.ActiveDocument.FileName)
  return project_path.parent.joinpath(
    'export', (str(project_path.stem) + suffix + '.png')
  )

# returns all document objects as a dictionary of lists, grouped by type.
def get_objects_as_dict():
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

def set_objects_visibility(obj_type, visitility):
  sketch_objects = get_objects_by_type(obj_type)
  for obj in sketch_objects:
    obj.ViewObject.Visibility = visitility

def reset_objects_visibility():
  # show all parts and bodies
  set_objects_visibility('App.Part', True)
  set_objects_visibility('PartDesign.Body', True)
  # hide shape binders, axis objects, and sketches
  set_objects_visibility('Part.Feature', False)
  set_objects_visibility('App.GeoFeature', False)
  set_objects_visibility('Sketcher.SketchObject', False)

def focus_view():
  Gui.SendMsgToActiveView('ViewFit')

def set_isometric_view():
  view = Gui.activeDocument().activeView()
  view.viewIsometric()

def set_front_view():
  view = Gui.activeDocument().activeView()
  view.viewFront()

def set_rear_view():
  view = Gui.activeDocument().activeView()
  view.viewRear()

def set_left_view():
  view = Gui.activeDocument().activeView()
  view.viewLeft()

def set_right_view():
  view = Gui.activeDocument().activeView()
  view.viewRight()

def set_top_view():
  view = Gui.activeDocument().activeView()
  view.viewTop()

def set_bottom_view():
  view = Gui.activeDocument().activeView()
  view.viewBottom()

def flip_view():
  view = Gui.activeDocument().activeView()
  cam = view.getCameraNode()
  cam_orientation_tuple = cam.orientation.getValue().getValue()
  cam_orientation_flipped_tuple = (
    cam_orientation_tuple[1], cam_orientation_tuple[0] * -1, cam_orientation_tuple[3] * -1, cam_orientation_tuple[2]
  )
  cam.orientation.setValue(cam_orientation_flipped_tuple)

def rotate_view_clockwise():
  view = Gui.activeDocument().activeView()
  cam = view.getCameraNode()
  cam_orientation_tuple = cam.orientation.getValue().getValue()
  cam_orientation_rotated_clockwise_tuple = (
    cam_orientation_tuple[1], cam_orientation_tuple[0], cam_orientation_tuple[3], cam_orientation_tuple[2]
  )
  cam.orientation.setValue(cam_orientation_rotated_clockwise_tuple)

def rotate_view_counterclockwise():
  view = Gui.activeDocument().activeView()
  cam = view.getCameraNode()
  cam_orientation_tuple = cam.orientation.getValue().getValue()
  cam_orientation_rotated_counterclockwise_tuple = (
    cam_orientation_tuple[0], cam_orientation_tuple[1] * -1, cam_orientation_tuple[2] * -1, cam_orientation_tuple[3]
  )
  cam.orientation.setValue(cam_orientation_rotated_counterclockwise_tuple)

def capture_image(path):
  view = Gui.activeDocument().activeView()
  view.saveImage(
     str(path), 1562, 958, 'Current'
  )

def capture_image_current():
  capture_image(resolve_image_path())

def capture_image_isometric():
  set_isometric_view()
  focus_view()
  capture_image(resolve_image_path('-isometric'))

def capture_image_isometric_flipped():
  set_isometric_view()
  flip_view()
  focus_view()
  capture_image(resolve_image_path('-isometric-flipped'))

def capture_image_isometric_cw():
  set_isometric_view()
  rotate_view_clockwise()
  focus_view()
  capture_image(resolve_image_path('-isometric-rotated-clockwise'))

def capture_image_isometric_ccw():
  set_isometric_view()
  rotate_view_counterclockwise()
  focus_view()
  capture_image(resolve_image_path('-isometric-rotated-counterclockwise'))

def capture_image_front():
  set_front_view()
  capture_image(resolve_image_path('-front'))

def capture_image_rear():
  set_rear_view()
  capture_image(resolve_image_path('-rear'))

def capture_image_left():
  set_left_view()
  capture_image(resolve_image_path('-left'))

def capture_image_right():
  set_right_view()
  capture_image(resolve_image_path('-right'))

def capture_image_top():
  set_top_view()
  capture_image(resolve_image_path('-top'))

def capture_image_bottom():
  set_bottom_view()
  capture_image(resolve_image_path('-bottom'))

def capture_image_all():
  capture_image_isometric()
  capture_image_isometric_flipped()
  capture_image_isometric_cw()
  capture_image_isometric_ccw()
  capture_image_front()
  capture_image_rear()
  capture_image_left()
  capture_image_right()
  capture_image_top()
  capture_image_bottom()

def capture_images():
  view_command_map[view]()

def bootstrap_scene():
  Gui.Selection.clearSelection()
  reset_objects_visibility()

def teardown_scene():
  set_isometric_view()
  focus_view()

def save_project():
  Gui.SendMsgToActiveView('Save')

def prepare_env():
  global view, view_command_map
  view = 'current'
  view_command_map = {
    'left': capture_image_left,
    'right': capture_image_right,
    'top': capture_image_top,
    'bottom': capture_image_bottom,
    'front': capture_image_front,
    'rear': capture_image_rear,
    'iso': capture_image_isometric,
    'iso-flipped': capture_image_isometric_flipped,
    'iso-cw': capture_image_isometric_cw,
    'iso-ccw': capture_image_isometric_ccw,
    'all': capture_image_all,
    'current': capture_image_current,
  }
  comment = FreeCAD.ActiveDocument.Comment

  if comment and comment in view_command_map:
    view = comment

  FreeCAD.ActiveDocument.Comment = ''

def main():
  prepare_env()
  bootstrap_scene()
  capture_images()
  teardown_scene()
  save_project()


main()
