'''
@author: David
'''

from EscudoCreator import ElfoEscudoCreator
from EscudoCreator import HadaEscudoCreator
from EscudoCreator import HumanoEscudoCreator
from EscudoCreator import OgroEscudoCreator
from EscudoCreator import MagoEscudoCreator

class DeterminarEscudo():
    crearescudo = None
    escudo = None
    def __init__ (self):
        pass

    def crearEscudo(self, number):
        self.crearEscudo = {1: ElfoEscudoCreator(), 2: HadaEscudoCreator(), 3:HumanoEscudoCreator(), 4:OgroEscudoCreator(),
                            5:MagoEscudoCreator()}

    def getEscudo(self):
        return self.escudo
