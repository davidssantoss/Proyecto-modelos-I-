'''
@author: David
'''

from Arma import ArmaElfo
from Arma import ArmaElfo2
from Arma import ArmaElfo3
from Arma import ArmaHada
from Arma import ArmaHumano
from Arma import ArmaHumano2
from Arma import ArmaHumano3
from Arma import ArmaOgro
from Arma import ArmaOgro2
from Arma import ArmaOgro3
from Arma import ArmaMago
from Arma import ArmaMago2
from Arma import ArmaMago3

#Estas clases son el Creador y creador concreto de las armas
#del patron Factory Method

class ArmaCreador():
    def __init__(self):
        pass

    def CrearArma(self):
        return self.factoryMethod()

    def factoryMethod(self):
        pass


class ArmaElfoCreador(ArmaCreador):
    def __init__(self):
        pass

    def factoryMethod(self):
        return ArmaElfo()

class ArmaElfoCreador2(ArmaCreador):
    def __init__(self):
        pass

    def factoryMethod(self):
        return ArmaElfo2()

class ArmaElfoCreador3(ArmaCreador):
    def __init__(self):
        pass

    def factoryMethod(self):
        return ArmaElfo3()



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

class ArmaHumanoCreador2(ArmaCreador):
    def __init__(self):
        pass

    def factoryMethod(self):
        return ArmaHumano2()

class ArmaHumanoCreador3(ArmaCreador):
    def __init__(self):
        pass

    def factoryMethod(self):
        return ArmaHumano3()

class ArmaOgroCreador(ArmaCreador):
    def __init__(self):
        pass

    def factoryMethod(self):
        return ArmaOgro()

class ArmaOgroCreador2(ArmaCreador):
    def __init__(self):
        pass

    def factoryMethod(self):
        return ArmaOgro2()

class ArmaOgroCreador3(ArmaCreador):
    def __init__(self):
        pass

    def factoryMethod(self):
        return ArmaOgro3()

class ArmaMagoCreador(ArmaCreador):
    def __init__(self):
        pass

    def factoryMethod(self):
        return ArmaMago()

class ArmaMagoCreador2(ArmaCreador):
    def __init__(self):
        pass

    def factoryMethod(self):
        return ArmaMago2()

class ArmaMagoCreador3(ArmaCreador):
    def __init__(self):
        pass

    def factoryMethod(self):
        return ArmaMago3()
