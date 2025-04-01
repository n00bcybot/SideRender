import multiprocessing
import maya.cmds as cmds
import maya.standalone
import os
import sys

file_to_render = "C:\\Users\\fresh\\Desktop\\render\\test.ma"
render_folder = "C:\\Users\\fresh\\Desktop\\render\\render"
frame_name = "test"
camera_name = "persp"
start_frame = 1
end_frame = 6

maya.standalone.initialize()

import maya.cmds as cmds

prefs_folder = os.path.expanduser("~\\Documents\\maya\\2025\\prefs")
cmds.workspace(prefs_folder, openWorkspace=True)
mtoa_path = "C:\Program Files\Autodesk\Arnold\maya2025\plug-ins\mtoa.mll"
cmds.loadPlugin(mtoa_path)

cmds.file(file_to_render, o=True)
cmds.setAttr("defaultRenderGlobals.imageFilePrefix", (render_folder + '/' + frame_name),
             type="string")
# cmds.setAttr("defaultArnoldRenderOptions.skipLicenseCheck", 1)
for number in range(start_frame, end_frame + 1):
    cmds.arnoldRender(cam=camera_name, seq = number)
