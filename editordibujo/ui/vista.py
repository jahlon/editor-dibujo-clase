import editordibujo.ui.resources

from PyQt5 import uic, QtGui
from PyQt5.QtGui import QPaintEvent, QPainter, QBrush
from PyQt5.QtWidgets import QMainWindow, QWidget, QFrame, QHBoxLayout
from PyQt5.QtCore import QFile, Qt, QPoint

from editordibujo.dibujo.modelo import Linea, Dibujo, Rectangulo, Ovalo


class Canvas(QWidget):

    def __init__(self, main_window):
        QWidget.__init__(self)
        self.main_window = main_window
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)

    def mousePressEvent(self, e: QtGui.QMouseEvent) -> None:
       if e.button() == Qt.LeftButton:
           self.main_window.hacer_click(e.x(), e.y())

    def paintEvent(self, e: QPaintEvent) -> None:
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHints(QPainter.Antialiasing, True)
        self.main_window.dibujar(qp)

        x_sel = self.main_window.x_seleccionado
        y_sel = self.main_window.y_seleccionado
        if x_sel != -1 and y_sel != -1:
            brush = QBrush()
            brush.setColor(Qt.green)
            brush.setStyle(Qt.SolidPattern)
            qp.setBrush(brush)
            qp.drawEllipse(x_sel-2, y_sel-2, 4, 4)

        qp.end()


class MainWindowEditorDibujo(QMainWindow):

    SELECCIONAR = 1
    DIBUJAR = 2
    NINGUNA = 0

    def __init__(self):
        QMainWindow.__init__(self)
        file = QFile(":/ui/main_window_editor_dibujo.ui")
        file.open(QFile.ReadOnly)
        uic.loadUi(file, self)
        file.close()

        self.dibujo = Dibujo()
        self.canvas = Canvas(self)
        self.x_seleccionado = -1
        self.y_seleccionado = -1

        self.configurar_ui()

    def configurar_ui(self):
        self.canvas_container.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.canvas_container.setLayout(QHBoxLayout())
        self.canvas_container.layout().addWidget(self.canvas)

    def hacer_click(self, x: int, y: int):
        acc = self.accion()
        if acc == MainWindowEditorDibujo.SELECCIONAR:
            pass
        elif acc == MainWindowEditorDibujo.DIBUJAR:
            if self.x_seleccionado == -1 and self.y_seleccionado == -1:
                self.x_seleccionado = x
                self.y_seleccionado = y
            else:
                self.agregar_figura(self.x_seleccionado, self.y_seleccionado, x, y)
                self.x_seleccionado = -1
                self.y_seleccionado = -1
        self.canvas.repaint()

    def accion(self):
        if self.pbutton_seleccionar.isChecked():
            return MainWindowEditorDibujo.SELECCIONAR
        elif self. pbutton_linea.isChecked() or self.pbutton_ovalo.isChecked() or self.pbutton_rect.isChecked():
            return MainWindowEditorDibujo.DIBUJAR
        else:
            return MainWindowEditorDibujo.NINGUNA

    def agregar_figura(self, x1: int, y1: int, x2: int, y2: int):
        p1 = QPoint(x1, y1)
        p2 = QPoint(x2, y2)
        color_linea = Qt.blue
        ancho = 5
        tipo_linea = Qt.DashLine
        color_fondo = Qt.yellow
        if self.pbutton_linea.isChecked():
            figura = Linea(p1, p2, color_linea, tipo_linea, ancho)
        elif self.pbutton_rect.isChecked():
            figura = Rectangulo(p1, p2, color_linea, tipo_linea, ancho, color_fondo)
        elif self.pbutton_ovalo.isChecked():
            figura = Ovalo(p1, p2, color_linea, tipo_linea, ancho, color_fondo)

        self.dibujo.agregar_figura(figura)
        self.canvas.repaint()

    def dibujar(self, qp: QPainter):
        self.dibujo.dibujar(qp)




