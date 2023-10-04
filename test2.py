import os
import sys
import maya.standalone
import multiprocessing
import maya.cmds as cmds
import subprocess
from PySide2.QtWidgets import (QApplication, QLabel, QMainWindow, QWidget, QGridLayout, QPushButton, QLineEdit,
                               QFileDialog)
from PySide2.QtGui import QFont, QIcon
sys.path.append('C:\\Program Files\\Autodesk\\Arnold\\maya2024\\scripts')


# class RenderLogic:
#
#     def __int__(self, start_frame, end_frame, step, file_to_render, render_folder, frame_name, camera_name):
#
#         prefs_folder = os.path.expanduser("~\\Documents\\maya\\2024\\prefs")
#         cmds.workspace(prefs_folder, openWorkspace=True)
#         cmds.setAttr("defaultRenderGlobals.imageFilePrefix", (render_folder + frame_name), type="string")
#         mtoa_path = "C:\Program Files\Autodesk\Arnold\maya2024\plug-ins\mtoa.mll"
#         cmds.loadPlugin(mtoa_path)
#
#         self.start_frame = start_frame
#         self.end_frame = end_frame
#         self.step = step
#         self.mtoa_path = mtoa_path
#         self.file_to_render = file_to_render
#         self.render_folder = render_folder
#         self.frame_name = frame_name
#         self.camera_name = camera_name
#
#     def startRender(self, start, end, by_step):
#         for number in range(start, end + 1, by_step):
#             cmds.arnoldRender(cam=self.camera_name, seq=number)
#
#     def multiRender(self):
#         processes = []
#         for i in range(self.step):
#             process = multiprocessing.Process(target=self.startRender,
#                                               args=(self.start_frame + i, self.end_frame, self.step))
#             processes.append(process)
#         for process in processes:
#             process.start()
#
#     def sequenceRender(self):
#         self.startRender(self.start_frame, self.end_frame, self.step)
#
#     @staticmethod
#     def skiplicenseCheck(skip=True):
#         if skip:
#             cmds.setAttr("defaultArnoldRenderOptions.skipLicenseCheck", 1)
#
# # ----------------------------------------------------------------------------------------------------------------


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

        # File path textbox
        # --------------------------------------------------------------------
        self.textbox_file_path = QLineEdit()
        self.textbox_file_path.setMaximumWidth(300)
        self.textbox_file_path.setMinimumSize(200, 23)

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
        self.main_layout.addWidget(self.button_start, 4, 0)

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
    def startRender(self):

        param1 = self.textbox_start_frame.text()
        param2 = self.textbox_end_frame.text()
        param3 = str(4)
        param4 = self.textbox_file_path.text()
        param5 = self.textbox_folder_path.text()
        param6 = "kjh"
        param7 = "persp"

        subprocess.call(["mayapy", "main.py", param1, param2, param3, param4, param5, param6, param7])

myApp = QApplication()
window = MainWindow()
window.show()

myApp.exec_()
sys.exit(0)

