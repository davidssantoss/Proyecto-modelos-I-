'''
@author: David
'''

from PersonajeCreator import *
#Cadena de Responsabilidad


class Handler():
    sucesor = None
    def __init__(self):
        pass

    def handlerRequest(self, number):
        pass

    def getSucesor(self):
        return self.sucesor

    def setSucesor(self, suceso):
        self.sucesor = suceso


class HandlerOpcDefault(Handler):
    def __init__(self):
        pass
    def handlerRequest(self, number):
        return PersonajeCreator()

    
class HandlerOpcUno(Handler):
    def __init__(self):
        pass
    def handlerRequest(self, number):
        if(number==1):
            return ElfoCreator()
        else:
            return self.sucesor.handlerRequest(number)

class HandlerOpcDos(Handler):
    def __init__(self):
        pass
    def handlerRequest(self, number):
        if(number == 2):
            return HadaCreator()
        else:
            return self.sucesor.handlerRequest(number)

class HandlerOpcTres(Handler):
    def __init__(self):
        pass
    def handlerRequest(self, number):
        if(number == 3):
            return HumanoCreator()
        else:
            return self.sucesor.handlerRequest(number)

class HandlerOpcCuatro(Handler):
    def __init__(self):
        pass
    def handlerRequest(self, number):
        if(number == 4):
            return OgroCreator()
        else:
            return self.sucesor.handlerRequest(number)

class HandlerOpcCinco(Handler):
    def __init__(self):
        pass
    def handlerRequest(self, number):
        if(number == 5):
            return MagoCreator()
        else:
            return self.sucesor.handlerRequest(number)

class DeterminarPersonaje():
    crearpersonaje = None
    personaje = None
    def __init__(self):
        pass

    handlers = [HandlerOpcUno(), HandlerOpcDos(), HandlerOpcTres(),
                HandlerOpcCuatro(), HandlerOpcCinco(), HandlerOpcDefault()]

    def crearPersonaje(self, number):
        
        for i in range(0, len(self.handlers)-1,1):
            self.handlers[i].setSucesor(self.handlers[i+1])

        self.crearpersonaje = self.handlers[0].handlerRequest(number)

        self.personaje = self.crearpersonaje.CrearPersonaje()

    def getPersonaje(self):
        return self.personaje



          
    
