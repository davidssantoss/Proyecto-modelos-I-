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
    determinarpersonaje = None
    determinararma = None
    determinarescudo = None
    constructorpersonaje = None
    armarpersonaje = None
    personajesclonados = None

    def __init__(self):
        self.determinarpersonaje = DeterminarPersonaje()
        self.determinararma = DeterminarArma()
        self.determinarescudo = Personaje()
        self.constructorpersonaje = PersonajeBuilder()
        self.armarpersonaje = Director()


    def generarChakra(func):
        x = randint(0,4)
        def wrapper(self):
            func(self, x)
            return func
        return wrapper

    def crearArma(self, number):
        self.determinararma.crearArma(number)


    @generarChakra  #Patron decorator
    def crearEscudo(self, number):
        print(str(number))
        self.determinarescudo.setEscudo(number)

    def crearPersonaje(self, number):
        self.determinarpersonaje.crearPersonaje(number)

    def BuildPersonaje(self):
        self.armarpersonaje.setBuilder(self.constructorpersonaje)
        self.armarpersonaje.BuildPersonaje(self.determinarpersonaje.getPersonaje(),
                                           self.determinararma.getArma(),
                                           self.determinarescudo.getEscudoNum())
        

    def clonePersonaje(self):
        self.personajesclonados = self.armarpersonaje.getPersonaje()
        return self.personajesclonados.clone()


                                           
