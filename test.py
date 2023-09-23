import maya.cmds as cmds
import maya.standalone


maya.standalone.initialize()

file_to_render = "%USERPROFILE%\\Desktop\\maya\\rendertest\\test.ma"     # "Browse" button
cmds.file(file_to_render, o = True)   # "Browse button"

import mtoa.utils as mutils
mutils.createLocator("aiSkyDomeLight", asLight=True)

cmds.file(s = True)   # "Browse button"

maya.standalone.uninitialize()
