import maya.cmds as cmds

from PySide2.QtWidgets import (QApplication, QLabel, QMainWindow, QGroupBox, QHBoxLayout, QComboBox, QWidget,
                               QGridLayout, QPushButton, QLineEdit)
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

        self.font_1 = QFont()
        self.font_1.setPointSize(20)
        self.font_1.setFamily("Verdana")

        # Set window size, maximum and minimum size
        # -----------------------------------------------------------------------------------------------------------

        self.setWindowTitle("Side Render")
        self.setGeometry(300, 300, 300, 300)
        self.setMaximumSize(800, 400)
        self.setMinimumSize(200, 100)
        self.setWindowIcon(self.icon)

        # Label
        # -----------------------------------------------------------------------------------------------------------

        self.label_1 = QLabel(self)
        self.label_1.setText("label")
        self.label_1.setBaseSize(100, 50)
        self.label_1.setFont(self.font_1)
        self.label_1.setToolTip("This is my label")

        # Camera name textbox
        # --------------------------------------------------------------------
        self.camera_name_textbox = QLineEdit()
        self.camera_name_textbox.setMaximumWidth(150)

        # "Make Camera" button
        # --------------------------------------------------------------------
        self.make_cam_button = QPushButton("Make Camera")
        self.make_cam_button.setCheckable(False)
        self.make_cam_button.clicked.connect(lambda: self.MakeCamera(self.camera_name_textbox.text()))


        # Create grid style main layout
        # -----------------------------------------------------------------------------------------------------------
        self.main_layout = QGridLayout()
        self.main_layout.addWidget(self.label_1, 0, 0)
        self.main_layout.addWidget(self.camera_name_textbox, 0, 1)
        self.main_layout.addWidget(self.make_cam_button, 1, 0)

        # Add the main layout to window
        # -----------------------------------------------------------------------------------------------------------
        widget = QWidget()
        widget.setLayout(self.main_layout)
        self.setCentralWidget(widget)

    def MakeCamera(self, camera_name):
        cmds.camera(name=camera_name)
        cmds.rename(camera_name + '1', camera_name)


# myApp = QApplication()
window = MainWindow()
window.show()

# myApp.exec_()
# sys.exit(0)

