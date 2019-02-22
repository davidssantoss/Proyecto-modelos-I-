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
        self.nombreArma="Esta es la arma del elfo"
        self.imagenArma="<Nombre de la carpeta>/<Nombre del archivo>"
    def showWeapon(self):
        pass

class ArmaHada(Arma):
    def __init__(self):
        self.nombreArma="Esta es la arma de la hada"
        self.imagenArma="<Nombre de la carpeta>/<Nombre del archivo>"
    def showWeapon(self):
        pass

class ArmaHumano(Arma):
    def __init__(self):
        self.nombreArma="Esta es la arma del humano"
        self.imagenArma="<Nombre de la carpeta>/<Nombre del archivo>"
    def showWeapon(self):
        pass

class ArmaOgro(Arma):
    def __init__(self):
        self.nombreArma="Esta es la arma del ogro"
        self.imagenArma="<Nombre de la carpeta>/<Nombre del archivo>"
    def showWeapon(self):
        pass


class ArmaMago(Arma):
    def __init__(self):
        self.nombreArma="Esta es la arma del mago"
        self.imagenArma="<Nombre de la carpeta>/<Nombre del archivo>"
    def showWeapon(self):
        pass
