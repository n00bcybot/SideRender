import maya.standalone

maya.standalone.initialize()
import maya.cmds as cmds
import mtoa.utils as mutils

file_to_render = "%USERPROFILE%\\Desktop\\maya\\rendertest\\test.ma"  # "Browse" button
cmds.file(file_to_render, o=True)  # "Browse button"

cmds.camera(name="asfda")

cmds.SaveScene()
cmds.quit()
maya.standalone.uninitialize()

