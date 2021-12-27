from PyQt5.QtWidgets import QApplication
from qt.window import Window

import sys

app = QApplication([])
window = Window()

while True:
    sys.exit(app.exec())