# -*- coding: utf-8 -*-

import FreeCAD
from pathlib import Path


def resolve_image_path(suffix = ''):
  project_path = Path(App.ActiveDocument.FileName)
  return project_path.parent.joinpath(
    "export", (str(project_path.stem) + suffix + '.png')
  )

def focus_view():
  Gui.SendMsgToActiveView("ViewFit")
  Gui.runCommand("Std_ViewZoomOut", 0)

def set_isometric_view():
  view = Gui.activeDocument().activeView()
  view.viewIsometric()

def capture_image(path):
  view = Gui.activeDocument().activeView()
  view.saveImage(
     str(path), 1562, 958, "Current"
  )

def save_project():
  Gui.SendMsgToActiveView("Save")

def flip_view():
  view = Gui.activeDocument().activeView()
  cam = view.getCameraNode()
  cam_orientation_tuple = cam.orientation.getValue().getValue()
  cam_orientation_flipped_tuple = (
    cam_orientation_tuple[1], cam_orientation_tuple[0] * -1, cam_orientation_tuple[3] * -1, cam_orientation_tuple[2]
  )
  cam.orientation.setValue(cam_orientation_flipped_tuple)

def main():
  set_isometric_view()
  focus_view()
  capture_image(resolve_image_path('-isometric'))

  flip_view()
  focus_view()
  capture_image(resolve_image_path('-isometric-flipped'))

  set_isometric_view()
  focus_view()

  save_project()


main()
