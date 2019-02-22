'''
@author: David
'''

from Arma import ArmaElfo
from Arma import ArmaHada
from Arma import ArmaHumano
from Arma import ArmaOgro
from Arma import ArmaMago

#Estas clases son el Creador y creador concreto de las armas
#del patron Factory Method

class ArmaCreador():
    def __init__(self):
        pass

    def crearArma(self):
        return self.factoryMethod()

    def factoryMethod(self):
        pass


class ArmaElfoCreador(ArmaCreador):
    def __init__(self):
        pass

    def factoryMethod(self):
        return ArmaElfo()


class ArmaHadaCreador(ArmaCreador):
    def __init__(self):
        pass

    def factoryMethod(self):
        return ArmaHada()


class ArmaHumanoCreador(ArmaCreador):
    def __init__(self):
        pass

    def factoryMethod(self):
        return ArmaHumano()


class ArmaOgroCreador(ArmaCreador):
    def __init__(self):
        pass

    def factoryMethod(self):
        return ArmaOgro()


class ArmaMagoCreador(ArmaCreador):
    def __init__(self):
        pass

    def factoryMethod(self):
        return ArmaMago()
