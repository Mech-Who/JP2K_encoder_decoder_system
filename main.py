import sys

from PySide6 import QtWidgets
from src.gui.main_window import MainWindow

app = QtWidgets.QApplication([])

main_window = MainWindow()
main_window.resize(800, 600)
main_window.show()

sys.exit(app.exec())
