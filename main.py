import maya.cmds as cmds
import maya.standalone


maya.standalone.initialize()

file_to_render = "%USERPROFILE%\\Desktop\\maya\\rendertest\\test.ma"     # "Browse" button
cmds.file(file_to_render, o = True)   # "Browse button"

play_end = cmds.playbackOptions(q=True, maxTime=True)
play_start = cmds.playbackOptions(q=True, minTime=True)

camera_name = "persp"   # Dropdown. Get list from scene
start_frame = 30    # Textbox eventually
end_frame = 40      # Textbox eventually
step = 2    # Nuber of processors to create a step. This should only be included when multiprocessing. Dropdown perhaps

for number in range(start_frame, end_frame + 1, step):
    cmds.arnoldRender(cam=camera_name, seq=number)

maya.standalone.uninitialize()

# sfsdfsfsdfdsf
