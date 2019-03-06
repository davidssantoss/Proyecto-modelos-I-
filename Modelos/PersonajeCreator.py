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
class Strategy():
    
    damage = 10

    def __init__(self,func=None):
        self.listaDisparo = []
        if func:
             self.attack = func

    def attack(self):
        print("Attacking with " + str(self.damage) + " hit points")

class AtacarA(Strategy):
    def atacar(self):
        print("Attacking with " + str(self.damage) + " hit points")
        
        


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
        return Elfo(Strategy(AtacarA.atacar))
        pass
        # return Hada(un ataque)
        
class HumanoCreator(PersonajeCreator):
    def __init__ (self):
        pass
    def factoryMethod (self):
        return Humano(Strategy())
        pass
        # return Hada(un ataque)

class OgroCreator(PersonajeCreator):
    def __init__ (self):
        pass
    def factoryMethod (self):
        return Ogro(Strategy())
        pass
        # return Hada(un ataque)

class HadaCreator(PersonajeCreator):
    def __init__ (self):
        pass
    def factoryMethod (self):
        return Hada(Strategy())
        pass
        # return Hada(un ataque)
    
class MagoCreator(PersonajeCreator):
    def __init__ (self):
        pass
    def factoryMethod (self):
        return Mago(Strategy())
        pass
        # return Mago( un ataque )
