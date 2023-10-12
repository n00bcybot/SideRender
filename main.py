import os
import sys
import maya.cmds as cmds
import maya.standalone
import multiprocessing




# def startRender(start, end, by_step):
#     for number in range(start, end + 1, by_step):
#         cmds.arnoldRender(cam=camera_name, seq=number)
#
# start_frame = 20    # Textbox eventually
# end_frame = 40      # Textbox eventually
# step = 4   # Number of processors to create a step. This should only be included when multiprocessing. Dropdown perhaps
#
#
# maya.standalone.initialize()
# import maya.cmds as cmds
#
# # Set preferences folder
# prefs_folder = os.path.expanduser("~\\Documents\\maya\\2024\\prefs")
#
# # Set MtoA path. Loading the plugin guaranties initialization
# mtoa_path = "C:\Program Files\Autodesk\Arnold\maya2024\plug-ins\mtoa.mll"
#
# # Set the Maya project to use the user documents folder for preferences
# cmds.workspace(prefs_folder, openWorkspace=True)
#
# # Load the MtoA plugin
# cmds.loadPlugin(mtoa_path)
#
# file_to_render = "%USERPROFILE%\\Desktop\\maya\\arctic\\arctic.ma"  # "Browse" button
# cmds.file(file_to_render, o=True)  # "Browse button"
#
# # Options -------------------------------------------------------------------------------------------------------------
# # Set file name
# render_folder = "C:\\Users\\fresh\\Desktop\\maya\\arctic\\render\\"
# file_name = 'hhh'
#
# cmds.setAttr("defaultRenderGlobals.imageFilePrefix", render_folder + file_name, type="string")
#
# # # Skip license check. It reduces rendering time, useful for quick preview rendering
# # cmds.setAttr("defaultArnoldRenderOptions.skipLicenseCheck", 1)
#
# camera_name = "persp"  # Dropdown. Get list from scene
#
# # Rendering -----------------------------------------------------------------------------------------------------------
# # Create list of processes and start them. Number of processes depends on the should depend on the number of cores
# # and how many cores should be left out for other applications; dropdown
#
# if __name__ == '__main__':
#     processes = []
#     for i in range(step):
#         process = multiprocessing.Process(target=startRender, args=(start_frame + i, end_frame, step))
#         processes.append(process)
#
#     for process in processes:
#         process.start()
#
# # ---------------------------------------------------------------------------------------------------------------------

# param1 = sys.argv[1]  # Start frame
# param2 = sys.argv[2]  # End frame
# param3 = sys.argv[3]  # Number of cores
# param4 = sys.argv[4]  # File path
# param5 = sys.argv[5]  # Folder path
# param6 = sys.argv[6]  # File name
# param7 = sys.argv[7]  # Camera name
# param8 = sys.argv[8]  # Render type


class RenderLogic:

    def __int__(self, start_frame, end_frame, step, file_to_render, render_folder, frame_name, camera_name, render_type):

        self.start_frame = start_frame
        self.end_frame = end_frame
        self.step = step
        self.file_to_render = file_to_render
        self.render_folder = render_folder
        self.frame_name = frame_name
        self.camera_name = camera_name
        self.render_type = render_type



    def startSequenceRender(self, start, end):
        for number in range(start, end + 1):
            cmds.arnoldRender(cam=self.camera_name, seq=number)

    def startMultiRender(self, start, end, step):
        for number in range(start, end + 1, step):
            cmds.arnoldRender(cam=self.camera_name, seq=number)

    def multiRender(self):

        if __name__ == "__main__":
            processes = []
            for i in range(self.step):
                process = multiprocessing.Process(target=self.startMultiRender,
                                                  args=(self.start_frame + i, self.end_frame, self.step))
                processes.append(process)
            for process in processes:
                process.start()

    def sequenceRender(self):
        self.startSequenceRender(self.start_frame, self.end_frame)

    @staticmethod
    def skiplicenseCheck(skip=True):
        if skip:
            cmds.setAttr("defaultArnoldRenderOptions.skipLicenseCheck", 1)

    def startRender(self):
        maya.standalone.initialize()
        import maya.cmds as cmds

        prefs_folder = os.path.expanduser("~\\Documents\\maya\\2024\\prefs")
        cmds.workspace(prefs_folder, openWorkspace=True)
        mtoa_path = "C:\Program Files\Autodesk\Arnold\maya2024\plug-ins\mtoa.mll"
        cmds.loadPlugin(mtoa_path)

        cmds.file(self.file_to_render, o=True)
        cmds.setAttr("defaultRenderGlobals.imageFilePrefix", (self.render_folder + '/' + self.frame_name),
                     type="string")
        self.skiplicenseCheck(skip=True)

        if self.render_type == "Multiprocess":
            cmds.setAttr("defaultArnoldRenderOptions.threads_autodetect", 0)
            cmds.setAttr("defaultArnoldRenderOptions.threads", self.step)
            self.multiRender()
        elif self.render_type == "Sequence":
            self.sequenceRender()

        # cmds.quit()

# # ----------------------------------------------------------------------------------------------------------------
# render = RenderLogic()
# render.start_frame = int(param1)
# render.end_frame = int(param2)
# render.step = int(param3)
# render.file_to_render = param4
# render.render_folder = param5
# render.frame_name = param6
# render.camera_name = param7
#
#
