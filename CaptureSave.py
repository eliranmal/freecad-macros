# -*- coding: utf-8 -*-

from pathlib import Path
import FreeCAD


def resolve_image_path(suffix = ''):
  project_path = Path(App.ActiveDocument.FileName)
  return project_path.parent.joinpath(
    "export", (str(project_path.stem) + suffix + '.png')
  )

def prepare_view(view):
  view.viewIsometric()
  Gui.SendMsgToActiveView("ViewFit")
  Gui.runCommand("Std_ViewZoomOut", 0)

def capture_image(view, path):
  view.saveImage(
     str(path), 1562, 958, "Current"
  )

def save_project():
  Gui.SendMsgToActiveView("Save")


active_view = Gui.activeDocument().activeView()
image_path = resolve_image_path()

prepare_view(active_view)
capture_image(active_view, image_path)

save_project()
