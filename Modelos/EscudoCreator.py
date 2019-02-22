'''
@author: David
'''

from Escudo import ElfoEscudo
from Escudo import HadaEscudo
from Escudo import HumanoEscudo
from Escudo import OgroEscudo
from Escudo import MagoEscudo

#Estas clases son el Creador y creador concreto de los escudos
#del patron Factory Method

class EscudoCreator():
    def __init__(self):
        pass

    def crearEscudo(self):
        return self.factoryMethod()

    def factoryMethod(self):
        pass


class ElfoEscudoCreator(EscudoCreator):
    def __init__(self):
        pass
    def factoryMethod (self):
        return ElfoEscudo()

class HadaEscudoCreator(EscudoCreator):
    def __init__(self):
        pass
    def factoryMethod (self):
        return HadaEscudo()


class HumanoEscudoCreator(EscudoCreator):
    def __init__(self):
        pass
    def factoryMethod (self):
        return HumanoEscudo()


class OgroEscudoCreator(EscudoCreator):
    def __init__(self):
        pass
    def factoryMethod (self):
        return OgroEscudo()


class MagoEscudoCreator(EscudoCreator):
    def __init__(self):
        pass
    def factoryMethod (self):
        return MagoEscudo()

