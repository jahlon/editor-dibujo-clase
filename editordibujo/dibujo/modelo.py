from abc import ABC, ABCMeta, abstractmethod

from PyQt5.QtCore import QPoint, QLine, Qt, QRect
from PyQt5.QtGui import QPainter, QColor, QPen, QBrush


class IFigura(metaclass=ABCMeta):
    @abstractmethod
    def pintar(self, qp: QPainter, seleccionada: bool):
        raise NotImplementedError

    @abstractmethod
    def esta_dentro(self, x: int, y: int):
         raise NotImplementedError


class Figura(IFigura, ABC):

    def __init__(self, p1: QPoint, p2: QPoint, color_linea: QColor, tipo_linea: Qt.PenStyle, ancho_linea: int):
        self.punto_1 = p1
        self.punto_2 = p2
        self.color_linea = color_linea
        self.tipo_linea = tipo_linea
        self.ancho_linea = ancho_linea


class Linea(Figura):

    def __init__(self, p1: QPoint, p2: QPoint, color_linea: QColor, tipo_linea: Qt.PenStyle, ancho_linea: int):
        super().__init__(p1, p2, color_linea, tipo_linea, ancho_linea)
        self.linea = QLine(p1, p2)

    def pintar(self, qp: QPainter, seleccionada: bool):
        pen = QPen()
        pen.setStyle(self.tipo_linea)
        pen.setWidth(self.ancho_linea)
        pen.setColor(self.color_linea)
        qp.setPen(pen)
        qp.drawLine(self.linea)

        if seleccionada:
            brush = QBrush()
            brush.setColor(Qt.green)
            brush.setStyel(Qt.SolidPattern)
            pen = QPen()
            pen.setWidth(1)
            pen.setColor(Qt.black)
            qp.setPen(pen)
            qp.setBrush(brush)
            qp.drawEllipse(self.punto_1.x() - 5, self.punto_1.y() - 5, 7, 7)
            qp.drawEllipse(self.punto_2.x() - 5, self.punto_2.y() - 5, 7, 7)

    def esta_dentro(self, x: int, y: int):
        m = (self.punto_2.y() - self.punto_1.y()) / (self.punto_2.x() - self.punto_1.x())
        termino_y = m * (x - self.punto_1.x()) + self.punto_1.y()
        min_x = min(self.punto_1.x(), self.punto_2.x())
        max_x = max(self.punto_1.x(), self.punto_2.x())
        return (min_x <= x <= max_x) and (termino_y - 5 <= y <= termino_y + 5)


class FiguraConFondo(Figura, ABC):
    def __init__(self, p1: QPoint, p2: QPoint, color_linea: QColor, tipo_linea: Qt.PenStyle, ancho_linea: int,
                 color_fondo: QColor):
        super().__init__(p1, p2, color_linea, tipo_linea, ancho_linea)
        self.color_fondo = color_fondo
        self.rect = QRect(p1, p2)

    def pintar(self, qp: QPainter, seleccionada: bool):
        pen = QPen()
        pen.setStyle(self.tipo_linea)
        pen.setWidth(self.ancho_linea)
        pen.setColor(self.color_linea)

        brush = QBrush()
        brush.setColor(self.color_fondo)
        brush.setStyle(Qt.SolidPattern)

        qp.setPen(pen)
        qp.setBrush(brush)
        self._pintar(qp)

        if seleccionada:
            brush = QBrush()
            brush.setColor(Qt.green)
            brush.setStyel(Qt.SolidPattern)
            pen = QPen()
            pen.setWidth(1)
            pen.setColor(Qt.black)
            qp.setPen(pen)
            qp.setBrush(brush)
            qp.drawEllipse(self.punto_1.x() - 5, self.punto_1.y() - 5, 7, 7)
            qp.drawEllipse(self.punto_2.x() - 5, self.punto_2.y() - 5, 7, 7)
            qp.drawEllipse(self.punto_1.x() - 5, self.punto_2.y() - 5, 7, 7)
            qp.drawEllipse(self.punto_2.x() - 5, self.punto_1.y() - 5, 7, 7)

    def esta_dentro(self, x: int, y: int):
        return self.rect.contains(x, y)

    @abstractmethod
    def _pintar(self, qp:QPainter):
        raise NotImplementedError


class Rectangulo(FiguraConFondo):

    def __init__(self, p1: QPoint, p2: QPoint, color_linea: QColor, tipo_linea: Qt.PenStyle, ancho_linea: int,
                 color_fondo: QColor):
        super().__init__(p1, p2, color_linea, tipo_linea, ancho_linea, color_fondo)

    def _pintar(self, qp: QPainter):
        qp.drawRect(self.rect)


class Ovalo(FiguraConFondo):

    def __init__(self, p1: QPoint, p2: QPoint, color_linea: QColor, tipo_linea: Qt.PenStyle, ancho_linea: int,
                 color_fondo: QColor):
        super().__init__(p1, p2, color_linea, tipo_linea, ancho_linea, color_fondo)

    def _pintar(self, qp: QPainter):
        qp.drawEllipse(self.rect)


class Dibujo:
    def __init__(self):
        self.figuras = []

    def agregar_figura(self, figura: IFigura):
        self.figuras.append(figura)

    def dibujar(self, qp: QPainter):
        for f in self.figuras:
            f.pintar(qp, False)
