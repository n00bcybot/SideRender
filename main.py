import os
import maya.standalone

maya.standalone.initialize()
import maya.cmds as cmds
import mtoa.utils as mutils

# Set preferences folder
prefs_folder = os.path.expanduser("~\\Documents\\maya\\2024\\prefs")

# Set MtoA path
plugin_path = "C:\Program Files\Autodesk\Arnold\maya2024\plug-ins\mtoa.mll"

# Set the Maya project to use the user documents folder for preferences
cmds.workspace(prefs_folder, openWorkspace=True)

# Load the MtoA plugin
try:
    cmds.loadPlugin(plugin_path)
    print("MtoA plugin loaded successfully.")
except Exception as e:
    print("Error loading MtoA plugin:", str(e))

file_to_render = "%USERPROFILE%\\Desktop\\maya\\rendertest\\test.ma"     # "Browse" button
cmds.file(file_to_render, o=True)   # "Browse button"

# ---------------------------------------------------------------------------------------------------------------------

cmds.setAttr("defaultRenderGlobals.imageFilePrefix", "C:\\Users\\fresh\\Desktop\\maya\\rendertest\\render\\hhh", type = "string")
cmds.setAttr("defaultArnoldRenderOptions.skipLicenseCheck", 1)  # Skip license check. It reduces rendering time

play_end = cmds.playbackOptions(q=True, maxTime=True)   # Returns integer (the frame number)
play_start = cmds.playbackOptions(q=True, minTime=True)

camera_name = "persp"   # Dropdown. Get list from scene
start_frame = 30    # Textbox eventually
end_frame = 40      # Textbox eventually
step = 2   # Number of processors to create a step. This should only be included when multiprocessing. Dropdown perhaps

for number in range(start_frame, end_frame + 1, step):
    cmds.arnoldRender(cam=camera_name, seq=number)

# ---------------------------------------------------------------------------------------------------------------------

# Save file
cmds.file(save=True, type="mayaAscii")

# Quit
cmds.quit()
maya.standalone.uninitialize()

