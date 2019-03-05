from tkinter import *
from EnlistPersonaje import EnlistarPersonaje
import pygame, sys
from pygame.locals import *
from random import randint


class charChooserGUI:
    imageweapon = None

    def __init__(self, master):

        # ***** Tamano de la ventana ****
        master.minsize(width=1500, height=600)
        master.maxsize(width=1500, height=600)

        label = Label(bg="#3a3a3a")

        # **** Titulo ****
        title = Label(text="Selecciona tu personaje.", font="times 24 bold italic", fg="#20ef1c", bg="#3a3a3a")
        title.pack(pady=(50, 0))

        # ***** Imagenes ****

        img1 = PhotoImage(file="imagenes/Elfo.png")
        img2 = PhotoImage(file="imagenes/Mago.png")
        img3 = PhotoImage(file="imagenes/Humano.png")
        img4 = PhotoImage(file="imagenes/Ogro.png")
        img5 = PhotoImage(file="imagenes/Hada.png")

        pelfo = Button(label, image=img1, command=lambda: self.chooseWeapon(1,master), bg="black")
        pelfo.image = img1
        pelfo.grid(row=0, padx=6, pady=2)

        pmago = Button(label, image=img2, command=lambda: self.chooseWeapon(2, master), bg="black")
        pmago.image = img2
        pmago.grid(row=0, column=1, padx=6, pady=2)

        phumano= Button(label, image=img3, command=lambda: self.chooseWeapon(3, master), bg="black")
        phumano.image = img3
        phumano.grid(row=0, column=2, padx=6, pady=2)

        pogro = Button(label, image=img4, command=lambda: self.chooseWeapon(4, master), bg="black")
        pogro.image = img4
        pogro.grid(row=0, column=3, padx=6, pady=2)

        phada = Button(label, image=img5, command=lambda: self.chooseWeapon(5, master), bg="black")
        phada.image = img5
        phada.grid(row=0, column=4, padx=6, pady=2)

        # ****** Nombres *****

        name1 = Label(label, text="Elfo", font="times 14 bold italic", fg="#20ef1c", bg="#3a3a3a")
        name1.grid(row=1, column=0)
        name2 = Label(label, text="Mago", font="times 14 bold italic", fg="#20ef1c", bg="#3a3a3a")
        name2.grid(row=1, column=1)
        name3 = Label(label, text="Humano", font="times 14 bold italic", fg="#20ef1c", bg="#3a3a3a")
        name3.grid(row=1, column=2)
        name4 = Label(label, text="Ogro", font="times 14 bold italic", fg="#20ef1c", bg="#3a3a3a")
        name4.grid(row=1, column=3)
        name5 = Label(label, text="Hada", font="times 14 bold italic", fg="#20ef1c", bg="#3a3a3a")
        name5.grid(row=1, column=4)

        # *** Adds the whole content that's on the label ***
        label.pack()


    def chooseWeapon(self, raze, root):

        root.destroy()
        root2 = Tk()
        root2.title("Seleccionar Arma")
        root2.configure(bg="#191919")
        root2.minsize(width=1000, height=550)

        # **** Content ***

        label = Label(bg="#3a3a3a")
        # **** Titulo ****

        title = Label(text="Seleccione su arma.", font="times 24 bold italic", fg="#20ef1c", bg="#3a3a3a")
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
            imagen1 = PhotoImage(file="imagenes\ArmaMago.png")
            imagen2 = PhotoImage(file="imagenes\ArmaMago2.png")
            imagen3 = PhotoImage(file="imagenes\ArmaMago3.png")
            nameweapon = {1: "Baculo", 2: "Espada maldita", 3: "Martillo del dragon"}
            numweapon = {1: 10, 2: 11, 3: 11}
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
            imagen1 = PhotoImage(file="imagenes\ArmaHada.png")
            imagen2 = PhotoImage(file="imagenes\ArmaMago2.png")
            imagen3 = PhotoImage(file="imagenes\ArmaOgro2.png")
            nameweapon = {1: "varita", 2: "Daga bendita", 3: "Sable sabio"}
            numweapon = {1: 4, 2: 11, 3: 9}
        #Se manejan tipos de personajes poniendo las diferentes armas
        
        personaje = Button(label, image=imagen1, command=lambda: self.createChar(raze, numweapon[1], nCharVar.get(), root2), bg="black", activebackground="#222222")
        personaje.image = imagen1
        personaje.grid(row=0, padx=10, pady=5)
        
        
        personajev2 = Button(label, image=imagen2, command=lambda: self.createChar(raze, numweapon[2], nCharVar.get(), root2), bg="black", activebackground="#222222")
        personajev2.image = imagen2
        personajev2.grid(row=0, column=1, padx=10, pady=5)
        
        
        personajev3 = Button(label, image=imagen3, command=lambda: self.createChar(raze, numweapon[3], nCharVar.get(), root2), 
                       bg="black", activebackground="#222222")
        personajev3.image = imagen3
        personajev3.grid(row=0, column=2, padx=10, pady=5)

        # ****** Nombres de las armas *****

        name1 = Label(label, text=nameweapon[1], font="times 10 bold italic", fg="#20ef1c", bg="#3a3a3a")
        name1.grid(row=1, column=0)
        name2 = Label(label, text=nameweapon[2], font="times 10 bold italic", fg="#20ef1c", bg="#3a3a3a")
        name2.grid(row=1, column=1)
        name3 = Label(label, text=nameweapon[3], font="times 10 bold italic", fg="#20ef1c", bg="#3a3a3a")
        name3.grid(row=1, column=2)

        # *** Agrega todo el contenido que esta en el label  ***
        nCharMsj = Label(label, text="Cuantos personajes desea", font="times 15 bold italic",
                         fg="#20ef1c", bg="#222222")
        nCharMsj.grid(row=2, column=0, columnspan=2, sticky=E)

        nCharVar = StringVar(label)
        nCharVar.set("1")
        nChar = ["1", "2"]

        nCharMenu = OptionMenu(label, nCharVar, *nChar)
        nCharMenu.config(width=5, font="times 15 bold italic", fg="#20ef1c", bg="#2d2d2d",
                         highlightbackground="#000000", activebackground="#222222")
        nCharMenu.grid(row=2, column=2, pady=30)

        label.pack()

    def createChar(self, raza, arma, nchar, root2):



        root2.destroy()

        creacion = EnlistarPersonaje()
        creacion.crearArma(arma)
        creacion.crearEscudo()
        creacion.crearPersonaje(raza)

        creacion.BuildPersonaje()

        personaje1 = None
        personaje2 = None

        if nchar == "1":
            personaje1 = creacion.clonePersonaje()

        if nchar == "2":
            personaje1 = creacion.clonePersonaje()
            personaje2 = creacion.clonePersonaje()
        imweapon = personaje1.getArma().getImageArma()
        print(soyarma)
        imchar = personaje1.getImagen()
        print(soy)
        imAurora = personaje1.getEscudo()
        print(soyescudo)


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

            atras1=pygame.image.load("boton/button11.png")
            atras2=pygame.image.load("boton/button1.png")

            boton1=Boton(atras1,atras2,0,0)

            r1=pygame.Rect(50,440,300,500)
            r2=pygame.Rect(400,440,300,500)

            pX=0
            pY=0
            cont1=1000
            cont2=1000
            imagen_arma = pygame.image.load(imweapon)

            imagen_personaje = pygame.image.load(imchar)
            imagen_aurora = pygame.image.load(imAurora)



            if (raze == 1) or (raze == 5):

                X = 90
                Y = 310
                X1 = 340
                Y1 = 310
                X2 = 590
                Y2 = 310
                posX = 100
                posY = 350
                posX1 = 350
                posY1 = 350
                posX2 = 600
                posY2 = 350
                positX = -15
                positY = 260
                positX1 = 235
                positY1 = 260
                positX2 = 485
                positY2 = 260

            if raze == 2:
                X = 28
                Y = 345
                X1 = 278
                Y1 = 345
                X2 = 528
                Y2 = 345
                posX = 150
                posY = 350
                posX1 = 400
                posY1 = 350
                posX2 = 650
                posY2 = 350
                positX = 30
                positY = 260
                positX1 = 280
                positY1 = 260
                positX2 = 530
                positY2 = 260
            if raze == 3:
                X = 140
                Y = 440
                X1 = 390
                Y1 = 440
                X2 = 640
                Y2 = 440
                posX = 100
                posY = 350
                posX1 = 350
                posY1 = 350
                posX2 = 600
                posY2 = 350
                positX = 25
                positY = 260
                positX1 = 275
                positY1 = 260
                positX2 = 525
                positY2 = 260
            if raze == 4:
                X = 170
                Y = 310
                X1 = 420
                Y1 = 310
                X2 = 670
                Y2 = 310
                posX = 100
                posY = 350
                posX1 = 350
                posY1 = 350
                posX2 = 600
                posY2 = 350
                positX = -15
                positY = 240
                positX1 = 235
                positY1 = 240
                positX2 = 485
                positY2 = 240

            fondo = pygame.image.load("fondo.jpg")
            boton2 = Boton(fondo,fondo,0,0)
            velocidad = 5
            verde = (0, 255, 0)
            derecha = True



            wood = pygame.image.load("efecto/2.png")
            while True:
                ventana.fill(verde)
                ventana.blit(fondo, (0, 0))
                if nchar == "1":
                    ventana.blit(imagen_aurora, (positX1, positY1))
                    ventana.blit(imagen_personaje, (posX1, posY1))
                    ventana.blit(imagen_arma, (X1, Y1))
                if nchar == "2":
                    ventana.blit(imagen_aurora, (positX, positY))
                    ventana.blit(imagen_personaje, (posX, posY))
                    ventana.blit(imagen_arma, (X, Y))
                    ventana.blit(imagen_aurora, (positX1, positY1))
                    ventana.blit(imagen_personaje, (posX1, posY1))
                    ventana.blit(imagen_arma, (X1, Y1))
                

                ventana.blit(wood, (450,-70))

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
                    personaje1.attack()
                elif keys[K_p]:
                    personaje2.attack()
                    
                fuente = pygame.font.Font("fuente/fuente.ttf",50)
                text1="Vida del personaje 1:"+str(cont1)
                text2="Vida del personaje 2:"+str(cont2)
                texto1 = fuente.render(text1,1,(155,127,22))
                texto2 = fuente.render(text2,1,(155,155,22))
                ventana.blit(texto1,(500,50))
                ventana.blit(texto2,(500,80))
                pygame.display.flip()

                pygame.display.update()



# *** Defines window ***

root = Tk()
root.title("Escoger personaje")
root.configure(bg="#191919")

escogerPersonaje = charChooserGUI(root)

root.mainloop()
