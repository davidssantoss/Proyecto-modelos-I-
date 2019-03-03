'''
@author: David
'''

from ArmaCreator import ArmaElfoCreador
from ArmaCreator import ArmaElfoCreador2
from ArmaCreator import ArmaElfoCreador3
from ArmaCreator import ArmaHadaCreador
from ArmaCreator import ArmaHumanoCreador
from ArmaCreator import ArmaHumanoCreador2
from ArmaCreator import ArmaHumanoCreador3
from ArmaCreator import ArmaOgroCreador
from ArmaCreator import ArmaOgroCreador2
from ArmaCreator import ArmaOgroCreador3
from ArmaCreator import ArmaMagoCreador
from ArmaCreator import ArmaMagoCreador2
from ArmaCreator import ArmaMagoCreador3

class DeterminarArma():
    crearArma = None
    arma = None
    def __init__(self):
        pass

    def crearArma(self, number):
        self.crearArma = {1: ArmaElfoCreador(), 2:ArmaElfoCreador2(), 3:ArmaElfoCreador3(),
                          4:ArmaHadaCreador(), 5:ArmaHumanoCreador(), 6:ArmaHumanoCreador2(),
                          7:ArmaHumanoCreador3(), 8:ArmaOgroCreador(), 9:ArmaOgroCreador2(),
                          10:ArmaMagoCreador(), 11:ArmaMagoCreador2(), 12:ArmaMagoCreador3()}
        self.arma = self.crearArma[number].crearArma()
        print(str(self.arma))

    def getArma(self):
        return self.arma
