from abc import ABC, ABCMeta, abstractmethod


class IFigura(metaclass=ABCMeta):
    @abstractmethod
    def pintar(self):
        raise NotImplementedError

    @abstractmethod
    def seleccionar(self):
         raise NotImplementedError

    @abstractmethod
    def cambiar_texto(self, texto):
        raise NotImplementedError


class Figura(IFigura, ABC):

    def __init__(self, p1, p2, color_linea, tipo_linea, ancho_linea: int):
        self.punto_1 = p1
        self.punto_2 = p2
        self.texto = ""
        self.color_linea = color_linea
        self.tipo_linea = tipo_linea
        self.ancho_linea = ancho_linea

    def cambiar_texto(self, texto):
        self.texto = texto


class Linea(Figura):

    def __init__(self, p1, p2, color_linea, tipo_linea, ancho_linea: int):
        super().__init__(p1, p2, color_linea, tipo_linea, ancho_linea)

    def pintar(self):
        print("Pintando una linea")

    def seleccionar(self):
        pass


class FiguraConFondo(Figura, ABC):
    def __init__(self, p1, p2, color_linea, tipo_linea, ancho_linea: int, color_fondo):
        super().__init__(p1, p2, color_linea, tipo_linea, ancho_linea)
        self.color_fondo = color_fondo


class Rectangulo(FiguraConFondo):

    def __init__(self, p1, p2, color_linea, tipo_linea, ancho_linea: int, colo_fondo):
        super().__init__(p1, p2, color_linea, tipo_linea, ancho_linea, colo_fondo)

    def pintar(self):
        print("Pintando una rectángulo")

    def seleccionar(self):
        pass


class Ovalo(FiguraConFondo):

    def __init__(self, p1, p2, color_linea, tipo_linea, ancho_linea: int, colo_fondo):
        super().__init__(p1, p2, color_linea, tipo_linea, ancho_linea, colo_fondo)

    def pintar(self):
        print("Pintando una óvalo")

    def seleccionar(self):
        pass


class Triangulo(FiguraConFondo):

    def __init__(self, p1, p2, color_linea, tipo_linea, ancho_linea: int, colo_fondo):
        super().__init__(p1, p2, color_linea, tipo_linea, ancho_linea, colo_fondo)

    def pintar(self):
        print("Pintando una triángulo")

    def seleccionar(self):
        pass


class Fractal(IFigura):

    def pintar(self):
        print("Pintando fractal")

    def seleccionar(self):
        pass

    def cambiar_texto(self, texto):
        pass

    def __init__(self):
        pass


class Dibujo:
    def __init__(self):
        self.figuras = []

    def agregar_figura(self, figura: IFigura):
        self.figuras.append(figura)

    def dibujar(self):
        for f in self.figuras:
            f.pintar()