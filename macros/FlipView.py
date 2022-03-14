# -*- coding: utf-8 -*-

import FreeCAD


def focus_view():
  Gui.SendMsgToActiveView('ViewFit')
  Gui.runCommand('Std_ViewZoomOut', 0)

def flip_view():
  view = Gui.activeDocument().activeView()
  cam = view.getCameraNode()
  cam_orientation_tuple = cam.orientation.getValue().getValue()
  cam_orientation_flipped_tuple = (
    cam_orientation_tuple[1], cam_orientation_tuple[0] * -1, cam_orientation_tuple[3] * -1, cam_orientation_tuple[2]
  )
  cam.orientation.setValue(cam_orientation_flipped_tuple)

def main():
  flip_view()
  focus_view()


main()
