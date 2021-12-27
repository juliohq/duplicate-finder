from PyQt5.QtWidgets import (
    QMainWindow,
    QVBoxLayout
)

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Duplicate Finder")
        
        self.layout = QVBoxLayout()
        
        (width, height) = (200, 200)
        self.setMinimumSize(width, height)
        
        self.show()