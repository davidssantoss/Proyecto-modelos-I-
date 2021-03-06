from tkinter import *
from EnlistPersonaje import EnlistarPersonaje
import pygame, sys
from pygame.locals import *
from random import randint


class charChooserGUI:
    imageweapon = None

    def __init__(self, master):

        # ***** Tamano de la ventana ****
        master.minsize(width=1300, height=500)
        master.maxsize(width=1300, height=500)

        label = Label(bg="#aa6612")

        # **** Titulo ****
        title = Label(text="Selecciona tu personaje.", font="courier 24 bold italic", fg="#eac98f", bg="#aa6612")
        title.pack(pady=(50, 0))

        # ***** Imagenes ****

        img1 = PhotoImage(file="imagenes/Elfo.png")
        img2 = PhotoImage(file="imagenes/Mago.png")
        img3 = PhotoImage(file="imagenes/Humano.png")
        img4 = PhotoImage(file="imagenes/Ogro.png")
        img5 = PhotoImage(file="imagenes/Hada.png")

        pelfo = Button(label, image=img1, command=lambda: self.chooseWeapon(1,master), bg="#eac98f")
        pelfo.image = img1
        pelfo.grid(row=0, padx=6, pady=2)
        print("pelfo: ",pelfo)

        pmago = Button(label, image=img2, command=lambda: self.chooseWeapon(5, master), bg="#eac98f")
        pmago.image = img2
        pmago.grid(row=0, column=1, padx=6, pady=2)

        phumano= Button(label, image=img3, command=lambda: self.chooseWeapon(3, master), bg="#eac98f")
        phumano.image = img3
        phumano.grid(row=0, column=2, padx=6, pady=2)

        pogro = Button(label, image=img4, command=lambda: self.chooseWeapon(4, master), bg="#eac98f")
        pogro.image = img4
        pogro.grid(row=0, column=3, padx=6, pady=2)

        phada = Button(label, image=img5, command=lambda: self.chooseWeapon(2, master), bg="#eac98f")
        phada.image = img5
        phada.grid(row=0, column=4, padx=6, pady=2)

        # ****** Nombres *****
        
        name1 = Label(label, text="Elfo", font="courier 14 bold italic", fg="#eac98f", bg="#3a3a3a")
        name1.grid(row=1, column=0)
        name2 = Label(label, text="Mago", font="courier 14 bold italic", fg="#eac98f", bg="#3a3a3a")
        name2.grid(row=1, column=1)
        name3 = Label(label, text="Humano", font="courier 14 bold italic", fg="#eac98f", bg="#3a3a3a")
        name3.grid(row=1, column=2)
        name4 = Label(label, text="Ogro", font="courier 14 bold italic", fg="#eac98f", bg="#3a3a3a")
        name4.grid(row=1, column=3)
        name5 = Label(label, text="Hada", font="courier 14 bold italic", fg="#eac98f", bg="#3a3a3a")
        name5.grid(row=1, column=4)

        # *** Adds the whole content that's on the label ***
        label.pack()


    def chooseWeapon(self, raze, root):
        print("chosePeronaje raze: ", raze)
        root.destroy()
        root2 = Tk()
        root2.title("Seleccionar Arma")
        root2.configure(bg="#f29f3a")
        root2.minsize(width=1000, height=550)

        # **** Content ***

        label = Label(bg="#aa6612")
        # **** Titulo ****

        title = Label(text="Selecciona tu arma.", font="courier 24 bold italic", fg="#eac98f", bg="#aa6612")
        title.pack(pady=(50, 0))

        # ***** Imagenes ****
        raze1 = raze

        if raze1 == 1:
            imagen1 = PhotoImage(file="imagenes\ArmaElfo.png")
            imagen2 = PhotoImage(file="imagenes\ArmaElfo2.png")
            imagen3 = PhotoImage(file="imagenes\ArmaElfo3.png")
            nameweapon = {1: "Arco Elfico", 2: "Cetro Elfico", 3: "Cetro elfico reforzado"}
            numweapon = {1: 1, 2: 2, 3: 3}
        if raze1 == 2:
            imagen1 = PhotoImage(file="imagenes\ArmaHada.png")
            imagen2 = PhotoImage(file="imagenes\ArmaMago2.png")
            imagen3 = PhotoImage(file="imagenes\ArmaOgro2.png")
            nameweapon = {1: "varita", 2: "Espada maldita", 3: "Daga mortal"}
            numweapon = {1:4, 2: 11, 3: 9}
        if raze1 == 3:
            imagen1 = PhotoImage(file="imagenes\ArmaHumano.png")
            imagen2 = PhotoImage(file="imagenes\ArmaHumano2.png")
            imagen3 = PhotoImage(file="imagenes\ArmaHumano3.png")
            nameweapon = {1: "Sable mortifero", 2: "Maza", 3: "Lanza sangrienta"}
            numweapon = {1: 5, 2: 6, 3: 7}
        if raze1 == 4:
            imagen1 = PhotoImage(file="imagenes\ArmaOgro.png")
            imagen2 = PhotoImage(file="imagenes\ArmaOgro2.png")
            imagen3 = PhotoImage(file="imagenes\ArmaOgro3.png")
            nameweapon = {1: "Martillo de caverna", 2: "Daga mortal", 3: "Hacha maldita"}
            numweapon = {1: 8, 2: 9, 3: 10}
        if raze1 == 5:
            imagen1 = PhotoImage(file="imagenes\ArmaMago.png")
            imagen2 = PhotoImage(file="imagenes\ArmaMago2.png")
            imagen3 = PhotoImage(file="imagenes\ArmaMago3.png")
            nameweapon = {1: "Baculo", 2: "Espada maldita", 3: "Martillo del dragon"}
            numweapon = {1: 10, 2: 11, 3: 12}
        #Se manejan tipos de personajes poniendo las diferentes armas
        #print ("seleccionada",raze)
        personaje = Button(label, image=imagen1, command=lambda: self.createChar(raze,
                                                                                 numweapon[1],
                                                                                 nCharVar.get(),
                                                                                 root2), bg="#eac98f", activebackground="#222222")
        personaje.image = imagen1
        personaje.grid(row=0, padx=10, pady=5)
        
        
        personajev2 = Button(label, image=imagen2, command=lambda: self.createChar(raze, numweapon[2], nCharVar.get(), root2), bg="#eac98f", activebackground="#222222")
        personajev2.image = imagen2
        personajev2.grid(row=0, column=1, padx=10, pady=5)
        
        
        personajev3 = Button(label, image=imagen3, command=lambda: self.createChar(raze, numweapon[3], nCharVar.get(), root2), 
                       bg="#eac98f", activebackground="#222222")
        personajev3.image = imagen3
        personajev3.grid(row=0, column=2, padx=10, pady=5)

        # ****** Nombres de las armas *****

        name1 = Label(label, text=nameweapon[1], font="courier 10 bold italic", fg="#eac98f", bg="#3a3a3a")
        name1.grid(row=1, column=0)
        name2 = Label(label, text=nameweapon[2], font="courier 10 bold italic", fg="#eac98f", bg="#3a3a3a")
        name2.grid(row=1, column=1)
        name3 = Label(label, text=nameweapon[3], font="courier 10 bold italic", fg="#eac98f", bg="#3a3a3a")
        name3.grid(row=1, column=2)

        # *** Agrega todo el contenido que esta en el label  ***
        nCharMsj = Label(label, text="¿Cuántos personajes desea?", font="courier 15 bold italic",
                         fg="#20ef1c", bg="#222222")
        nCharMsj.grid(row=2, column=0, columnspan=2, sticky=E)

        nCharVar = StringVar(label)
        nCharVar.set("2")
        nChar = ["1", "2"]

        nCharMenu = OptionMenu(label, nCharVar, *nChar)
        nCharMenu.config(width=5, font="courier 15 bold italic", fg="#eac98f", bg="#2d2d2d",
                         highlightbackground="#000000", activebackground="#222222")
        nCharMenu.grid(row=2, column=2, pady=30)

        label.pack()

    def createChar(self, raze, arma, nchar, root2):


        root2.destroy()

        creacion = EnlistarPersonaje()
        creacion.crearArma(arma)
        creacion.crearEscudo()
        creacion.crearPersonaje(raze)
        
        creacion.BuildPersonaje()
        print("crear personaje")


        personaje1 = None
        personaje2 = None

        if nchar == "1":
            personaje1 = creacion.clonePersonaje()

        if nchar == "2":
            personaje1 = creacion.clonePersonaje()
            personaje2 = creacion.clonePersonaje()
        imArma = personaje1.getArma().getImageArma()
        print(imArma)
        imPers = personaje1.getImagen()
        print(imPers)
        imEscudo = personaje1.getEscudo()
        print(imEscudo)


        class BotonAtacar(pygame.sprite.Sprite):
            def __init__(self,imagen1,imagen2,x=-50,y=500):
                self.imagen_normal=imagen1
                self.imagen_seleccion=imagen2
                self.imagen_actual=self.imagen_normal
                self.rect=self.imagen_actual.get_rect()
                self.rect.left,self.rect.top=(50,500)

        class Boton(pygame.sprite.Sprite):
            def __init__(self,imagen1,imagen2,x=200,y=200):
                self.imagen_normal=imagen1
                self.imagen_seleccion=imagen2
                self.imagen_actual=self.imagen_normal
                self.rect=self.imagen_actual.get_rect()
                self.rect.left,self.rect.top=(x,y)

            def update(self,pantalla,cursor):
                if cursor.colliderect(self.rect):
                    self.imagen_actual=self.imagen_seleccion
                else: self.imagen_actual=self.imagen_normal

                pantalla.blit(self.imagen_actual,self.rect)            


        class Animation():

            pygame.init()
            ventana = pygame.display.set_mode((1024, 683))

            pygame.display.set_caption("personajes")

            atras1=pygame.image.load("imagenes/botonV.png")
            atras2=pygame.image.load("imagenes/botonV.png")

            boton1=Boton(atras1, atras2, 0, 0)

            r1=pygame.Rect(50,440,300,500)
            r2=pygame.Rect(400,440,300,500)

            pX=0
            pY=0
            cont1=1000
            cont2=1000
            imagen_arma = pygame.image.load(imArma)

            imagen_personaje = pygame.image.load(imPers)
            imagen_escudo = pygame.image.load(imEscudo)



            if (raze == 1):
                #pos arma
                X = 90
                Y = 310
                #pos arma2
                X1 = 340
                Y1 = 310
                #pos per
                posX = 100
                posY = 350
                #pos per2
                posX1 = 350
                posY1 = 350
                #pos esc
                positX = 200
                positY = 470
                #pos esc2
                positX1 = 450
                positY1 = 470
                

            if raze == 2:
                #pos arma
                X = 400
                Y = 345
                #pos arma2
                X1 = 118
                Y1 = 345
                #pos per
                posX = 500
                posY = 350
                #pos per2
                posX1 = 150
                posY1 = 350
                #pos esc
                positX = 620
                positY = 480
                #pos esc2
                positX1 = 290
                positY1 = 480
                
            if raze == 3:
                #pos arma
                X = 140
                Y = 440
                #pos arma 2 per
                X1 = 390
                Y1 = 440
                #pos per
                posX = 100
                posY = 350
                #pos per2
                posX1 = 350
                posY1 = 350
                #pos esc
                positX = 25
                positY = 400
                #pos esc2
                positX1 = 275
                positY1 = 400
                
            if raze == 4:
                #pos arma
                X = 170
                Y = 310
                #pos arma2
                X1 = 420
                Y1 = 310
                #pos per
                posX = 100
                posY = 350
                #pos pers2
                posX1 = 350
                posY1 = 350
                #pos esc
                positX = -15
                positY = 280
                #pos esc2
                positX1 = 235
                positY1 = 280
                
            if (raze == 5):
                #pos arma
                X = 90
                Y = 310
                #pos arma2
                X1 = 340
                Y1 = 310
                #pos per
                posX = 100
                posY = 350
                #pos per2
                posX1 = 350
                posY1 = 350
                #pos esc
                positX = 200
                positY = 470
                #pos esc2
                positX1 = 450
                positY1 = 470
                
        

            fondo = pygame.image.load("imagenes/fondo1.jpg")
            boton2 = Boton(fondo,fondo,0,0)
            velocidad = 5
            verde = (0, 255, 0)
            derecha = True



            #wood = pygame.image.load("imagenes/2.png")
            while True:
                ventana.fill(verde)
                ventana.blit(fondo, (0, 0))
                if nchar == "1":
                    ventana.blit(imagen_escudo, (positX1, positY1))
                    ventana.blit(imagen_personaje, (posX1, posY1))
                    ventana.blit(imagen_arma, (X1, Y1))
                if nchar == "2":
                    #imagen_personaje2 = pygame.transform.flip(imagen_personaje2, True, False)
                    ventana.blit(imagen_escudo, (positX, positY))
                    ventana.blit(imagen_personaje, (posX, posY))
                    ventana.blit(imagen_arma, (X, Y))
                    ventana.blit(imagen_escudo, (positX1, positY1))
                    ventana.blit(imagen_personaje, (posX1, posY1))
                    ventana.blit(imagen_arma, (X1, Y1))

                if len(personaje1.listaDisparo)>0:
                    for x in personaje1.listaDisparo:
                        x.dibujar(ventana)
                        x.recorrido()
                        #x.colision(personaje1)
                        if x.rect.left<-10:
                            personaje1.listaDisparo.remove(x)

                if len(personaje2.listaDisparo)>0:
                    for x in personaje2.listaDisparo:
                        x.dibujar(ventana)
                        x.recorrido()
                        #x.colision(personaje1)
                        if x.rect.right<10:
                            personaje2.listaDisparo.remove(x)
                
                

                #ventana.blit(wood, (450,-70))

                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                        pintar_rect=False
                    #Agregar el contador para cuando se pierda vida y muera e inmediatamente finalice el juego


                keys = pygame.key.get_pressed()
                if keys[K_LEFT]:
                    positX -= velocidad
                    X -= velocidad
                    posX -= velocidad
                elif keys[K_RIGHT]:
                    positX += velocidad
                    posX += velocidad
                    X += velocidad
                if keys [K_a]:
                    positX1 -= velocidad
                    X1 -= velocidad
                    posX1 -= velocidad
                elif keys[K_d]:
                    positX1 += velocidad
                    posX1 += velocidad
                    X1 += velocidad
                if keys[K_SPACE]:
                    xd = posX
                    yd = posY+100
                    personaje1.atacar(xd,yd)
                    cont2=cont2-10
                    print("vida 2:"+ str(cont2))
                    if cont2==0:
                        print("muerto 2")
                        pygame.quit()
                        sys.exit()
                        pintar_rect=False
                elif keys[K_p]:
                    xd = posX1
                    yd = posY1+100
                    personaje2.atacar(xd,yd)
                    cont1=cont1-10
                    print("vida 1:"+ str(cont1))
                    if cont1==0:
                        print("muerto 1")
                        pygame.quit()
                        sys.exit()
                        pintar_rect=False
                    
                fuente = pygame.font.Font("fuente/fuente.ttf",30)
                text1="Vida personaje 1: "+str(cont1)
                text2="Vida personaje 2: "+str(cont2)
                texto1 = fuente.render(text1,1,(155,127,22))
                texto2 = fuente.render(text2,1,(155,200,22))
                ventana.blit(texto1,(20,50))
                ventana.blit(texto2,(500,50))
                pygame.display.flip()

                pygame.display.update()



# *** Defines window ***

root = Tk()
root.title("Escoger personaje")
root.configure(bg="#f29f3a")

escogerPersonaje = charChooserGUI(root)

root.mainloop()
