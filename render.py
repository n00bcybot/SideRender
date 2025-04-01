import multiprocessing
import maya.cmds as cmds
import maya.standalone
import os
import sys
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QWidget, QGridLayout, QPushButton, QLineEdit,
                               QFileDialog, QComboBox)
from PySide6.QtGui import QFont, QIcon

sys.path.append('C:\\Program Files\\Autodesk\\Arnold\\maya2025\\scripts')


class RenderLogic:

    def __init__(self, start_frame, end_frame, step, file_to_render, render_folder, frame_name, camera_name,
                 render_type):

        self.start_frame = start_frame
        self.end_frame = end_frame
        self.step = step
        self.file_to_render = file_to_render
        self.render_folder = render_folder
        self.frame_name = frame_name
        self.camera_name = camera_name
        self.render_type = render_type

    @staticmethod
    def skiplicenseCheck(skip=True):
        if skip:
            cmds.setAttr("defaultArnoldRenderOptions.skipLicenseCheck", 1)

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
        #self.skiplicenseCheck(skip=True)

        if self.render_type == "Multiprocess":
            for number in range(self.start_frame, self.end_frame + 1, self.step):
                cmds.arnoldRender(cam=self.camera_name, seq=number)

        elif self.render_type == "Sequence":
            for number in range(self.start_frame, self.end_frame + 1):
                cmds.arnoldRender(cam=self.camera_name, seq=number)
        # maya.standalone.uninitialize()
        cmds.file(new=True, force=True)


# The RenderLogic class must be instantiated outside the GUI to avoid pickling problems. It also needs to be instantiated
# in a function, for the multiprocessing to work.
def render(start, end, step, file_to_render, render_folder, frame_name, camera_name,
           render_type):
    render = RenderLogic(
        start_frame=start,
        end_frame=end,
        step=step,
        file_to_render=file_to_render,
        render_folder=render_folder,
        frame_name=frame_name,
        camera_name=camera_name,
        render_type=render_type
    )
    render.startRender()


if __name__ == "__main__":
    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__(parent=None)

            # Set window icon. An instance of the QIcon object that contains the path to the ico file needs to be created first
            self.icon = QIcon(
                "C:\\Users\\fresh\\Desktop\\truemax\\semester4\\powershell\\renderScript\\interface\\favicon.ico")

            self.font_tuka = QFont()
            self.font_tuka.setPointSize(10)
            self.font_tuka.setFamily("Tuka")

            # Set window size, maximum and minimum size
            # -----------------------------------------------------------------------------------------------------------
            self.setWindowTitle("Side Render")
            # self.setGeometry(400, 400, 400, 400)
            # self.setMaximumSize(800, 400)
            # self.setMinimumSize(300, 100)
            self.setWindowIcon(self.icon)

            # Label select file
            # -----------------------------------------------------------------------------------------------------------
            self.label_select_file = QLabel(self)
            self.label_select_file.setText("Select file")
            self.label_select_file.setBaseSize(100, 50)
            self.label_select_file.setFont(self.font_tuka)
            self.label_select_file.setToolTip("Select file to render")

            # Label select folder
            # -----------------------------------------------------------------------------------------------------------
            self.label_select_folder = QLabel(self)
            self.label_select_folder.setText("Select folder")
            self.label_select_folder.setBaseSize(100, 50)
            self.label_select_folder.setFont(self.font_tuka)
            self.label_select_folder.setToolTip("Select folder to contain the rendered files")

            # Label start frame
            # -----------------------------------------------------------------------------------------------------------
            self.label_start_frame = QLabel(self)
            self.label_start_frame.setText("Start Frame")
            self.label_start_frame.setBaseSize(100, 50)
            self.label_start_frame.setFont(self.font_tuka)
            self.label_start_frame.setToolTip("Enter frame number to start rendering from")

            # Label end frame
            # -----------------------------------------------------------------------------------------------------------
            self.label_end_frame = QLabel(self)
            self.label_end_frame.setText("End Frame")
            self.label_end_frame.setBaseSize(100, 50)
            self.label_end_frame.setFont(self.font_tuka)
            self.label_end_frame.setToolTip("Enter the last frame number to render")

            # Label file name
            # -----------------------------------------------------------------------------------------------------------
            self.label_file_name = QLabel(self)
            self.label_file_name.setText("Output name")
            self.label_file_name.setBaseSize(100, 50)
            self.label_file_name.setFont(self.font_tuka)
            self.label_file_name.setToolTip("Set file name")

            # Label dropbox camera
            # -----------------------------------------------------------------------------------------------------------
            self.label_dropbox_camera = QLabel(self)
            self.label_dropbox_camera.setText("Select camera")
            self.label_dropbox_camera.setBaseSize(100, 50)
            self.label_dropbox_camera.setFont(self.font_tuka)
            self.label_dropbox_camera.setToolTip("Select Camera")

            # Label render type
            # -----------------------------------------------------------------------------------------------------------
            self.label_render_type = QLabel(self)
            self.label_render_type.setText("Render type")
            self.label_render_type.setBaseSize(100, 50)
            self.label_render_type.setFont(self.font_tuka)
            self.label_render_type.setToolTip("Select render type")

            # Label use cores
            # -----------------------------------------------------------------------------------------------------------
            self.label_use_cores = QLabel(self)
            self.label_use_cores.setText("Utilize cores")
            self.label_use_cores.setBaseSize(100, 50)
            self.label_use_cores.setFont(self.font_tuka)
            self.label_use_cores.setToolTip("Select number of cores to utilize")

            # File path textbox
            # --------------------------------------------------------------------
            self.textbox_file_path = QLineEdit()
            self.textbox_file_path.setMaximumWidth(300)
            self.textbox_file_path.setMinimumSize(200, 23)
            self.textbox_file_path.textChanged.connect(self.getCamerasList)

            # Folder path textbox
            # --------------------------------------------------------------------
            self.textbox_folder_path = QLineEdit()
            self.textbox_folder_path.setMaximumWidth(300)
            self.textbox_folder_path.setMinimumSize(200, 23)

            # Start frame textbox
            # --------------------------------------------------------------------
            self.textbox_start_frame = QLineEdit()
            self.textbox_start_frame.setMaximumWidth(300)
            self.textbox_start_frame.setMinimumSize(50, 23)

            # End frame textbox
            # --------------------------------------------------------------------
            self.textbox_end_frame = QLineEdit()
            self.textbox_end_frame.setMaximumWidth(300)
            self.textbox_end_frame.setMinimumSize(50, 23)

            # Output file name textbox
            # --------------------------------------------------------------------
            self.textbox_file_name = QLineEdit()
            self.textbox_file_name.setMaximumWidth(300)
            self.textbox_file_name.setMinimumSize(50, 23)

            # Browse file button
            # --------------------------------------------------------------------
            self.button_browse_file = QPushButton()
            self.button_browse_file.setText('Browse')
            self.button_browse_file.setCheckable(False)
            self.button_browse_file.clicked.connect(self.getFilePath)

            # Select folder button
            # --------------------------------------------------------------------
            self.button_select_folder = QPushButton()
            self.button_select_folder.setText('Browse')
            self.button_select_folder.setCheckable(False)
            self.button_select_folder.clicked.connect(self.getFolderPath)

            # START BUTTON
            # --------------------------------------------------------------------
            self.button_start = QPushButton()
            self.button_start.setText('START')
            self.button_start.setCheckable(False)
            self.button_start.clicked.connect(self.startRender)

            # Browse file dialog
            # --------------------------------------------------------------------
            self.file_dialog_browse_file = QFileDialog(self)
            self.file_dialog_browse_file.setFileMode(QFileDialog.ExistingFiles)
            self.file_dialog_browse_file.setNameFilter("Maya files (*.ma *.mb)")
            self.file_dialog_browse_file.selectNameFilter("Maya files (*.ma *.mb)")

            # Select folder dialog
            # --------------------------------------------------------------------
            self.file_dialog_select_folder = QFileDialog(self)
            self.file_dialog_select_folder.setFileMode(QFileDialog.DirectoryOnly)

            # Select camera
            # --------------------------------------------------------------------
            self.dropbox_camera = QComboBox(self)

            # Select render type
            # --------------------------------------------------------------------
            self.dropbox_render_type = QComboBox(self)
            self.dropbox_render_type.addItem("Multiprocess")
            self.dropbox_render_type.addItem("Sequence")

            # Select number of cores
            # --------------------------------------------------------------------
            self.dropbox_cores = QComboBox(self)
            self.dropbox_cores.addItems(self.getCoreCount())

            # Create grid style main layout
            # -----------------------------------------------------------------------------------------------------------
            self.main_layout = QGridLayout()
            self.main_layout.addWidget(self.label_select_file, 0, 0)
            self.main_layout.addWidget(self.textbox_file_path, 0, 1)
            self.main_layout.addWidget(self.button_browse_file, 0, 2)
            self.main_layout.addWidget(self.label_select_folder, 1, 0)
            self.main_layout.addWidget(self.textbox_folder_path, 1, 1)
            self.main_layout.addWidget(self.button_select_folder, 1, 2)
            self.main_layout.addWidget(self.label_start_frame, 2, 0)
            self.main_layout.addWidget(self.textbox_start_frame, 2, 1)
            self.main_layout.addWidget(self.label_end_frame, 3, 0)
            self.main_layout.addWidget(self.textbox_end_frame, 3, 1)
            self.main_layout.addWidget(self.label_file_name, 4, 0)
            self.main_layout.addWidget(self.textbox_file_name, 4, 1)
            self.main_layout.addWidget(self.label_dropbox_camera, 5, 0)
            self.main_layout.addWidget(self.dropbox_camera, 5, 1)
            self.main_layout.addWidget(self.label_render_type, 6, 0)
            self.main_layout.addWidget(self.dropbox_render_type, 6, 1)
            self.main_layout.addWidget(self.label_use_cores, 7, 0)
            self.main_layout.addWidget(self.dropbox_cores, 7, 1)
            self.main_layout.addWidget(self.button_start, 8, 1)

            # Add the main layout to window
            # -----------------------------------------------------------------------------------------------------------
            widget = QWidget()
            widget.setLayout(self.main_layout)
            self.setCentralWidget(widget)

        def getFilePath(self):
            if self.file_dialog_browse_file.exec_() == QFileDialog.Accepted:
                selected_file = self.file_dialog_browse_file.selectedFiles()
                if selected_file:
                    self.textbox_file_path.setText(selected_file[0])

        def getFolderPath(self):
            if self.file_dialog_select_folder.exec_() == QFileDialog.Accepted:
                selected_folder = self.file_dialog_select_folder.getExistingDirectory(self, "Select a Directory")
                if selected_folder:
                    self.textbox_folder_path.setText(selected_folder)

        def getCamerasList(self):
            maya.standalone.initialize()
            import maya.cmds as cmds

            cmds.file(self.textbox_file_path.text(), o=True)
            cameras_list = cmds.listCameras()
            self.dropbox_camera.addItems(cameras_list)

            for camera in cameras_list:
                if cmds.getAttr(camera + '.renderable'):
                    self.dropbox_camera.setCurrentIndex(cameras_list.index(camera))

        @staticmethod
        def getCoreCount():
            core_count = [i + 1 for i in range(multiprocessing.cpu_count())]
            core_count.reverse()
            cores = []
            for i in core_count:
                cores.append(str(i))
            return cores

        def startRender(self):

            if self.dropbox_render_type.currentText() == "Multiprocess":
                processes = []
                for i in range(int(self.dropbox_cores.currentText())):
                    process = multiprocessing.Process(target=render, args=(
                        int(self.textbox_start_frame.text()) + i,
                        int(self.textbox_end_frame.text()),
                        int(self.dropbox_cores.currentText()),
                        self.textbox_file_path.text(),
                        self.textbox_folder_path.text(),
                        self.textbox_file_name.text(),
                        self.dropbox_camera.currentText(),
                        self.dropbox_render_type.currentText()
                    )
                                                      )
                    processes.append(process)
                for process in processes:
                    process.start()

            elif self.dropbox_render_type.currentText() == "Sequence":
                render(
                    int(self.textbox_start_frame.text()),
                    int(self.textbox_end_frame.text()),
                    int(self.dropbox_cores.currentText()),
                    self.textbox_file_path.text(),
                    self.textbox_folder_path.text(),
                    self.textbox_file_name.text(),
                    self.dropbox_camera.currentText(),
                    self.dropbox_render_type.currentText()
                )


    myApp = QApplication()
    window = MainWindow()
    window.show()

    myApp.exec_()
    sys.exit(0)
