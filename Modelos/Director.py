'''
@author : David
'''

# Clase director del patron Factory Method

class Director():
    constructor = None

    def __init__(self):
        pass

    def setBuilder(self, constructor):
        self.constructor = constructor

    def getPersonaje(self):
        return self.constructor.getPersonaje()

    def BuildPersonaje(self, personaje, arma, escudo):
        self.constructor.buildPersonaje(personaje)
        print("paso: ", personaje)
        print("personajeBuilder: ", self.constructor.personaje)
        self.constructor.buildArma(arma)
        
        self.constructor.buildEscudo(escudo)
