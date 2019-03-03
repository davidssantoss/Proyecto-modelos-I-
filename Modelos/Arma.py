'''
@author: David
'''

#Estas clases son el Producto y producto concreto de las armas
#del patron Factory Method

class Arma():
    nombreArma = None
    imagenArma = None

    def getNombreArma (self):
        return self.nombreArma

    def __init__(self):
        pass

    def mostrarArma(self):
        pass

    def getImageArma(self):
        return self.imagenArma


class ArmaElfo(Arma):
    def __init__(self):
        self.nombreArma="Esta es la Arma del Elfo"
        self.imagenArma="imagenes/ArmaElfo.png"
    def showWeapon(self):
        pass

class ArmaElfo2(Arma):
    def __init__(self):
        self.nombreArma="Esta es la Arma del Elfo"
        self.imagenArma="imagenes/ArmaElfo2.png"
    def showWeapon(self):
        pass
    
class ArmaElfo3(Arma):
    def __init__(self):
        self.nombreArma="Esta es la Arma del Elfo"
        self.imagenArma="imagenes/ArmaElfo3.png"
    def showWeapon(self):
        pass


class ArmaHada(Arma):
    def __init__(self):
        self.nombreArma="Esta es la Arma de la Hada"
        self.imagenArma="imagenes/ArmaHada.png"
    def showWeapon(self):
        pass

class ArmaHumano(Arma):
    def __init__(self):
        self.nombreArma="Esta es la Arma del Humano"
        self.imagenArma="imagenes/ArmaHumano.png"
    def showWeapon(self):
        pass

class ArmaHumano2(Arma):
    def __init__(self):
        self.nombreArma="Esta es la Arma del Humano"
        self.imagenArma="imagenes/ArmaHumano2.png"
    def showWeapon(self):
        pass

class ArmaHumano3(Arma):
    def __init__(self):
        self.nombreArma="Esta es la Arma del Humano"
        self.imagenArma="imagenes/ArmaHumano3.png"
    def showWeapon(self):
        pass


class ArmaOgro(Arma):
    def __init__(self):
        self.nombreArma="Esta es la Arma del Ogro"
        self.imagenArma="imagenes/ArmaOgro.png"
    def showWeapon(self):
        pass

class ArmaOgro2(Arma):
    def __init__(self):
        self.nombreArma="Esta es la Arma del Ogro"
        self.imagenArma="imagenes/ArmaOgro2.png"
    def showWeapon(self):
        pass

class ArmaOgro3(Arma):
    def __init__(self):
        self.nombreArma="Esta es la Arma del Ogro"
        self.imagenArma="imagenes/ArmaOgro3.png"
    def showWeapon(self):
        pass



class ArmaMago(Arma):
    def __init__(self):
        self.nombreArma="Esta es la Arma del Mago"
        self.imagenArma="imagenes/ArmaMago.png"
    def showWeapon(self):
        pass

class ArmaMago2(Arma):
    def __init__(self):
        self.nombreArma="Esta es la Arma del Mago"
        self.imagenArma="imagenes/ArmaMago2.png"
    def showWeapon(self):
        pass

class ArmaMago3(Arma):
    def __init__(self):
        self.nombreArma="Esta es la Arma del Mago"
        self.imagenArma="imagenes/ArmaMago3.png"
    def showWeapon(self):
        pass
