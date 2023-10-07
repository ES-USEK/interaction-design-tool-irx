# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interaction_manager/ui/saveasdialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SaveAsDialog(object):
    def setupUi(self, SaveAsDialog):
        SaveAsDialog.setObjectName("SaveAsDialog")
        SaveAsDialog.resize(513, 244)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SaveAsDialog.sizePolicy().hasHeightForWidth())
        SaveAsDialog.setSizePolicy(sizePolicy)
        SaveAsDialog.setMinimumSize(QtCore.QSize(0, 0))
        SaveAsDialog.setMaximumSize(QtCore.QSize(1000, 800))
        self.gridLayout_3 = QtWidgets.QGridLayout(SaveAsDialog)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox = QtWidgets.QGroupBox(SaveAsDialog)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.fileNameLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.fileNameLineEdit.setObjectName("fileNameLineEdit")
        self.gridLayout_12.addWidget(self.fileNameLineEdit, 2, 0, 1, 4)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_12.addItem(spacerItem, 7, 1, 1, 1)
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_12.addWidget(self.line, 0, 0, 1, 4)
        self.selectFolderToolButton = QtWidgets.QToolButton(self.groupBox)
        self.selectFolderToolButton.setObjectName("selectFolderToolButton")
        self.gridLayout_12.addWidget(self.selectFolderToolButton, 1, 3, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.groupBox)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_12.addWidget(self.buttonBox, 5, 0, 1, 4)
        self.label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout_12.addWidget(self.label, 3, 0, 1, 4)
        self.line_2 = QtWidgets.QFrame(self.groupBox)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_12.addWidget(self.line_2, 4, 0, 1, 4)
        self.folderNameLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.folderNameLineEdit.setObjectName("folderNameLineEdit")
        self.gridLayout_12.addWidget(self.folderNameLineEdit, 1, 0, 1, 3)
        self.gridLayout_2.addLayout(self.gridLayout_12, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(SaveAsDialog)
        self.buttonBox.accepted.connect(SaveAsDialog.accept)
        self.buttonBox.rejected.connect(SaveAsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SaveAsDialog)

    def retranslateUi(self, SaveAsDialog):
        _translate = QtCore.QCoreApplication.translate
        SaveAsDialog.setWindowTitle(_translate("SaveAsDialog", "Save As Dialog"))
        self.groupBox.setTitle(_translate("SaveAsDialog", "Save As Design"))
        self.fileNameLineEdit.setPlaceholderText(_translate("SaveAsDialog", "File Name"))
        self.selectFolderToolButton.setText(_translate("SaveAsDialog", "..."))
        self.label.setText(_translate("SaveAsDialog", "Note: if the file exists, it will be overwritten!"))
        self.folderNameLineEdit.setPlaceholderText(_translate("SaveAsDialog", "Select Folder"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SaveAsDialog = QtWidgets.QDialog()
    ui = Ui_SaveAsDialog()
    ui.setupUi(SaveAsDialog)
    SaveAsDialog.show()
    sys.exit(app.exec_())
