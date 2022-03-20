# -*- coding: utf-8 -*-

import FreeCAD


def rotate_view_clockwise():
  view = Gui.activeDocument().activeView()
  cam = view.getCameraNode()
  cam_orientation_tuple = cam.orientation.getValue().getValue()
  cam_orientation_rotated_clockwise_tuple = (
    cam_orientation_tuple[1], cam_orientation_tuple[0], cam_orientation_tuple[3], cam_orientation_tuple[2]
  )
  cam.orientation.setValue(cam_orientation_rotated_clockwise_tuple)

def main():
  rotate_view_clockwise()
  focus_view()


main()
