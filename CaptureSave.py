# -*- coding: utf-8 -*-

from pathlib import Path
import FreeCAD

project_path = Path(App.ActiveDocument.FileName)
image_path = project_path.parent.joinpath(
  "export", (str(project_path.stem) + '.png')
)

Gui.activeDocument().activeView().viewIsometric()
Gui.SendMsgToActiveView("ViewFit")
Gui.runCommand("Std_ViewZoomOut", 0)
Gui.activeDocument().activeView().saveImage(
   str(image_path), 1562, 958, "Current"
)
Gui.SendMsgToActiveView("Save")
