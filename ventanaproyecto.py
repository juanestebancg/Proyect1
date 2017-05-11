import tkinter
import time
import random
from time import clock
w0=tkinter.Tk()# se crea la ventana

w0.geometry("700x500")#tamaño de la ventana
w0.title("Crazy Runner")

fondo=tkinter.PhotoImage(file="vector.png")#fondo de la pantalla

lblfondo=tkinter.Label(w0,image=fondo).place(x=0)#Label del fondo

#campo de entrada label jugador 1
lblfondo1=tkinter.Label(w0,text="Jugador 1: ",font=("Arial",14)).place(x=10,y=10)

#jugador 1 campo

j1=tkinter.StringVar()
j1.set("")
j1txt=tkinter.Entry(w0,textvariable=j1).place(x=120,y=10)

#campo de entrada label jugador 2
lblfondo2=tkinter.Label(w0,text="Jugador 2: ",font=("Arial",14)).place(x=10,y=40)

#para jugar 
lblfondo3=tkinter.Label(w0,text="Play ",font=("Arial",14)).place(x=500,y=40)
#jugador 1 campo

j2=tkinter.StringVar()
j2.set("")
j2txt=tkinter.Entry(w0,textvariable=j2).place(x=120,y=40)
##Variables
presiono = False
x = None
z=None
i = 0
i2=0
j = 0
c=0 #contador 1
c2=0 #contador 2
a1=0
contadormini=0
reloadrunner=0
reloadfighter=0
gaso=tkinter.StringVar()#label de la gasolina
puntos=tkinter.StringVar()#label de los puntos
velocidad=tkinter.StringVar()#label de la velocidad
########---------------------------------------------------------------------------------------------- nivel 1
##imagenes

mapa=tkinter.PhotoImage(file="mapa1111.png")#imagen del mapa
#mapa22=tkinter.PhotoImage(file="casito.png")
carro = tkinter.PhotoImage(file="c11.png")#el jugador
carroc=tkinter.PhotoImage(file="c11chocado.png")#imagen choque1
carroc2=tkinter.PhotoImage(file="c11chocado2.png")#imagen choque2
runner=tkinter.PhotoImage(file="c22.png")#imagen del runner
minivan=tkinter.PhotoImage(file="c33.png")#imagen del minivan
fighter=tkinter.PhotoImage(file="c44.png")#imagen fighter
referencia=tkinter.PhotoImage(file="cuad11.png")#referencia
##imagenes

def nivel1(): # Abrir la ventana del nivel 1, fusionar funcion de guardado a precionar nivel 1
    """
    Esta funcion es para abrir una nueva ventana, que abre el mapa del nivel 1
    """
    global c1,nvl1,mapa,a,y,x,z,gaso,lbl3,y2,j2,j2txt,fight,menos,ref1,ref2,x2
    nvl1 = tkinter.Toplevel(w0)#crear la ventana del nivel 1
    w0.iconify()
    nvl1.geometry("1200x850")#dimensiones de la ventana
    c1=tkinter.Canvas(nvl1,bg="gold", width=1600, height=800)#canvas del nivel
    c1.pack()
    y=c1.create_image(400,400,image=mapa)
    y2=c1.create_image(845,400,image=mapa)
    c1.lower(y)
    c1.lower(y2)#poner mapa atras
    # Liga el evento key al canvas
    #c1.bind("<Key>", key)
    c1.bind("<KeyPress>", keydown)
    c1.bind("<KeyRelease>", keyup)
    c1.focus_set()    
    #label gasolina, jugadores, puntos
    lbl3=tkinter.Label(nvl1,textvariable= gaso, underline=True,font=("",16,"bold")).place(x=50,y=62)
    lbljugador1=tkinter.Label(nvl1,text=j1.get(),font=("Arial",14)).place(x=50,y=10)
    lbljugador2=tkinter.Label(nvl1,text=j2.get(),font=("Arial",14)).place(x=50,y=400)
    lblpuntos=tkinter.Label(nvl1,textvariable=puntos,font=("",16,"bold")).place(x=50,y=100)
    lblvelocidad=tkinter.Label(nvl1,textvariable=velocidad,font=("",16,"bold")).place(x=50,y=130)
    ##cargar imagenes de los player y enemigos
    x = c1.create_image(400+i,750+j,image=carro)#imagen carro
    a=c1.create_image(400,170,image=runner)#imagen runner
    z=c1.create_image(500,-50,image=minivan)#imagen minivan
    fight=c1.create_image(500,50,image=fighter)#imagen fighter
    ref1=c1.create_image(550,70,image=referencia)
    x2=c1.create_image(830,750,image=carro)#imagen carro 2
    min2=c1.create_image(830,30,image=minivan)
    #ref2=c1.create_image(245,70,image=referencia)
    ##cargar funciones
    velocidadd()
    puntoss()
    runer()
    mini()
    gasolina()
    fondito()
    fondito2()
    fighterr()
    keyy()
###contadores    
contgaso=60
contpuntos=0
contvelocidad=0
####### Gasolina
def gasolina():
    """
    con esta funcion se crea el label de la gasolina
    """
    global gaso,nvl1,lbl3,contgaso
    
    
    if(contgaso>=0):
        gaso.set(str(contgaso))
        contgaso=contgaso-1
    c1.after(1000,gasolina)
    #if(contgaso<0):
        #nvl1.destroy()
    
####puntos
def puntoss():
    """
    control de puntos
    """
    global nvl1,contpuntos,puntos,lblpuntos
    if(contpuntos>=0):
        puntos.set(str(contpuntos))
        contpuntos=contpuntos+1
    c1.after(10,puntoss)

####velocidad
def velocidadd():
    """
    funcion para el label de velocidad
    """
    global nvl1,contvelocidad,velocidad,lblvelocidad
    if(contvelocidad>=0 and contvelocidad<=180):
        velocidad.set(str(contvelocidad))
        contvelocidad=contvelocidad+1
    c1.after(100,velocidadd)
h = []        
#####mover player    
##def key(event): #teclas para mover el jugador
##    """
##    """
##    global x,i,j,y,i2,x2,h
##    tecla = repr(event.char)
##    #print(tecla)
##    if(tecla == "'d'"):
##        if(i < 150):
##            c1.delete(x)
##            i = i + 10
##            x = c1.create_image(400+i,750+j,image=carro)   
##        else:
##            c1.delete(x)
##            x = c1.create_image(400+i,750+j,image=carroc)            
##    if(tecla == "'a'"):
##        if(i > -140):
##            c1.delete(x)
##            i = i - 10
##            x = c1.create_image(400+i,750+j,image=carro)
##        else:
##            c1.delete(x)
##            x = c1.create_image(400+i,750+j,image=carroc)
##    if(tecla=="'l'"):
##        if(i2 < 145):
##            c1.delete(x2)
##            i2 = i2 + 10
##            x2 = c1.create_image(830+i2,750+j,image=carro)
##            
##        else:
##            c1.delete(x2)
##            x2 = c1.create_image(830+i2,750+j,image=carroc)
##    if(tecla == "'j'"):
##        if(i2 > -130):
##            c1.delete(x2)
##            i2 = i2 - 10
##            x2 = c1.create_image(830+i2,750+j,image=carro)
##        else:
##            c1.delete(x2)
##            x2 = c1.create_image(830+i2,750+j,image=carroc)
    
def keyup(e):
    global h
    #print(e.keycode)
    if(e.keycode in h):
        h.pop(h.index(e.keycode))

def keydown(e):
    global h
    if not e.keycode in h:
        h.append(e.keycode)
def keyy():
    global h,x,i,j,y,i2,x2
    if(68 in h):
        if(i<150):
            c1.delete(x)
            i = i + 3
            x = c1.create_image(400+i,750+j,image=carro)
        else:
            c1.delete(x)
            x = c1.create_image(400+i,750+j,image=carroc) 
    if(65 in h):
        if(i > -140):
            c1.delete(x)
            i = i - 3
            x = c1.create_image(400+i,750+j,image=carro)
        else:
            c1.delete(x)
            x = c1.create_image(400+i,750+j,image=carroc)
    if(76 in h):
        if(i2 < 150):
            c1.delete(x2)
            i2 = i2 + 3
            x2 = c1.create_image(830+i2,750+j,image=carro)
        else:
            c1.delete(x2)
            x2 = c1.create_image(830+i2,750+j,image=carroc)
    if(74 in h):
        if(i2 > -130):
             c1.delete(x2)
             i2 = i2 - 3
             x2 = c1.create_image(830+i2,750+j,image=carro)
        else:
             c1.delete(x2)
             x2 = c1.create_image(830+i2,750+j,image=carroc)
     
             
    
        
    nvl1.after(10,keyy)
####mover player

####enemigo runner
def runer():#mover runner
    """
    """
    global a,ref1
    menosruner=random.randint(280,500)
    if(c1.coords(a)[0]<c1.coords(ref1)[0]):
        c1.move(a,0.5,0.5)
    if(c1.coords(a)[0]>=c1.coords(ref1)[0]):
        c1.move(a,-0.5,0.5)
        c1.move(ref1,-50,70)
    #if(c1.coords(a)[0]>c1.coords(ref2)[0]):
        #c1.move(a,-0.5,0.5)
    #if(c1.coords(a)[0]<1000):
        #c1.move(a,-0.5,1)
    nvl1.after(10,runer)
    
##    if(c2<190):
##        c2=c2+1
##        c1.move(a,1,0.3)
##   
##    if(c2>=190 and c2<515):
##        c1.move(a,-0.6,0.1)
##  
##        c2=c2+0.5
##    if(c2>=515 and c2<800):
##        c1.move(a,0.4,0.1)
##    
##        c2=c2+0.3
##    if(c2>=800 and c2<1085):
##        c1.move(a,-0.4,0.1)
##       
##        c2=c2+0.3
##    if(c2>=1085 and c2<1375):
##        c1.move(a,0.4,0.1)
##      
##        c2=c2+0.3
##    if(c2>=1375 and c2<1580):
##        c1.move(a,-0.4,0.1)
##        
##        c2=c2+0.3
##    if(c2>=1580):
##        c1.move(a,400-c1.coords(a)[0],-c1.coords(a)[1])
##        c2=0
##    nvl1.after(1,runer) 
###enemigo runner

###enemigo minivan

def mini():#mover minivan
    """
    """
    
    global nvl1,y,p,c,z,c1,contadormini,x,contgaso,contvelocidad
    menos=random.randint(280,500)
    if(c<400):
        c1.move(z,0,2)
        c = c + 1
        
    if(c==400):
        #c1.delete(z)
        c = 0
        c1.move(z,menos-c1.coords(z)[0],-c1.coords(z)[1])
        #z=c1.create_image(500,-50,image=minivan)

    if(contadormini<950):#250
        
        contadormini = contadormini + 1
        posx1 = c1.coords(x)[0]
        posy1 = c1.coords(x)[1]
        posx2 = c1.coords(z)[0]
        posy2 = c1.coords(z)[1]
        
        #posx1 <= posx2 and posx2+37 <= posx1 and posy1<= posy2 and posy2 <= posy1 + 50

        if(posx1>=posx2 and posx1<=posx2+28 and posy1>=posy2 and posy1<=posy2+50 or(posx1+28>=posx2 and posx1+28<=posx2+28 and posy1>=posy2 and posy1<=posy2+50) ):
            print("crash")
            l=x
            x = c1.create_image(c1.coords(l)[0],c1.coords(l)[1],image=carroc)
            c1.delete(l)
            c1.move(z,menos-c1.coords(z)[0],-c1.coords(z)[1])
            nvl1.after(10,mini)
            contgaso=contgaso-2
            contvelocidad=0
        else:
            contadormini=0
            nvl1.after(10,mini)
            
###enemigo minivan
###mover fondo
def fondito():
    """
    """
    global c1,nvl1
    c22=0
    c32=0
    if(c22<5):
        c1.move(y,0,0.8)
        c22=c22+1
        c32=c32+1
    if(c1.coords(y)[1]>=10000):
        c22=0
        c1.move(y,0,-c1.coords(y)[1])
    nvl1.after(1,fondito)
    
        
def fondito2():
    """
    """
    global c1,nvl1
    c222=0
    c322=0
    if(c222<5):
        c1.move(y2,0,0.8)
        c222=c222+1
        c322=c322+1
        
    if(c1.coords(y2)[1]>=10000):
        c222=0
        c1.move(y2,0,-c1.coords(y)[1])
    nvl1.after(1,fondito2)
###mover fondo
###enemigo fighter
def fighterr():
    """
    esta funcion es para mover el fighter
    """
    
    global fight,reloadfighter,x,contgaso,contvelocidad,y
    menosfighter=random.randint(280,500)
    if(c1.coords(x)[0]<c1.coords(fight)[0]):
        c1.move(fight,-0.5,2)
    elif(c1.coords(x)[0]>c1.coords(fight)[0]):
        c1.move(fight,0.5,2)
    else:
        c1.move(fight,0,2)
    if(c1.coords(x)[1]==c1.coords(fight)[1]):
        c1.move(fight,menosfighter-c1.coords(fight)[0],-c1.coords(fight)[1])
        #fight=c1.create_image(500,50,image=fighter)
        
    if(reloadfighter<950):#250
        
        reloadfighter = reloadfighter + 1
        posx11 = c1.coords(x)[0]
        posy11 = c1.coords(x)[1]
        posx22 = c1.coords(fight)[0]
        posy22 = c1.coords(fight)[1]
        
        #posx1 <= posx2 and posx2+37 <= posx1 and posy1<= posy2 and posy2 <= posy1 + 50

        if(posx11>=posx22 and posx11<=posx22+28 and posy11>=posy22 and posy11<=posy22+50 or(posx11+28>=posx22 and posx11+28<=posx22+28 and posy11>=posy22 and posy11<=posy22+50) ):
            print("crash")
            l=x
            x = c1.create_image(c1.coords(l)[0],c1.coords(l)[1],image=carroc)
            c1.delete(l)
            c1.move(fight,menosfighter-c1.coords(fight)[0],-c1.coords(fight)[1])
            nvl1.after(10,fighterr)
            contgaso=contgaso-2
            contvelocidad=0
            c1.move(y,0,-c1.coords(y)[1])
        else:
            reloadfighter=0
            nvl1.after(10,fighterr)
        
        
    
###enemigo fighter
#####-------------------------------------------------------------------------------------------------- nivel 1






####------------------------------------------------------------------------------------------------------nivel 2
##imagenes
mapa2=tkinter.PhotoImage(file="2lvl2.png")#imagen del mapa
carro2 = tkinter.PhotoImage(file="c11.png")#el jugador
carroc2=tkinter.PhotoImage(file="c11chocado.png")#imagen choque
runner2=tkinter.PhotoImage(file="c22.png")#imagen del runner
minivan2=tkinter.PhotoImage(file="c33.png")#imagen del minivan
##imagenes

   
def nivel2(): # Abrir la ventana del nivel 2, fusionar funcion de guardado a precionar nivel 2
    """
    Esta funcion es para abrir una nueva ventana, que abre el mapa del nivel 2
    """
    global can2,nvl2,mapa2,xlvlx
    nvl2 = tkinter.Toplevel(w0)#crear la ventana del nivel 2
    w0.iconify()
    nvl2.geometry("800x800")#dimensiones de la ventana
    can2=tkinter.Canvas(nvl2, width=800, height=800)#canvas del nivel 2
    can2.pack()
    xlvlx=can2.create_image(400,400,image=mapa2)#mapa del nivel 2
    can2.lower(xlvlx)

####---------------------------------------------------------------------------------------------------nivel 2
def nivel3(): # Abrir la ventana del nivel 3, fusionar funcion de guardado a precionar nivel 3
    """
    Esta funcion es para abrir una nueva ventana, que abre el mapa del nivel 3
    """
    nvl3 = tkinter.Tk()

    
def nivel4(): # Abrir la ventana del nivel 4, fusionar funcion de guardado a precionar nivel 4
    """
    Esta funcion es para abrir una nueva ventana, que abre el mapa del nivel 4
    """
    nvl4 = tkinter.Tk()


    
def nivel5(): # Abrir la ventana del nivel 5, fusionar funcion de guardado a precionar nivel 5
    """
    Esta funcion es para abrir una nueva ventana, que abre el mapa del nivel 4
    """
    nvl5 = tkinter.Tk()

##botones
b1=tkinter.Button(w0,text="Nivel 1",font=("Arial",14),command=nivel1).place(x=600,y=10) #Boton nvl1
b2=tkinter.Button(w0,text="Nivel 2",font=("Arial",14),command=nivel2).place(x=600,y=60) #Boton nvl2
b3=tkinter.Button(w0,text="Nivel 3",font=("Arial",14),command=nivel3).place(x=600,y=110) #Boton nvl3
b4=tkinter.Button(w0,text="Nivel 4",font=("Arial",14),command=nivel4).place(x=600,y=160)  #Boton nvl4
b5=tkinter.Button(w0,text="Nivel 5",font=("Arial",14),command=nivel5).place(x=600,y=210) #Boton nvl5



w0.mainloop()
nvl1.mainloop()
nvl2.mainloop()
nvl3.mainloop()
nvl4.mainloop()
nvl5.mainloop()
