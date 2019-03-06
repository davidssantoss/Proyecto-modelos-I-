'''
@author: david
'''

#Estas clases son el Producto y producto concreto de los personajes
#del patron Factory Method
from copy import deepcopy

class Personaje():

    arma = None
    imagen = None
    escudo = None
    escudoNum = None
    objclone = None

    def __init__(self):
        pass

    def clone(self):
        return deepcopy(self)
    
    def setArma(self, arma):
        self.arma = arma

    def getArma(self):
        return self.arma

    def getImagen(self):
        return self.imagen

    def setEscudo(self, escudo):
        self.escudoNum = escudo
        if (escudo == 0):
            self.escudo = "imagenes/EscudoHada.png"

        if (escudo == 1):
            self.escudo = "imagenes/EscudoElfo.png"

        if (escudo == 2):
            self.escudo = "imagenes/EscudoOgro.png"
        
        if (escudo == 3):
            self.escudo = "imagenes/EscudoMago.png"
            
        if (escudo == 4):
            self.escudo = "imagenes/EscudoHumano.png"

    def getEscudo(self):
        return self.escudo
    def getEscudoNum(self):
        return self.escudoNum

    #metodo de prueba
    def hable(self):
        pass

    
class Elfo(Personaje):

    def __init__(self, attack):
        self.Attack = attack
        print ("Legolas ataca!!")
        self.imagen = "imagenes/Elfo.png"

    def attack(self):
        self._Attack.attack()

    # metodo de prueba
    def hable(self):
        return ("yo soy elfo")

class Ogro(Personaje):
    def __init__(self, attack):
        self._Attack = attack
        print("soy un Ogro")
        self.imagen = "imagenes/Ogro.png"

    def attack(self):
        self._Attack.attack()

    # metodo de prueba
    def hable(self):
        return ("yo soy ogro")

class Hada(Personaje):
    def __init__(self, attack):
        self._Attack = attack
        print("Soy una Hada")
        self.imagen = "imagenes/Hada.png"

    def attack(self):
        self._Attack.attack()

    # metodo de prueba
    def hable(self):
        return ("yo soy Hada")
        

class Humano(Personaje):
    def __init__(self, attack):
        self._Attack = attack
        print("Soy un Humano")
        self.imagen = "imagenes/Humano.png"

    def attack(self):
        self._Attack.attack()

    # metodo de prueba
    def hable(self):
        return ("yo soy humano")

class Mago(Personaje):
    def __init__(self, attack):
        self._Attack = attack
        print("Soy un Mago")
        self.imagen = "imagenes/Mago.png"

    def attack(self):
        self._Attack.attack()

        
    # metodo de prueba
    def hable(self):
        return ("yo soy mago")
