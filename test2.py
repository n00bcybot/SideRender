import maya.cmds as cmds

from PySide2.QtWidgets import (QApplication, QLabel, QMainWindow, QGroupBox, QHBoxLayout, QComboBox, QWidget,
                               QGridLayout, QPushButton, QLineEdit, QFileDialog)
from PySide2.QtGui import QFont, QIcon
from PySide2 import QtCore
import sys
sys.path.append('C:\\Program Files\\Autodesk\\Arnold\\maya2024\\scripts')


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)

        # Set window icon. An instance of the QIcon object that contains the path to the ico file needs to be created first
        self.icon = QIcon(
            "C:\\Users\\fresh\\Desktop\\truemax\\semester4\\powershell\\renderScript\\interface\\favicon.ico")

        self.font_verdana = QFont()
        self.font_verdana.setPointSize(10)
        self.font_verdana.setFamily("Verdana")

        # Set window size, maximum and minimum size
        # -----------------------------------------------------------------------------------------------------------
        self.setWindowTitle("Side Render")
        self.setGeometry(300, 300, 300, 300)
        self.setMaximumSize(800, 400)
        self.setMinimumSize(200, 100)
        self.setWindowIcon(self.icon)

        # Label start frame
        # -----------------------------------------------------------------------------------------------------------
        self.label_start_frame = QLabel(self)
        self.label_start_frame.setText("Start Frame")
        self.label_start_frame.setBaseSize(100, 50)
        self.label_start_frame.setFont(self.font_verdana)
        self.label_start_frame.setToolTip("Start frame")

        # Label end frame
        # -----------------------------------------------------------------------------------------------------------
        self.label_end_frame = QLabel(self)
        self.label_end_frame.setText("End Frame")
        self.label_end_frame.setBaseSize(100, 50)
        self.label_end_frame.setFont(self.font_verdana)
        self.label_end_frame.setToolTip("End frame")

        # Browse file dialog
        # --------------------------------------------------------------------
        self.browse_file_dialog = QFileDialog(self)
        self.browse_file_dialog.setFileMode(QFileDialog.ExistingFiles)
        self.browse_file_dialog.setNameFilter("Maya files (*.ma *.mb)")
        self.browse_file_dialog.selectNameFilter('*.ma')

        # Select folder dialog
        # --------------------------------------------------------------------
        self.select_folder_dialog = QFileDialog(self)
        self.select_folder_dialog.setFileMode(QFileDialog.DirectoryOnly)

        # Start frame text box
        # --------------------------------------------------------------------
        self.start_frame_textbox = QLineEdit()
        self.start_frame_textbox.setMaximumWidth(300)

        # End frame text box
        # --------------------------------------------------------------------
        self.end_frame_textbox = QLineEdit()
        self.end_frame_textbox.setMaximumWidth(300)

        # Browse file button
        # --------------------------------------------------------------------
        self.browse_file_button = QPushButton()
        self.browse_file_button.setText('Browse')
        self.browse_file_button.setCheckable(False)
        # self.make_cam_button.clicked.connect(lambda: self.MakeCamera(self.camera_name_textbox.text()))
        self.browse_file_button.clicked.connect(self.getFilePath)

        # Select folder button
        # --------------------------------------------------------------------
        self.select_folder_button = QPushButton()
        self.select_folder_button.setText('Browse')
        self.select_folder_button.setCheckable(False)
        self.select_folder_button.clicked.connect(self.getFolderPath)

        # Create grid style main layout
        # -----------------------------------------------------------------------------------------------------------
        self.main_layout = QGridLayout()
        self.main_layout.addWidget(self.label_start_frame, 0, 0)
        self.main_layout.addWidget(self.start_frame_textbox, 0, 1)
        self.main_layout.addWidget(self.browse_file_button, 0, 2)
        self.main_layout.addWidget(self.label_end_frame, 1, 0)
        self.main_layout.addWidget(self.end_frame_textbox, 1, 1)
        self.main_layout.addWidget(self.select_folder_button, 1, 2)

        # Add the main layout to window
        # -----------------------------------------------------------------------------------------------------------
        widget = QWidget()
        widget.setLayout(self.main_layout)
        self.setCentralWidget(widget)

    def getFilePath(self):
        if self.browse_file_dialog.exec_() == QFileDialog.Accepted:
            selected_file = self.browse_file_dialog.selectedFiles()
            if selected_file:
                self.start_frame_textbox.setText(selected_file[0])
    def getFolderPath(self):
        if self.select_folder_dialog.exec_() == QFileDialog.Accepted:
            selected_folder = self.select_folder_dialog.getExistingDirectory()
            if selected_folder:
                self.start_frame_textbox.setText(selected_folder[0])

    def startRender(self):
        with open("main.py") as f:
            exec(f.read())


myApp = QApplication()
window = MainWindow()
window.show()

myApp.exec_()
sys.exit(0)
