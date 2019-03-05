'''
@author: David
'''

class Builder():
    personaje = None
    arma = None
    escudo = None

    def __init__(self):
        pass

    def buildPersonaje(self):
        pass

    def buildArma(self):
        pass

    def buildEscudo(self):
        pass

    def getPersonaje(self):
        return self.personaje


class PersonajeBuilder(Builder):

    def __init__(self):
        pass

    def buildPersonaje(self, personaje):
        self.personaje = personaje

    def buildArma(self, arma):
        self.personaje.setArma(arma)

    def buildEscudo(self, escudo):
        self.personaje.setEscudo(escudo)
