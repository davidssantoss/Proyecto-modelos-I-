'''
@author: David
'''
from Personaje import Elfo
from Personaje import Hada
from Personaje import Humano
from Personaje import Ogro
from Personaje import Mago

# Se podría implementar el patrón Strategy donde los ataques sean mas "mortiferos"

#Estas clases son el Creador y creador concreto de los personajes
#del patron Factory Method


class PersonajeCreator():
    def __init__(self):
        pass
    def factoryMethod(self):
        pass
    def CrearPersonaje(self):
        return self.factoryMethod()


class ElfoCreator(PersonajeCreator):
    def __init__ (self):
        pass
    def factoryMethod (self):
        pass
        # return Elfo( un ataque )
        
class HumanoCreator(PersonajeCreator):
    def __init__ (self):
        pass
    def factoryMethod (self):
        pass
        # return Humano( un ataque )

class OgroCreator(PersonajeCreator):
    def __init__ (self):
        pass
    def factoryMethod (self):
        pass
        # return Ogro( un ataque )

class HadaCreator(PersonajeCreator):
    def __init__ (self):
        pass
    def factoryMethod (self):
        pass
        # return Hada(un ataque)
    
class MagoCreator(PersonajeCreator):
    def __init__ (self):
        pass
    def factoryMethod (self):
        pass
        # return Mago( un ataque )
