# -*- coding: utf-8 -*-

import FreeCAD
from pathlib import Path


def resolve_image_path(suffix = ''):
  project_path = Path(App.ActiveDocument.FileName)
  return project_path.parent.joinpath(
    'export', (str(project_path.stem) + suffix + '.png')
  )

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

def capture_images():
  set_isometric_view()
  focus_view()
  capture_image(resolve_image_path('-isometric'))

  flip_view()
  focus_view()
  capture_image(resolve_image_path('-isometric-flipped'))

  set_isometric_view()
  rotate_view_clockwise()
  focus_view()
  capture_image(resolve_image_path('-isometric-rotated-clockwise'))

  set_isometric_view()
  rotate_view_counterclockwise()
  focus_view()
  capture_image(resolve_image_path('-isometric-rotated-counterclockwise'))

  set_front_view()
  capture_image(resolve_image_path('-front'))

  set_rear_view()
  capture_image(resolve_image_path('-rear'))

  set_left_view()
  capture_image(resolve_image_path('-left'))

  set_right_view()
  capture_image(resolve_image_path('-right'))

  set_top_view()
  capture_image(resolve_image_path('-top'))

  set_bottom_view()
  capture_image(resolve_image_path('-bottom'))

def bootstrap_scene():
  Gui.Selection.clearSelection()

def teardown_scene():
  set_isometric_view()
  focus_view()

def save_project():
  Gui.SendMsgToActiveView('Save')

def main():
  bootstrap_scene()
  capture_images()
  teardown_scene()
  save_project()


main()
