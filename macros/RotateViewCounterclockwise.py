# -*- coding: utf-8 -*-

import FreeCAD


def rotate_view_counterclockwise():
  view = Gui.activeDocument().activeView()
  cam = view.getCameraNode()
  cam_orientation_tuple = cam.orientation.getValue().getValue()
  cam_orientation_rotated_counterclockwise_tuple = (
    cam_orientation_tuple[0], cam_orientation_tuple[1] * -1, cam_orientation_tuple[2] * -1, cam_orientation_tuple[3]
  )
  cam.orientation.setValue(cam_orientation_rotated_counterclockwise_tuple)

def main():
  rotate_view_counterclockwise()
  focus_view()


main()
