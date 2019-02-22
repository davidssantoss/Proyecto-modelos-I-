'''
@author: David
'''

from DeterminePersonaje import DeterminarPersonaje
from DetermineArma import DeterminarArma
from DetermineEscudo import DeterminarEscudo
from Director import Director
from Builder import PersonajeBuilder
from random import *
from Personaje import *


class EnlistarPersonaje:
    determinarPersonaje = None
    determinarArma = None
    determinarEscudo = None
    constructorPersonaje = None
    armarPersonaje = None

    def __init__(self):
        self.determinarPersonaje = DeterminarPersonaje()
        self.determinarArma = DeterminarArma()
        self.determinarEscudo = Personaje()
        self.constructorPersonaje = PersonajeBuilder()
        self.armarPersonaje = Director()


    def generarChakra(func):
        x = randint(0,3)
        def wrapper(func):
            func(self,x)
            return func
        return wrapper

    def crearArma(self, number):
        self.determinarArma.crearArma(number)


    @generarChakra  #Patron decorator
    def crearEscudo(self, number):
        print(str(number))
        self.determinarEscudo.setEscudo(number)

    def crearPersonaje(self, number):
        self.determinarPersonaje.crearPersonaje(number)

    def BuildPersonaje(self):
        self.armarPersonaje.setBuilder(self.constructorPersonaje)
        self.armarPersonaje.BuildPersonaje(self.determinarPersonaje.getPersonaje(),
                                           self.determinarArma.getArma(),
                                           self.determinarEscudo.getEscudoNum())




                                           
