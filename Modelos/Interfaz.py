from tkinter import *
from EnlistCharacter import EnlistCharacter
import pygame, sys
from pygame.locals import *
from random import randint


class charChooserGUI:
    imageweapon = None

    def __init__(self, master):

        # ***** Parent Window Size ****
        master.minsize(width=2000, height=1000)
        master.maxsize(width=2000, height=1000)

        label = Label(bg="#3a3a3a")

        # **** Title ****

        title = Label(text="Selecciona tu personaje.", font="times 24 bold italic", fg="#ffca1e", bg="#3a3a3a")
        title.pack(pady=(50, 0))

        # ***** Images ****
        img1 = PhotoImage(file="imagenes/Elfo.png")
        img2 = PhotoImage(file="imagenes/Mago.png")
        img3 = PhotoImage(file="imagenes/Humano.png")
        img4 = PhotoImage(file="imagenes/Ogro.png")
        img5 = PhotoImage(file="imagenes/Hada.png")
        

        pelfo = Button(label, image=img1, command=lambda: self.chooseConjurer(master), bg="black")
        pelfo.image = img1
        pelfo.grid(row=0, padx=7, pady=2)
        pmago = Button(label, image=img2, command=lambda: self.chooseWeapon(2, master), bg="black")
        pmago.image = img2
        pmago.grid(row=0, column=1, padx=7, pady=2)
        phumano= Button(label, image=img3, command=lambda: self.chooseWeapon(3, master), bg="black")
        phumano.image = img3
        phumano.grid(row=0, column=2, padx=7, pady=2)
        pogro = Button(label, image=img4, command=lambda: self.chooseWeapon(4, master), bg="black")
        pogro.image = img4
        pogro.grid(row=0, column=3, padx=7, pady=2)
        phada = Button(label, image=img5, command=lambda: self.chooseWeapon(4, master), bg="black")
        phada.image = img5
        phada.grid(row=0, column=4, padx=7, pady=2)

        # ****** Names *****

        name1 = Label(label, text="Elfo", font="times 10 bold italic", fg="#ffca1e", bg="#3a3a3a")
        name1.grid(row=1, column=0)
        name2 = Label(label, text="Mago", font="times 10 bold italic", fg="#ffca1e", bg="#3a3a3a")
        name2.grid(row=1, column=1)
        name3 = Label(label, text="Humano", font="times 10 bold italic", fg="#ffca1e", bg="#3a3a3a")
        name3.grid(row=1, column=2)
        name4 = Label(label, text="Ogro", font="times 10 bold italic", fg="#ffca1e", bg="#3a3a3a")
        name4.grid(row=1, column=3)
        name5 = Label(label, text="Hada", font="times 10 bold italic", fg="#ffca1e", bg="#3a3a3a")
        name5.grid(row=1, column=4)

        # *** Adds the whole content that's on the label ***
        label.pack()

    def chooseConjurer(self, root):

        root.destroy()
        root2 = Tk()
        root2.title("Conjurer Chooser")
        root2.configure(bg="#191919")
        root2.minsize(width=660, height=460)

        # *** Main content ***

        label = Label(bg="#3a3a3a")

        #*** Inner content ***

        title = Label(text="Which side do you want to be? D:<", font="times 22 bold italic", fg="#ffca1e", bg="#3a3a3a")
        title.pack(pady=(40, 0))

        img1 = PhotoImage(file="images_characters/1.png")
        img2 = PhotoImage(file="images_characters/5.png")

        pelfo= Button(label, image=img1, command=lambda: self.chooseWeapon(1, root2), bg="black", highlightbackground="#222222")
        pelfo.image = img1
        pelfo.grid(row=0, padx=(40,40), pady=10)
        pmago = Button(label, image=img2, command=lambda: self.chooseWeapon(5, root2), bg="black")
        pmago.image = img2
        pmago.grid(row=0, column=1, padx=(40,40), pady=10)

        # ****** Names *****

        name1 = Label(label, text="Good  Witch", font="times 10 bold italic", fg="#ffca1e", bg="#3a3a3a")
        name1.grid(row=1, column=0)
        name2 = Label(label, text="Evil Witch", font="times 10 bold italic", fg="#ffca1e", bg="#3a3a3a")
        name2.grid(row=1, column=1)

        label.pack()

    def chooseWeapon(self, raze, root):

        root.destroy()
        root2 = Tk()
        root2.title("Weapon Chooser")
        root2.configure(bg="#191919")
        root2.minsize(width=1000, height=600)

        # **** Content ***

        label = Label(bg="#3a3a3a")
        # **** Title ****

        title = Label(text="Choose your weapon", font="times 24 bold italic", fg="#ffca1e", bg="#3a3a3a")
        title.pack(pady=(50, 0))

        # ***** Images ****
        raze1 = raze

        if (raze1 == 1) or (raze1 == 5):
            image1 = PhotoImage(file="imagenes\ArmaElfo.png")
            image2 = PhotoImage(file="weapons_witch\HeavenlyScepter.png")
            image3 = PhotoImage(file="weapons_witch\Scepter.png")
            nameweapon = {1: "Epic Scepter", 2: "Heavenly Scepter", 3: "Scepter"}
            numweapon = {1: 1, 2: 2, 3: 3}
        if raze1 == 2:
            image1 = PhotoImage(file="imagenes\ArmaMago.png")
            image2 = PhotoImage(file="weapons_demon\DamnBlade.png")
            image3 = PhotoImage(file="weapons_demon\DragonHammer.png")
            nameweapon = {1: "Hades Sword", 2: "Damn Blade", 3: "Dragon Hammer"}
            numweapon = {1: 4, 2: 5, 3: 6}
        if raze1 == 3:
            image1 = PhotoImage(file="imagenes/ArmaHumano.png")
            image2 = PhotoImage(file="weapons_goblin\Hammer.png")
            image3 = PhotoImage(file="weapons_goblin\OdinSpear.png")
            nameweapon = {1: "Excalibur Sword", 2: "Hammer", 3: "Odin Spear"}
            numweapon = {1: 7, 2: 8, 3: 9}
        if raze1 == 4:
            image1 = PhotoImage(file="imagenes\ArmaOgro.png")
            image2 = PhotoImage(file="weapons_orc\MortalDagger.png")
            image3 = PhotoImage(file="weapons_orc\VampireSpear.png")
            nameweapon = {1: "Dragon Tail", 2: "Mortal Dagger", 3: "Vampire Spear"}
            numweapon = {1: 10, 2: 11, 3: 12}

        pelfo = Button(label, image=image1, command=lambda: self.createChar(raze, numweapon[1], nCharVar.get(), root2), bg="black", activebackground="#222222")
        pelfo.image = image1
        pelfo.grid(row=0, padx=10, pady=5)
        pmago = Button(label, image=image2, command=lambda: self.createChar(raze, numweapon[2], nCharVar.get(), root2),bg="black", activebackground="#222222")
        pmago.image = image2
        pmago.grid(row=0, column=1, padx=10, pady=5)
        phumano= Button(label, image=image3, command=lambda: self.createChar(raze, numweapon[3], nCharVar.get(), root2), bg="black", activebackground="#222222")
        phumano.image = image3
        phumano.grid(row=0, column=2, padx=10, pady=5)

        # ****** Names *****

        name1 = Label(label, text=nameweapon[1], font="times 10 bold italic", fg="#ffca1e", bg="#3a3a3a")
        name1.grid(row=1, column=0)
        name2 = Label(label, text=nameweapon[2], font="times 10 bold italic", fg="#ffca1e", bg="#3a3a3a")
        name2.grid(row=1, column=1)
        name3 = Label(label, text=nameweapon[3], font="times 10 bold italic", fg="#ffca1e", bg="#3a3a3a")
        name3.grid(row=1, column=2)

        # *** Adds the whole content that's on the label ***
        nCharMsj = Label(label, text="Choose how many characters you want :)", font="times 15 bold italic",
                         fg="#ffca1e", bg="#222222")
        nCharMsj.grid(row=2, column=0, columnspan=2, sticky=E)

        nCharVar = StringVar(label)
        nCharVar.set("1")
        nChar = ["1", "2", "3"]

        nCharMenu = OptionMenu(label, nCharVar, *nChar)
        nCharMenu.config(width=5, font="times 15 bold italic", fg="#ffca1e", bg="#2d2d2d",
                         highlightbackground="#000000", activebackground="#222222")
        nCharMenu.grid(row=2, column=2, pady=30)

        label.pack()

    def createChar(self, raze, weapon, nchar, root2):


        root2.destroy()

        creacion = EnlistCharacter()
        creacion.createWeapon(weapon)
        creacion.createAurora()
        creacion.createCharacter(raze)

        creacion.BuildCharacter()

        personaje1 = None
        personaje12 = None
        personaje13 = None

        if nchar == "1":
            personaje1 = creacion.cloneCharacter()

        if nchar == "2":
            personaje1 = creacion.cloneCharacter()
            personaje12 = creacion.cloneCharacter()
        if nchar == "3":
            personaje1 = creacion.cloneCharacter()
            personaje12 = creacion.cloneCharacter()
            personaje13 = creacion.cloneCharacter()
        imweapon = personaje1.getWeapon().getImageWeapon()
        print(imweapon)
        imchar = personaje1.getImage()
        print(imchar)
        imAurora = personaje1.getAurora()
        print(imAurora)


  
        
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

        

     



        class Animation():

            pygame.init()
            ventana = pygame.display.set_mode((1024, 683))
            pygame.display.set_caption("personajes")

            atras1=pygame.image.load("boton/button11.png")
            atras2=pygame.image.load("boton/button1.png")

            boton1=Boton(atras1,atras2,0,0)

            r1=pygame.Rect(50,440,300,500)
            r2=pygame.Rect(400,440,300,500)
            r3=pygame.Rect(600,440,300,500)
            pX=0
            pY=0
            cont1=1000
            cont2=1000
            cont3=1000
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
                if nchar == "3":
                    ventana.blit(imagen_aurora, (positX, positY))
                    ventana.blit(imagen_personaje, (posX, posY))
                    ventana.blit(imagen_arma, (X, Y))
                    ventana.blit(imagen_aurora, (positX1, positY1))
                    ventana.blit(imagen_personaje, (posX1, posY1))
                    ventana.blit(imagen_arma, (X1, Y1))
                    ventana.blit(imagen_aurora, (positX2, positY2))
                    ventana.blit(imagen_personaje, (posX2, posY2))
                    ventana.blit(imagen_arma, (X2, Y2))
  
                ventana.blit(wood, (450,-70))

                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                        pintar_rect=False
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
                if keys [K_j]:
                    positX2 -= velocidad
                    X2 -= velocidad
                    posX2 -= velocidad
                elif keys [K_l]:
                    positX2 += velocidad
                    posX2 += velocidad
                    X2 += velocidad
                if keys[K_SPACE]:
                    SonidoEspada.play()
                    personaje1.attack()
                fuente = pygame.font.Font("fuente/fuente.ttf",50)
                text1="Vida del grupo:"+str(cont1)
       
                pygame.display.flip()
                
                pygame.display.update()



# *** Defines window ***

root = Tk()
root.title("Character chooser")
root.configure(bg="#191919")

charChooser = charChooserGUI(root)

root.mainloop()
