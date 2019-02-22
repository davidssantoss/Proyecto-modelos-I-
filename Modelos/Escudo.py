'''
@author: David
'''

#Estas clases son el Producto y producto concreto de los escudos
#del patron Factory Method


class Escudo():
    nombreEscudo = None
    imagenEscudo = None

    def getNombreEscudo(self):
        return self.nombreEscudo

    def __init__(self):
        pass

    def muestraEscudo(self):
        pass

    def getImagenEscudo(self):
        return self.imagenEscudo


class ElfoEscudo(Escudo):
    def __init__(self):
        self.nombreEscudo = "escudo del elfo"
        self.imagenEscudo = "<nombre de la carpeta>/<nombre del archivo>"

    def muestraEscudo(self):
        pass

class HadaEscudo(Escudo):
    def __init__(self):
        self.nombreEscudo = "escudo de la hada"
        self.imagenEscudo = "<nombre de la carpeta>/<nombre del archivo>"

    def muestraEscudo(self):
        pass

class HumanoEscudo(Escudo):
    def __init__(self):
        self.nombreEscudo = "escudo del humano"
        self.imagenEscudo = "<nombre de la carpeta>/<nombre del archivo>"

    def muestraEscudo(self):
        pass

class OgroEscudo(Escudo):
    def __init__(self):
        self.nombreEscudo = "escudo del Ogro"
        self.imagenEscudo = "<nombre de la carpeta>/<nombre del archivo>"

    def muestraEscudo(self):
        pass

class MagoEscudo(Escudo):
    def __init__(self):
        self.nombreEscudo = "escudo del mago"
        self.imagenEscudo = "<nombre de la carpeta>/<nombre del archivo>"

    def muestraEscudo(self):
        pass

