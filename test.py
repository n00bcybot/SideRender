import maya.cmds as cmds

from PySide2.QtWidgets import (QApplication, QLabel, QMainWindow, QGroupBox, QHBoxLayout, QComboBox, QWidget,
                               QGridLayout, QPushButton, QLineEdit, QFileDialog, QVBoxLayout)
from PySide2.QtGui import QFont, QIcon
from PySide2 import QtCore
import sys
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('File Path Selector')

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.file_path_line_edit = QLineEdit(self)
        layout.addWidget(self.file_path_line_edit)

        select_file_button = QPushButton('Select File', self)
        select_file_button.clicked.connect(self.openFileDialog)
        layout.addWidget(select_file_button)

    def openFileDialog(self):
        options = QFileDialog.Options()
        file_dialog = QFileDialog(self, options=options)
        file_dialog.setNameFilter('All Files (*)')

        if file_dialog.exec_() == QFileDialog.Accepted:
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                file_path = selected_files[0]
                self.file_path_line_edit.setText(file_path)


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()


