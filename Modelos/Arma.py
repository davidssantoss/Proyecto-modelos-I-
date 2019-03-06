'''
@author: David
'''

#Estas clases son el Producto y producto concreto de las armas
#del patron Factory Method

class Arma():
    nombrearma = None
    imagenarma = None

    def getNombreArma (self):
        return self.nombrearma

    def __init__(self):
        pass

    def mostrarArma(self):
        pass

    def getImageArma(self):
        return self.imagenarma


class ArmaElfo(Arma):
    def __init__(self):
        self.nombrearma = "Arco Elfico"
        self.imagenarma = "imagenes/ArmaElfo.png"
    def showWeapon(self):
        pass

class ArmaElfo2(Arma):
    def __init__(self):
        self.nombrearma = "Cetro Elfico"
        self.imagenarma = "imagenes/ArmaElfo2.png"
    def showWeapon(self):
        pass
    
class ArmaElfo3(Arma):
    def __init__(self):
        self.nombrearma = "Cetro elfico reforzado"
        self.imagenarma = "imagenes/ArmaElfo3.png"
    def showWeapon(self):
        pass


class ArmaHada(Arma):
    def __init__(self):
        self.nombrearma = "varita"
        self.imagenarma = "imagenes/ArmaHada.png"
    def showWeapon(self):
        pass

class ArmaHumano(Arma):
    def __init__(self):
        self.nombrearma = "Sable mortifero"
        self.imagenarma = "imagenes/ArmaHumano.png"
    def showWeapon(self):
        pass

class ArmaHumano2(Arma):
    def __init__(self):
        self.nombrearma = "Maza"
        self.imagenarma = "imagenes/ArmaHumano2.png"
    def showWeapon(self):
        pass

class ArmaHumano3(Arma):
    def __init__(self):
        self.nombrearma = "Lanza sangrienta"
        self.imagenarma = "imagenes/ArmaHumano3.png"
    def showWeapon(self):
        pass


class ArmaOgro(Arma):
    def __init__(self):
        self.nombrearma = "Martillo de caverna"
        self.imagenarma = "imagenes/ArmaOgro.png"
    def showWeapon(self):
        pass

class ArmaOgro2(Arma):
    def __init__(self):
        self.nombrearma = "Daga mortal"
        self.imagenarma = "imagenes/ArmaOgro2.png"
    def showWeapon(self):
        pass

class ArmaOgro3(Arma):
    def __init__(self):
        self.nombrearma = "Hacha maldita"
        self.imagenarma = "imagenes/ArmaOgro3.png"
    def showWeapon(self):
        pass



class ArmaMago(Arma):
    def __init__(self):
        self.nombrearma = "Baculo"
        self.imagenarma = "imagenes/ArmaMago.png"
    def showWeapon(self):
        pass

class ArmaMago2(Arma):
    def __init__(self):
        self.nombrearma = "Espada maldita"
        self.imagenarma = "imagenes/ArmaMago2.png"
    def showWeapon(self):
        pass

class ArmaMago3(Arma):
    def __init__(self):
        self.nombrearma = "Martillo del dragon"
        self.imagenarma = "imagenes/ArmaMago3.png"
    def showWeapon(self):
        pass
