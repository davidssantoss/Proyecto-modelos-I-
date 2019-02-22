'''
@author: David
'''

from ArmaCreator import ArmaElfoCreador
from ArmaCreator import ArmaHadaCreador
from ArmaCreator import ArmaHumanoCreador
from ArmaCreator import ArmaOgroCreador
from ArmaCreator import ArmaMagoCreador

class DeterminarArma():
    crearArma = None
    arma = None
    def __init__(self):
        pass

    def crearArma(self, number):
        self.crearArma = {1: ArmaElfoCreador(), 2:ArmaHadaCreador(),
                          3:ArmaHumanoCreador(), 4:ArmaOgroCreador(),
                          5:ArmaMagoCreador()}
        self.arma = self.crearArma[number].crearArma()
        print(str(self.arma))

    def getArma(self):
        return self.arma
