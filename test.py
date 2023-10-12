import os
import sys
import maya.cmds as cmds
import maya.standalone
import multiprocessing


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



    # def startSequenceRender(self, start, end):
    #     for number in range(start, end + 1):
    #         cmds.arnoldRender(cam=self.camera_name, seq=number)

    # def startMultiRender(self, start, end, step):


    # def multiRender(self):
    #
    #     if __name__ == "__main__":
    #         processes = []
    #         for i in range(self.step):
    #             process = multiprocessing.Process(target=self.startMultiRender,
    #                                               args=(self.start_frame + i, self.end_frame, self.step))
    #             processes.append(process)
    #         for process in processes:
    #             process.start()
    #
    # def sequenceRender(self):
    #     self.startSequenceRender(self.start_frame, self.end_frame)
    #
    @staticmethod
    def skiplicenseCheck(skip=True):
        if skip:
            cmds.setAttr("defaultArnoldRenderOptions.skipLicenseCheck", 1)
    def startMultiRender(self):
        for number in range(self.start_frame, self.end_frame + 1, self.step):
            cmds.arnoldRender(cam=self.camera_name, seq=number)
    def startRender(self):
        maya.standalone.initialize()
        import maya.cmds as cmds

        prefs_folder = os.path.expanduser("~\\Documents\\maya\\2024\\prefs")
        cmds.workspace(prefs_folder, openWorkspace=True)
        # mtoa_path = "C:\Program Files\Autodesk\Arnold\maya2024\plug-ins\mtoa.mll"
        # cmds.loadPlugin(mtoa_path)

        cmds.file(self.file_to_render, o=True)
        cmds.setAttr("defaultRenderGlobals.imageFilePrefix", (self.render_folder + '/' + self.frame_name),
                     type="string")
        self.skiplicenseCheck(skip=True)

        self.startMultiRender()

        cmds.file(new=True, force=True)