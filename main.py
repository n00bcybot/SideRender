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

# Set MtoA path. Loading the plugin guaranties initialization
mtoa_path = "C:\Program Files\Autodesk\Arnold\maya2024\plug-ins\mtoa.mll"

# Set the Maya project to use the user documents folder for preferences
cmds.workspace(prefs_folder, openWorkspace=True)

# Load the MtoA plugin
cmds.loadPlugin(mtoa_path)

file_to_render = "%USERPROFILE%\\Desktop\\maya\\rendertest\\test.ma"     # "Browse" button
cmds.file(file_to_render, o=True)   # "Browse button"

# Options -------------------------------------------------------------------------------------------------------------
# Set file name
cmds.setAttr("defaultRenderGlobals.imageFilePrefix", "C:\\Users\\fresh\\Desktop\\maya\\rendertest\\render\\hhh",
             type="string")

# Skip license check. It reduces rendering time, useful for quick preview rendering
cmds.setAttr("defaultArnoldRenderOptions.skipLicenseCheck", 1)

camera_name = "persp"   # Dropdown. Get list from scene

# Rendering -----------------------------------------------------------------------------------------------------------
# Create list of processes and start them. Number of processes depends on the should depend on the number of cores
# and how many cores should be left out for other applications; dropdown

processes = []
if __name__ == '__main__':

    for i in range(step):
        process = multiprocessing.Process(target=startRender, args=(start_frame + i, end_frame, step))
        processes.append(process)

    for process in processes:
        process.start()

# ---------------------------------------------------------------------------------------------------------------------

maya.standalone.uninitialize()