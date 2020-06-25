from PyQt5 import QtCore, QtGui, QtWidgets


def translate_ui(dialog):
    _translate = QtCore.QCoreApplication.translate
    dialog.setWindowTitle(_translate("Dialog", "Dialog"))


class UIMemory(object):

    def init_ui(self, dialog):
        dialog.setObjectName("Dialog")
        dialog.resize(640, 480)
        self.button = QtWidgets.QDialogButtonBox(dialog)
        self.button.setGeometry(QtCore.QRect(10, 440, 621, 32))
        self.button.setOrientation(QtCore.Qt.Horizontal)
        self.button.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.button.setObjectName("buttonBox")

        translate_ui(dialog)
        self.button.accepted.connect(dialog.accept)
        self.button.rejected.connect(dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(dialog)
