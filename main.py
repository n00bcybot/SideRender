import os
import maya.standalone
import multiprocessing

def startRender(start, end, by_step):
    for number in range(start, end + 1, by_step):
        cmds.arnoldRender(cam=camera_name, seq=number)

start_frame = 10    # Textbox eventually
end_frame = 40      # Textbox eventually
step = 4   # Number of processors to create a step. This should only be included when multiprocessing. Dropdown perhaps

maya.standalone.initialize()
import maya.cmds as cmds

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
# Set file name
cmds.setAttr("defaultRenderGlobals.imageFilePrefix", "C:\\Users\\fresh\\Desktop\\maya\\rendertest\\render\\hhh", type="string")

# Skip license check. It reduces rendering time, useful for quick preview rendering
cmds.setAttr("defaultArnoldRenderOptions.skipLicenseCheck", 1)

camera_name = "persp"   # Dropdown. Get list from scene
# ---------------------------------------------------------------------------------------------------------------------

processes = []
if __name__ == '__main__':

    for i in range(4):
        process = multiprocessing.Process(target=startRender, args=(start_frame + i, end_frame, step))
        processes.append(process)

    for process in processes:
        process.start()
