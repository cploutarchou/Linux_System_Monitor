# app.py
import ui.main as main
from PyQt5 import QtWidgets


class App:

    def __init__(self):
        self.main_ui = main.UIMemory()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = main.UIMemory()
    ui.init_ui(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
