'''
@author: david
'''

#Estas clases son el Producto y producto concreto de los personajes
#del patron Factory Method

class Personaje():

    arma = None
    imagen = None
    escudo = None
    escudoNum = None

    def __init__(self):
        pass
    
    def setArma(self, arma):
        self.arma = arma

    def getArma(self):
        return self.arma

    def getImagen(self):
        return self.imagen

    def setEscudo(self, escudo):
        self.escudoNum = escudo
        if (escudo == 0):
            self.escudo = "<Nombre de la carpeta>/<nombre de la imagen>"

        if (escudo == 1):
            self.escudo = "<Nombre de la carpeta>/<nombre de la imagen>"

        if (escudo == 2):
            self.escudo = "<Nombre de la carpeta>/<nombre de la imagen>"

    def getEscudo(self):
        return self.escudo
    def getEscudoNum(self):
        return self.escudoNum

    
class Elfo(Personaje):

    def __init__(self, attack):
        self.Attack = attack
        print ("Legolas ataca!!")
        self.imagen = "<Nombre de la carpeta>/<nombre de la imagen>"

    def attack(self):
        self._Attack.attack()

class Ogro(Personaje):
    def __init__(self, attack):
        self._Attack = attack
        print("soy un Ogro")
        self.imagen = "<Nombre de la carpeta>/<nombre de la imagen>"

    def attack(self):
        self._Attack.attack()

class Hada(Personaje):
    def __init__(self, attack):
        self._Attack = attack
        print("Soy una Hada")
        self.imagen = "<Nombre de la carpeta>/<nombre de la imagen>"

    def attack(self):
        self._Attack.attack()

class Humano(Personaje):
    def __init__(self, attack):
        self._Attack = attack
        print("Soy un Humano")
        self.imagen = "<Nombre de la carpeta>/<nombre de la imagen>"

    def attack(self):
        self._Attack.attack()

class Mago(Personaje):
    def __init__(self, attack):
        self._Attack = attack
        print("Soy un Mago")
        self.imagen = "<Nombre de la carpeta>/<nombre de la imagen>"

    def attack(self):
        self._Attack.attack()

        
