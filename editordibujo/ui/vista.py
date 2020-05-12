import editordibujo.ui.resources

from PyQt5 import uic
from PyQt5.QtGui import QPaintEvent
from PyQt5.QtWidgets import QMainWindow, QWidget, QFrame, QHBoxLayout
from PyQt5.QtCore import QFile, Qt


class Canvas(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)

    def paintEvent(self, e: QPaintEvent) -> None:
        pass


class MainWindowEditorDibujo(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        file = QFile(":/ui/main_window_editor_dibujo.ui")
        file.open(QFile.ReadOnly)
        uic.loadUi(file, self)
        file.close()

        self.canvas = Canvas()

        self.configurar_ui()

    def configurar_ui(self):
        self.canvas_container.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.canvas_container.setLayout(QHBoxLayout())
        self.canvas_container.layout().addWidget(self.canvas)


