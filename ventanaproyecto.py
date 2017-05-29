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
lblfondo1=tkinter.Label(w0,text="Jugador 1: ",fg="white",bg="black",font=("Verdana",12)).place(x=10,y=10)

#jugador 1 campo

j1=tkinter.StringVar()
j1.set("")
j1txt=tkinter.Entry(w0,textvariable=j1).place(x=120,y=10)

#campo de entrada label jugador 2
lblfondo2=tkinter.Label(w0,text="Jugador 2: ",fg="white",bg="black",font=("verdana",12)).place(x=10,y=40)

#para jugar 
lblfondo3=tkinter.Label(w0,text="Jugar :",fg="white",bg="black",font=("Verdana",12)).place(x=500,y=40)
lblfondo4=tkinter.Label(w0,text="Partidas Guardadas",fg="white",bg="black",font=("Verdana",12)).place(x=100,y=300)
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
gaso22=tkinter.StringVar()#label gasolina 2 mapa
puntos=tkinter.StringVar()#label de los puntos
puntos22=tkinter.StringVar()#puntos mapa 2
velocidad=tkinter.StringVar()#label de la velocidad
velocidad22=tkinter.StringVar()#velocidad 2
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
mancha=tkinter.PhotoImage(file="manchita.png")#Aceite
imagengasolina=tkinter.PhotoImage(file="nyan13.png")#gasolina
gana1=tkinter.PhotoImage(file="1WIN.png")
##imagenes

def nivel1(): # Abrir la ventana del nivel 1, fusionar funcion de guardado a precionar nivel 1
    """
    Esta funcion es para abrir una nueva ventana, que abre el mapa del nivel 1
    """
    global c1,nvl1,mapa,a,y,x,z,gaso,lbl3,y2,j2,j2txt,fight,menos,ref1,ref2,x2,min2,aceite,fight2,gaso22,puntos22,velocidad22,run2,aceite2,nyan,nyan2
    nvl1 = tkinter.Toplevel(w0)#crear la ventana del nivel 1
    w0.iconify()
    nvl1.geometry("1200x850")#dimensiones de la ventana
    c1=tkinter.Canvas(nvl1,bg="black", width=1600, height=800)#canvas del nivel
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
    lbl3=tkinter.Label(nvl1,textvariable= gaso,fg="white",bg="black", underline=True,font=("",16,"bold")).place(x=50,y=62)#GASOLINA 1
    lblgaso2=tkinter.Label(nvl1,textvariable= gaso22,fg="white",bg="black", underline=True,font=("",16,"bold")).place(x=50,y=430)#gasolina 2
    lbljugador1=tkinter.Label(nvl1,text=j1.get(),fg="white",bg="black",font=("Arial",14)).place(x=50,y=10)
    lbljugador2=tkinter.Label(nvl1,text=j2.get(),fg="white",bg="black",font=("Arial",14)).place(x=50,y=400)
    lblpuntos=tkinter.Label(nvl1,textvariable=puntos,fg="white",bg="black",font=("",16,"bold")).place(x=50,y=100)#puntos 1
    lblpuntos2=tkinter.Label(nvl1,textvariable=puntos22,fg="white",bg="black",font=("",16,"bold")).place(x=50,y=460)#puntos 2
    lblvelocidad=tkinter.Label(nvl1,textvariable=velocidad,fg="white",bg="black",font=("",16,"bold")).place(x=50,y=130)# velocidad 1
    lblvelocidad2=tkinter.Label(nvl1,textvariable=velocidad22,fg="white",bg="black",font=("",16,"bold")).place(x=50,y=490)#velocidad 2
    ##cargar imagenes de los player y enemigos
    x = c1.create_image(400,750,image=carro)#imagen carro
    a=c1.create_image(400,170,image=runner)#imagen runner
    run2=c1.create_image(720,70,image=runner)#imagen runner 2
    z=c1.create_image(500,-50,image=minivan)#imagen minivan
    fight=c1.create_image(500,50,image=fighter)#imagen fighter
    nyan=c1.create_image(450,50,image=imagengasolina)#nyan 1
    nyan2=c1.create_image(770,50,image=imagengasolina)#nyan 2
    x2=c1.create_image(830,750,image=carro)#imagen carro 2
    min2=c1.create_image(830,-50,image=minivan)#minivan dos
    aceite=c1.create_image(480,30,image=mancha)#aceite del 1
    aceite2=c1.create_image(830,30,image=mancha)#aceite del 2
    fight2=c1.create_image(750,50,image=fighter)#fighter 2
    #nyan2=c1.create_image(740,50,image=poder)
    ##cargar funciones
    gasolina()
    gasolina22()
    mini2()
    fighterr2()
    manchita()
    manchita22()
    velocidadd()
    velocidadd22()
    puntoss()
    puntoss22()
    runer()
    runer22()
    mini()
    fondito()
    fondito2()
    fighterr()
    poder()
    poder22()
    keyy()
###contadores    
contgaso=60
contgaso22=60
contpuntos=0
contpuntos22=0
contvelocidad=0
contvelocidad22=0
contaceite=0
contaceite2=0
resbalar=0
resbalar2=0
c2player=0
contadormini2=0
reloadfighter2=0
contadorruner=0
contadorruner2=0
contadorpoder=0
reloadpoder=0
contadorpoder2=0
reloadpoder2=0
####### Gasolina
def gasolina():
    """
    con esta funcion se crea el label de la gasolina
    """
    global gaso,nvl1,lbl3,contgaso,gana1
    
    
    if(contgaso>0):
        gaso.set(str(contgaso)+" "+"G")
        contgaso=contgaso-1
    c1.after(1000,gasolina)
    if(contgaso==0):
        nvl1.destroy()
        
    
        print("2 win")
def gasolina22():
    """
    con esta funcion se crea el label de la gasolina
    """
    global gaso22,nvl1,contgaso22
    
    
    if(contgaso22>0):
        gaso22.set(str(contgaso22)+" "+"G")
        contgaso22=contgaso22-1
    c1.after(1000,gasolina22)
    if(contgaso22==0):
        nvl1.destroy()

        print("1 win")


    
####puntos
def puntoss():
    """
    control de puntos
    """
    global nvl1,contpuntos,puntos,lblpuntos
    if(contpuntos>=0):
        puntos.set(str(contpuntos)+" "+"M")
        contpuntos=contpuntos+1
    c1.after(10,puntoss)

def puntoss22():
    """
    control de puntos
    """
    global nvl1,contpuntos22,puntos22,lblpuntos
    if(contpuntos22>=0):
        puntos22.set(str(contpuntos22)+" "+"M")
        contpuntos22=contpuntos22+1
    c1.after(10,puntoss22)

####velocidad
def velocidadd():
    """
    funcion para el label de velocidad
    """
    global nvl1,contvelocidad,velocidad,lblvelocidad
    if(contvelocidad>=0 and contvelocidad<=180):
        velocidad.set(str(contvelocidad)+" "+"KM/H")
        contvelocidad=contvelocidad+1
    c1.after(100,velocidadd)
def velocidadd22():
    """
    funcion para el label de velocidad
    """
    global nvl1,contvelocidad22,velocidad22,lblvelocidad
    if(contvelocidad22>=0 and contvelocidad22<=180):
        velocidad22.set(str(contvelocidad22)+" "+"KM/H")
        contvelocidad22=contvelocidad22+1
    c1.after(100,velocidadd22)

###velocidad 
h = []        
#####mover player    

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
        
    if(65 in h):
        if(i > -140):
            c1.delete(x)
            i = i - 3
            x = c1.create_image(400+i,750+j,image=carro)
        
    if(76 in h):
        if(i2 < 160):
            c1.delete(x2)
            i2 = i2 + 3
            x2 = c1.create_image(830+i2,750+j,image=carro)
        
    if(74 in h):
        if(i2 > -130):
             c1.delete(x2)
             i2 = i2 - 3
             x2 = c1.create_image(830+i2,750+j,image=carro)
      
    if(32 in h):
         
         guardar()
                      
             
    
        
    nvl1.after(10,keyy)
####mover player
###------------------------------------------------guardar y cargar
def guardar():
    """
    """
    global h,x,j,i,y,i2,x2,contgaso,contgaso22,contpuntos,contpuntos22,archivo,c1
    archivo = open("partida.txt", "w")
    posix1=c1.coords(x)[0]
    posix11=c1.coords(x)[1]
    posix2=c1.coords(x2)[0]
    posix22=c1.coords(x2)[1]
    if(contgaso>0 and contgaso22>0):  
            archivo.write(str(contgaso)+"\n")
            archivo.write(str(contpuntos)+"\n")
            archivo.write(str(contgaso22)+"\n")
            archivo.write(str(contpuntos22)+"\n")
            archivo.write(str(posix1)+"\n")
            archivo.write(str(posix11)+"\n")
            archivo.write(str(posix2)+"\n")
            archivo.write(str(posix22)+"\n")
    
    
    archivo.close()
   
    
def cargar():
    """
    """
    global h,x,j,i,y,i2,x2,contgaso,contgaso22,contpuntos,contpuntos22,archivo,c1
    archivo=open("partida.txt","r")
    
    linea1 = archivo.readline()
    print(linea1)
    linea2=archivo.readline()
    print(linea2)
    linea3 = archivo.readline()
    print(linea3)
    linea4=archivo.readline()
    print(linea4)
    linea5 = archivo.readline()
    print(linea5)
    linea6=archivo.readline()
    print(linea6)
    linea7 = archivo.readline()
    print(linea7)
    linea8=archivo.readline()
    print(linea8)
    nivel1()
    juga1=c1.coords(x)[0]
    juga11=c1.coords(x)[1]
    juga2=c1.coords(x2)[0]
    juga22=c1.coords(x2)[1]
    contgaso=int(linea1)
    contpuntos=int(linea2)
    contgaso22=int(linea3)
    contpuntos22=int(linea4)
    juga1=float(linea5)
    juga11=float(linea6)
    juga2=float(linea7)
    juga22=float(linea8)
    
    archivo.close()

###------------------------------------------------guardar y cargar

##------------------------------------------------------------gasolina
def poder ():
    """
    esta funcion es para mover el gato de la gasolina
    """
    global nvl1,y,p,c,z,c1,contadormini,x,contgaso,contvelocidad,contadorpoder,reloadpoder,nyan
    menospoder=random.randint(280,500)
    if(contadorpoder<500):
        c1.move(nyan,0,5)
        contadorpoder = contadorpoder + 1
        
    if(contadorpoder==500):
        contadorpoder=0
        c1.move(nyan,menospoder-c1.coords(nyan)[0],-c1.coords(nyan)[1])

    if(reloadpoder<950):#250
        
        reloadpoder = reloadpoder + 1
        posx1ny = c1.coords(x)[0]
        posy1ny = c1.coords(x)[1]
        posx2ny = c1.coords(nyan)[0]
        posy2ny = c1.coords(nyan)[1]
        
        #posx1 <= posx2 and posx2+37 <= posx1 and posy1<= posy2 and posy2 <= posy1 + 50

        if(posx1ny>=posx2ny and posx1ny<=posx2ny+28 and posy1ny>=posy2ny and posy1ny<=posy2ny+50 or(posx1ny+28>=posx2ny and posx1ny+28<=posx2ny+28 and posy1ny>=posy2ny and posy1ny<=posy2ny+50) ):
            print("crash")
            c1.move(nyan,menospoder-c1.coords(nyan)[0],c1.coords(nyan)[1]-500)
            nvl1.after(10,poder)
            contgaso=contgaso+2
            contadorpoder=0
        else:
            reloadpoder=0
            nvl1.after(10,poder)
    
def poder22 ():
    """
    esta funcion es para mover el gato de la gasolina
    """
    global nvl1,y,p,c,z,c1,contadormini,x,contgaso22,contvelocidad,contadorpoder2,reloadpoder2,nyan2
    menospoder2=random.randint(700,980)
    if(contadorpoder2<500):
        c1.move(nyan2,0,5)
        contadorpoder2 = contadorpoder2 + 1
        
    if(contadorpoder2==500):
        contadorpoder2=0
        c1.move(nyan2,menospoder2-c1.coords(nyan2)[0],-c1.coords(nyan2)[1])

    if(reloadpoder2<950):#250
        
        reloadpoder2 = reloadpoder2 + 1
        posx1ny2 = c1.coords(x2)[0]
        posy1ny2 = c1.coords(x2)[1]
        posx2ny2 = c1.coords(nyan2)[0]
        posy2ny2 = c1.coords(nyan2)[1]
        
        #posx1 <= posx2 and posx2+37 <= posx1 and posy1<= posy2 and posy2 <= posy1 + 50

        if(posx1ny2>=posx2ny2 and posx1ny2<=posx2ny2+28 and posy1ny2>=posy2ny2 and posy1ny2<=posy2ny2+50 or(posx1ny2+28>=posx2ny2 and posx1ny2+28<=posx2ny2+28 and posy1ny2>=posy2ny2 and posy1ny2<=posy2ny2+50) ):
            print("crash")
            c1.move(nyan2,menospoder2-c1.coords(nyan2)[0],c1.coords(nyan2)[1]-500)
            nvl1.after(10,poder22)
            contgaso22=contgaso22+2
            contadorpoder2=0
        else:
            reloadpoder2=0
            nvl1.after(10,poder22)    

##-------------------------------------------------------------gasolina
direccion=1
direccion2=1
####enemigo runner
def runer():#mover runner
    """
    esta funcion es para mover el runer
    """
    global a,ref1,direccion,contgaso,contvelocidad,contadorruner,x
    menosruner=random.randint(280,500)
    if(c1.coords(a)[0]>=250):
            direccion=direccion*(-1)
            
    if(c1.coords(a)[0]<=550):
            direccion=direccion*(-1)
    if(c1.coords(x)[1]==c1.coords(a)[1]):
        c1.move(a,menosruner-c1.coords(a)[0],-c1.coords(a)[1])
    c1.move(a,direccion*1,1)
    #nvl1.after(10,runer)
    if(contadorruner<950):#250
        
        contadorruner = contadorruner + 1
        posx1r = c1.coords(x)[0]
        posy1r = c1.coords(x)[1]
        posx2r = c1.coords(a)[0]
        posy2r = c1.coords(a)[1]
        
        #posx1 <= posx2 and posx2+37 <= posx1 and posy1<= posy2 and posy2 <= posy1 + 50

        if(posx1r>=posx2r and posx1r<=posx2r+28 and posy1r>=posy2r and posy1r<=posy2r+50 or(posx1r+28>=posx2r and posx1r+28<=posx2r+28 and posy1r>=posy2r and posy1r<=posy2r+50) ):
            print("crash")
            l=x
            x = c1.create_image(c1.coords(l)[0],c1.coords(l)[1],image=carroc)
            c1.delete(l)
            c1.move(a,menosruner-c1.coords(a)[0],-c1.coords(a)[1])
            nvl1.after(10,runer)
            contgaso=contgaso-2
            contvelocidad=0
            c1.move(y,0,-c1.coords(y)[1])
        else:
            contadorruner=0
            nvl1.after(10,runer)
    


def runer22():
    """
runer del nivel 2
    """
    global run2,ref1,direccion2,contadorruner2,x2,contgaso22,contvelocidad22
    menosruner2=random.randint(700,980)
    if(c1.coords(run2)[0]>=700):
            direccion2=direccion2*(-1)
            
    if(c1.coords(run2)[0]<=980):
            direccion2=direccion2*(-1)
    if(c1.coords(x)[1]==c1.coords(run2)[1]):
        c1.move(run2,menosruner2-c1.coords(run2)[0],-c1.coords(run2)[1])
    c1.move(run2,direccion2*1,1)
    if(contadorruner<950):#250
        
        contadorruner2 = contadorruner2 + 1
        posx1r2 = c1.coords(x2)[0]
        posy1r2 = c1.coords(x2)[1]
        posx2r2 = c1.coords(run2)[0]
        posy2r2 = c1.coords(run2)[1]
        
        #posx1 <= posx2 and posx2+37 <= posx1 and posy1<= posy2 and posy2 <= posy1 + 50

        if(posx1r2>=posx2r2 and posx1r2<=posx2r2+28 and posy1r2>=posy2r2 and posy1r2<=posy2r2+50 or(posx1r2+28>=posx2r2 and posx1r2+28<=posx2r2+28 and posy1r2>=posy2r2 and posy1r2<=posy2r2+50) ):
            print("crash")
            l4=x2
            x2 = c1.create_image(c1.coords(l4)[0],c1.coords(l4)[1],image=carroc)
            c1.delete(l4)
            c1.move(run2,menosruner2-c1.coords(run2)[0],-c1.coords(run2)[1])
            nvl1.after(10,runer22)
            contgaso22=contgaso22-2
            contvelocidad22=0
            c1.move(y2,0,-c1.coords(y2)[1])
        else:
            contadorruner2=0
            nvl1.after(10,runer22)
    
###enemigo runner

###enemigo minivan--------------------------------------------------------------------------

def mini():#mover minivan
    """
    Esta funcion mueve la minivan
    """
    
    global nvl1,y,p,c,z,c1,contadormini,x,contgaso,contvelocidad
    menos=random.randint(280,500)
    if(c<430):
        c1.move(z,0,2.5)
        c = c + 1
        
    if(c==430):
        #c1.delete(z)
        
        c1.move(z,menos-c1.coords(z)[0],-c1.coords(z)[1])
        c = 0
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
            c=0
            c1.move(y,0,-c1.coords(y)[1])
        else:
            contadormini=0
            nvl1.after(10,mini)
def mini2():
    """
    Esta funcion mueve la minivan del segundo mapa
    """
    
    global nvl1,y,p,c2player,c1,contadormini2,x2,contgaso22,contvelocidad22,min2
    menos2=random.randint(700,970)
    if(c2player<400):
        c1.move(min2,0,2.5)
        c2player = c2player + 1
        
    if(c2player==400):
        #c1.delete(z)
        c1.move(min2,menos2-c1.coords(min2)[0],-c1.coords(min2)[1])
        c2player = 0
        #z=c1.create_image(500,-50,image=minivan)

    if(contadormini2<950):#250
        
        contadormini2 = contadormini2 + 1
        posx1m = c1.coords(x2)[0]
        posy1m = c1.coords(x2)[1]
        posx2m = c1.coords(min2)[0]
        posy2m = c1.coords(min2)[1]
        
        #posx1 <= posx2 and posx2+37 <= posx1 and posy1<= posy2 and posy2 <= posy1 + 50

        if(posx1m>=posx2m and posx1m<=posx2m+28 and posy1m>=posy2m and posy1m<=posy2m+50 or(posx1m+28>=posx2m and posx1m+28<=posx2m+28 and posy1m>=posy2m and posy1m<=posy2m+50) ):
            print("crash")
            l3=x2
            x2 = c1.create_image(c1.coords(l3)[0],c1.coords(l3)[1],image=carroc)
            c1.delete(l3)
            c1.move(min2,menos2-c1.coords(min2)[0],-c1.coords(min2)[1])
            nvl1.after(10,mini2)
            contgaso22=contgaso22-2
            contvelocidad22=0
            c2player=0
            c1.move(y2,0,-c1.coords(y2)[1])
        else:
            contadormini2=0
            nvl1.after(10,mini2)
    
            
###enemigo minivan-----------------------------------------------------------------------------------
###aceite
def manchita():#mover minivan
    """
    mancha de aceite
    """
    
    global nvl1,y,p,c,z,c1,contadormini,x,contgaso,contvelocidad,aceite,contaceite,resbalar
    menosaceite=random.randint(280,500)
    if(contaceite<400):
        c1.move(aceite,0,2)
        contaceite = contaceite + 1
        
    if(contaceite==400):
        #c1.delete(z)
        c1.move(aceite,menosaceite-c1.coords(aceite)[0],-c1.coords(aceite)[1])
        contaceite = 0

    if(resbalar<950):#250
        
        resbalar = resbalar + 1
        posx1x = c1.coords(x)[0]
        posy1x = c1.coords(x)[1]
        posx2a = c1.coords(aceite)[0]
        posy2a = c1.coords(aceite)[1]
        
        #posx1 <= posx2 and posx2+37 <= posx1 and posy1<= posy2 and posy2 <= posy1 + 50

        if(posx1x>=posx2a and posx1x<=posx2a+28 and posy1x>=posy2a and posy1x<=posy2a+50 or(posx1x+28>=posx2a and posx1x+28<=posx2a+28 and posy1x>=posy2a and posy1x<=posy2a+50) ):
            print("crash")
            l1=x
            c1.move(l1,-80,0)
            x = c1.create_image(c1.coords(l1)[0],c1.coords(l1)[1],image=carroc)
            c1.delete(l1)
            c1.move(aceite,menosaceite-c1.coords(aceite)[0],-c1.coords(aceite)[1])
            contgaso=contgaso-2
            contvelocidad=0
            contaceite=0
            c1.move(y,0,-c1.coords(y)[1])
            nvl1.after(10,manchita)
        else:
            resbalar=0
            nvl1.after(10,manchita)
            
def manchita22():#mover minivan
    """
    mancha de aceite 2
    """
    
    global nvl1,y,p,c1,x2,contgaso22,contvelocidad22,aceite2,contaceite2,resbalar2
    menosaceite2=random.randint(700,970)
    if(contaceite2<400):
        c1.move(aceite2,0,2)
        contaceite2 = contaceite2 + 1
        
    if(contaceite2==400):
        #c1.delete(z)
        c1.move(aceite2,menosaceite2-c1.coords(aceite2)[0],-c1.coords(aceite2)[1])
        contaceite2 = 0

    if(resbalar2<950):#250
        
        resbalar2 = resbalar2 + 1
        posx1xm2 = c1.coords(x2)[0]
        posy1xm2 = c1.coords(x2)[1]
        posx2am2 = c1.coords(aceite2)[0]
        posy2am2 = c1.coords(aceite2)[1]
        
        #posx1 <= posx2 and posx2+37 <= posx1 and posy1<= posy2 and posy2 <= posy1 + 50

        if(posx1xm2>=posx2am2 and posx1xm2<=posx2am2+28 and posy1xm2>=posy2am2 and posy1xm2<=posy2am2+50 or(posx1xm2+28>=posx2am2 and posx1xm2+28<=posx2am2+28 and posy1xm2>=posy2am2 and posy1xm2<=posy2am2+50) ):
            print("crash")
            l13=x2
            c1.move(l13,-80,0)
            x2 = c1.create_image(c1.coords(l13)[0],c1.coords(l13)[1],image=carroc)
            c1.delete(l13)
            c1.move(aceite2,menosaceite2-c1.coords(aceite2)[0],-c1.coords(aceite2)[1])
            nvl1.after(10,manchita22)
            contgaso22=contgaso22-2
            contvelocidad22=0
            contaceite2=0
            c1.move(y2,0,-c1.coords(y2)[1])
        else:
            resbalar2=0
            nvl1.after(10,manchita22)

###aceite
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
        c1.move(y2,0,-c1.coords(y2)[1])
    nvl1.after(1,fondito2)
###mover fondo
###enemigo fighter---------------------------------------------------------------------------------------
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
            l2=x
            x = c1.create_image(c1.coords(l2)[0],c1.coords(l2)[1],image=carroc)
            c1.delete(l2)
            c1.move(fight,menosfighter-c1.coords(fight)[0],-c1.coords(fight)[1])
            nvl1.after(10,fighterr)
            contgaso=contgaso-2
            contvelocidad=0
            c1.move(y,0,-c1.coords(y)[1])
        else:
            reloadfighter=0
            nvl1.after(10,fighterr)

def fighterr2():
    """
    esta funcion es para mover el fighter
    """
    
    global fight2,reloadfighter2,x2,contgaso22,contvelocidad22,y
    menosfighter2=random.randint(700,1000)
    if(c1.coords(x2)[0]<c1.coords(fight2)[0]):
        c1.move(fight2,-0.5,2)
    elif(c1.coords(x2)[0]>c1.coords(fight2)[0]):
        c1.move(fight2,0.5,2)
    else:
        c1.move(fight2,0,2)
    if(c1.coords(x2)[1]==c1.coords(fight2)[1]):
        c1.move(fight2,menosfighter2-c1.coords(fight2)[0],-c1.coords(fight2)[1])
        #fight=c1.create_image(500,50,image=fighter)
        
    if(reloadfighter2<950):#250
        
        reloadfighter2 = reloadfighter2 + 1
        posx11f = c1.coords(x2)[0]
        posy11f = c1.coords(x2)[1]
        posx22f= c1.coords(fight2)[0]
        posy22f = c1.coords(fight2)[1]
        
        #posx1 <= posx2 and posx2+37 <= posx1 and posy1<= posy2 and posy2 <= posy1 + 50

        if(posx11f>=posx22f and posx11f<=posx22f+28 and posy11f>=posy22f and posy11f<=posy22f+50 or(posx11f+28>=posx22f and posx11f+28<=posx22f+28 and posy11f>=posy22f and posy11f<=posy22f+50) ):
            print("crash")
            l22=x2
            x2 = c1.create_image(c1.coords(l22)[0],c1.coords(l22)[1],image=carroc)
            c1.delete(l22)
            c1.move(fight2,menosfighter2-c1.coords(fight2)[0],-c1.coords(fight2)[1])
            nvl1.after(10,fighterr2)
            contgaso22=contgaso22-2
            contvelocidad22=0
            c1.move(y2,0,-c1.coords(y2)[1])
        else:
            reloadfighter2=0
            nvl1.after(10,fighterr2)
        
        
    
###enemigo fighter-------------------------------------------------------------------------------------------------------------------------------
#####-------------------------------------------------------------------------------------------------- nivel 1






####------------------------------------------------------------------------------------------------------nivel 2
##imagenes
mapa2=tkinter.PhotoImage(file="mapa2222.png")#imagen del mapa
##imagenes

   
def nivel2(): # Abrir la ventana del nivel 2, fusionar funcion de guardado a precionar nivel 2
    """
    Esta funcion es para abrir una nueva ventana, que abre el mapa del nivel 2
    """
    global can2,nvl2,mapa2,x,x2,z,gaso,gaso22,puntos,puntos22,velocidad,min2,y,y2,a,run2,fight,fight2,aceite,aceite2,nyan,nyan2
    nvl2 = tkinter.Toplevel(w0)#crear la ventana del nivel 2
    w0.iconify()
    nvl2.geometry("1200x850")#dimensiones de la ventana
    can2=tkinter.Canvas(nvl2,bg="black", width=1600, height=800)#canvas del nivel 2
    can2.pack()
    y=can2.create_image(400,400,image=mapa2)#mapa del nivel 2
    y2=can2.create_image(847,400,image=mapa2)
    can2.lower(y)
    can2.lower(y2)
    #label gasolina, jugadores, puntos
    lbl3=tkinter.Label(nvl2,textvariable= gaso,fg="white",bg="black", underline=True,font=("",16,"bold")).place(x=50,y=62)#GASOLINA 1
    lblgaso2=tkinter.Label(nvl2,textvariable= gaso22,fg="white",bg="black", underline=True,font=("",16,"bold")).place(x=50,y=430)#gasolina 2
    lbljugador1=tkinter.Label(nvl2,text=j1.get(),fg="white",bg="black",font=("Arial",14)).place(x=50,y=10)
    lbljugador2=tkinter.Label(nvl2,text=j2.get(),fg="white",bg="black",font=("Arial",14)).place(x=50,y=400)
    lblpuntos=tkinter.Label(nvl2,textvariable=puntos,fg="white",bg="black",font=("",16,"bold")).place(x=50,y=100)#puntos 1
    lblpuntos2=tkinter.Label(nvl2,textvariable=puntos22,fg="white",bg="black",font=("",16,"bold")).place(x=50,y=460)#puntos 2
    lblvelocidad=tkinter.Label(nvl2,textvariable=velocidad,fg="white",bg="black",font=("",16,"bold")).place(x=50,y=130)# velocidad 1
    lblvelocidad2=tkinter.Label(nvl2,textvariable=velocidad22,fg="white",bg="black",font=("",16,"bold")).place(x=50,y=490)#velocidad 2
    ##cargar imagenes del player y los enemigos
    x= can2.create_image(400+i,750+j,image=carro)#imagen carro
    a=can2.create_image(400,170,image=runner)#imagen runner
    z=can2.create_image(500,-50,image=minivan)#imagen minivan
    fight=can2.create_image(500,50,image=fighter)#imagen fighter
    aceite=can2.create_image(480,30,image=mancha)#aceite del 1
    nyan=can2.create_image(450,50,image=imagengasolina)#nyan 1
    ##2 pantalla
    x2=can2.create_image(830,750,image=carro)#imagen carro 2
    nyan2=can2.create_image(770,50,image=imagengasolina)#nyan 2
    min2=can2.create_image(830,-50,image=minivan)#minivan dos
    fight2=can2.create_image(750,50,image=fighter)#fighter 2
    run2=can2.create_image(730,50,image=runner)#imagen runner
    aceite2=can2.create_image(770,30,image=mancha)#aceite del 1
    can2.bind("<KeyPress>", keydown)
    can2.bind("<KeyRelease>", keyup)
    can2.focus_set()
    #cargar funciones
    gasolinanvl2()
    gasolinanvl22()
    mininvl2()
    mininvl22()
    puntosnvl2()
    puntosnvl22()
    velocidadnvl2()
    velocidadnvl22()
    fonditonvl2()
    fonditonvl22()
    runernvl2()
    runernvl22()
    fighterrnvl2()
    fighterrnvl22()
    manchitanvl2()
    manchitanvl22()
    podernvl2()
    podernvl22()
    keyy2()  
###------------------------------------------------------------------------------------Players
def keyy2():
    global h, playernvl2,i,j,y,i2,x2,nvl2,playernvl22,x
    if(68 in h):
        if(i<150):
            can2.delete(x)
            i = i + 3
            x = can2.create_image(400+i,750+j,image=carro)
        #else:
            #c1.delete(x)
            #x = c1.create_image(400+i,750+j,image=carroc) 
    if(65 in h):
        if(i > -140):
            can2.delete(x)
            i = i - 3
            x = can2.create_image(400+i,750+j,image=carro)
        #else:
            #c1.delete(x)
            #x = c1.create_image(400+i,750+j,image=carroc)
    if(76 in h):
        if(i2 < 160):
            can2.delete(x2)
            i2 = i2 + 3
            x2 = can2.create_image(830+i2,750+j,image=carro)
        #else:
            #c1.delete(x2)
            #x2 = c1.create_image(830+i2,750+j,image=carroc)
    if(74 in h):
        if(i2 > -130):
             can2.delete(x2)
             i2 = i2 - 3
             x2 = can2.create_image(830+i2,750+j,image=carro)
       # else:
             #c1.delete(x2)
             #x2 = c1.create_image(830+i2,750+j,image=carroc)
    if(32 in h):
        guardar2()
    nvl2.after(10,keyy2)
###contadores
contgasonvl2=60
contgasonvl22=60
contpuntosnvl2=0
contpuntosnvl22=0
###contadores
###----------------------------------------------------------------------------------------Players
def guardar2():
    """
    """
    global h,x,j,i,y,i2,x2,contgasonvl2,contgasonvl22,contpuntosnvl2,contpuntosnvl22,archivo,can2
    archivo = open("partida2.txt", "w")
    posix1=can2.coords(x)[0]
    posix11=can2.coords(x)[1]
    posix2=can2.coords(x2)[0]
    posix22=can2.coords(x2)[1]
    if(contgasonvl2>0 and contgasonvl22>0):  
            archivo.write(str(contgasonvl2)+"\n")
            archivo.write(str(contpuntosnvl2)+"\n")
            archivo.write(str(contgasonvl22)+"\n")
            archivo.write(str(contpuntosnvl22)+"\n")
            archivo.write(str(posix1)+"\n")
            archivo.write(str(posix11)+"\n")
            archivo.write(str(posix2)+"\n")
            archivo.write(str(posix22)+"\n")
    
    
    archivo.close()
   
    
def cargar2():
    """
    """
    global h,x,j,i,y,i2,x2,contgasonvl2,contgasonvl22,contpuntosnvl2,contpuntosnvl22,archivo,can2
    archivo=open("partida2.txt","r")
    
    linea1 = archivo.readline()
    print(linea1)
    linea2=archivo.readline()
    print(linea2)
    linea3 = archivo.readline()
    print(linea3)
    linea4=archivo.readline()
    print(linea4)
    linea5 = archivo.readline()
    print(linea5)
    linea6=archivo.readline()
    print(linea6)
    linea7 = archivo.readline()
    print(linea7)
    linea8=archivo.readline()
    print(linea8)
    nivel2()
    juga1=can2.coords(x)[0]
    juga11=can2.coords(x)[1]
    juga2=can2.coords(x2)[0]
    juga22=can2.coords(x2)[1]
    contgasonvl2=int(linea1)
    contpuntosnvl2=int(linea2)
    contgasonvl22=int(linea3)
    contpuntosnvl22=int(linea4)
    juga1=float(linea5)
    juga11=float(linea6)
    juga2=float(linea7)
    juga22=float(linea8)
    
    archivo.close()

###------------------------------------------------guardar y cargar


###------------------------------------------------------------------------------minivan
def mininvl2():#mover minivan
    """
    Esta funcion mueve la minivan
    """
    
    global nvl2,y,p,c,z,c1,contadormini,x,contgasonvl2,contvelocidad
    menos=random.randint(280,500)
    if(c<350):
        can2.move(z,0,3)
        c = c + 1
        
    if(c==350):
        #c1.delete(z)
        
        can2.move(z,menos-can2.coords(z)[0],-can2.coords(z)[1])
        c = 0
        #z=c1.create_image(500,-50,image=minivan)

    if(contadormini<950):#250
        
        contadormini = contadormini + 1
        posx1 = can2.coords(x)[0]
        posy1 = can2.coords(x)[1]
        posx2 = can2.coords(z)[0]
        posy2 = can2.coords(z)[1]
        
        #posx1 <= posx2 and posx2+37 <= posx1 and posy1<= posy2 and posy2 <= posy1 + 50

        if(posx1>=posx2 and posx1<=posx2+28 and posy1>=posy2 and posy1<=posy2+50 or(posx1+28>=posx2 and posx1+28<=posx2+28 and posy1>=posy2 and posy1<=posy2+50) ):
            print("crash")
            l=x
            x = can2.create_image(can2.coords(l)[0],can2.coords(l)[1],image=carroc)
            can2.delete(l)
            can2.move(z,menos-can2.coords(z)[0],-can2.coords(z)[1])
            nvl2.after(10,mininvl2)
            contgasonvl2=contgasonvl2-2
            contvelocidad=0
            c=0
            can2.move(y,0,-can2.coords(y)[1])
        else:
            contadormini=0
            nvl2.after(10,mininvl2)
def mininvl22():
    """
    Esta funcion mueve la minivan del segundo mapa
    """
    
    global nvl1,y,p,c2player,c1,contadormini2,x2,contgasonvl22,contvelocidad22,min2
    menos2=random.randint(700,970)
    if(c2player<370):
        can2.move(min2,0,3)
        c2player = c2player + 1
        
    if(c2player==370):
        #c1.delete(z)
        can2.move(min2,menos2-can2.coords(min2)[0],-can2.coords(min2)[1])
        c2player = 0
        #z=c1.create_image(500,-50,image=minivan)

    if(contadormini2<950):#250
        
        contadormini2 = contadormini2 + 1
        posx1m = can2.coords(x2)[0]
        posy1m = can2.coords(x2)[1]
        posx2m = can2.coords(min2)[0]
        posy2m = can2.coords(min2)[1]
        
        #posx1 <= posx2 and posx2+37 <= posx1 and posy1<= posy2 and posy2 <= posy1 + 50

        if(posx1m>=posx2m and posx1m<=posx2m+28 and posy1m>=posy2m and posy1m<=posy2m+50 or(posx1m+28>=posx2m and posx1m+28<=posx2m+28 and posy1m>=posy2m and posy1m<=posy2m+50) ):
            print("crash")
            l3=x2
            x2 = can2.create_image(can2.coords(l3)[0],can2.coords(l3)[1],image=carroc)
            can2.delete(l3)
            can2.move(min2,menos2-can2.coords(min2)[0],-can2.coords(min2)[1])
            nvl2.after(10,mininvl22)
            contgasonvl22=contgasonvl22-2
            contvelocidad22=0
            c2player=0
            can2.move(y2,0,-can2.coords(y2)[1])
        else:
            contadormini2=0
            nvl2.after(10,mininvl22)
    
    
###-------------------------------------------------------------------------------minivan

###-----------------------------------------------------------------------------gasolina
def gasolinanvl2():
    """
    con esta funcion se crea el label de la gasolina
    """
    global gaso,nvl2,lbl3,contgasonvl2
    

    if(contgasonvl2>0):
        gaso.set(str(contgasonvl2)+" "+"G")
        contgasonvl2=contgasonvl2-1
    can2.after(1000,gasolinanvl2)
    if(contgasonvl2==0):
        nvl2.destroy()
        print("2 win")
    
def gasolinanvl22():
    """
    con esta funcion se crea el label de la gasolina
    """
    global gaso22,nvl2,contgasonvl22
    

    if(contgasonvl22>0):
        gaso22.set(str(contgasonvl22)+" "+ "G")
        contgasonvl22=contgasonvl22-1
    can2.after(1000,gasolinanvl22)
    if(contgasonvl22==0):
        nvl2.destroy()
        print("1 win")

###-----------------------------------------------------------------------------gasolina

    
###-----------------------------------------------------------------------------puntos
####puntos
def puntosnvl2():
    """
    control de puntos
    """
    global nvl1,contpuntosnvl2,puntos,lblpuntos
    if(contpuntosnvl2>=0):
        puntos.set(str(contpuntosnvl2)+ " "+"M")
        contpuntosnvl2=contpuntosnvl2+1
    can2.after(10,puntosnvl2)

def puntosnvl22():
    """
    control de puntos
    """
    global nvl1,contpuntosnvl22,puntos22,lblpuntos
    if(contpuntosnvl22>=0):
        puntos22.set(str(contpuntosnvl22)+" "+"M")
        contpuntosnvl22=contpuntosnvl22+1
    can2.after(10,puntosnvl22)

###--------------------------------------------------------------------------velocidad
####velocidad
def velocidadnvl2():
    """
    funcion para el label de velocidad
    """
    global nvl2,contvelocidad,velocidad,lblvelocidad
    if(contvelocidad>=0 and contvelocidad<=180):
        velocidad.set(str(contvelocidad)+ " "+ "KM/H")
        contvelocidad=contvelocidad+1
    can2.after(100,velocidadnvl2)
def velocidadnvl22():
    """
    funcion para el label de velocidad
    """
    global nvl2,contvelocidad22,velocidad22,lblvelocidad
    if(contvelocidad22>=0 and contvelocidad22<=180):
        velocidad22.set(str(contvelocidad22)+" "+"KM/H")
        contvelocidad22=contvelocidad22+1
    can2.after(100,velocidadnvl22)

###---------------------------------------------------------------------------velocidad

###--------------------------------------------------------------------fondo
def fonditonvl2():
    """
    """
    global c1,nvl1
    c22=0
    c32=0
    if(c22<5):
        can2.move(y,0,0.8)
        c22=c22+1
        c32=c32+1
    if(can2.coords(y)[1]>=10000):
        c22=0
        can2.move(y,0,-can2.coords(y)[1])
    nvl2.after(1,fonditonvl2)
    
        
def fonditonvl22():
    """
    """
    global c1,nvl1
    c222=0
    c322=0
    if(c222<5):
        can2.move(y2,0,0.8)
        c222=c222+1
        c322=c322+1
        
    if(can2.coords(y2)[1]>=10000):
        c222=0
        can2.move(y2,0,-can2.coords(y2)[1])
    nvl2.after(1,fonditonvl22)
###------------------------------------------------------------------fondo
###---------------------------------------------------------------------runner
####enemigo runner
def runernvl2():#mover runner
    """
    esta funcion es para mover el runer
    """
    global a,ref1,direccion,contgasonvl2,contvelocidad,contadorruner,x
    menosruner=random.randint(280,500)
    if(can2.coords(a)[0]>=250):
            direccion=direccion*(-1)
            
    if(can2.coords(a)[0]<=550):
            direccion=direccion*(-1)
    if(can2.coords(x)[1]==can2.coords(a)[1]):
        can2.move(a,menosruner-can2.coords(a)[0],-can2.coords(a)[1])
    can2.move(a,direccion*1.5,0.5)
    #nvl1.after(10,runer)
    if(contadorruner<950):#250
        
        contadorruner = contadorruner + 1
        posx1r = can2.coords(x)[0]
        posy1r = can2.coords(x)[1]
        posx2r = can2.coords(a)[0]
        posy2r = can2.coords(a)[1]
        
        #posx1 <= posx2 and posx2+37 <= posx1 and posy1<= posy2 and posy2 <= posy1 + 50

        if(posx1r>=posx2r and posx1r<=posx2r+28 and posy1r>=posy2r and posy1r<=posy2r+50 or(posx1r+28>=posx2r and posx1r+28<=posx2r+28 and posy1r>=posy2r and posy1r<=posy2r+50) ):
            print("crash")
            l=x
            x = can2.create_image(can2.coords(l)[0],can2.coords(l)[1],image=carroc)
            can2.delete(l)
            can2.move(a,menosruner-can2.coords(a)[0],-can2.coords(a)[1])
            nvl2.after(10,runernvl2)
            contgasonvl2=contgasonvl2-2
            contvelocidad=0
            can2.move(y,0,-can2.coords(y)[1])
        else:
            contadorruner=0
            nvl2.after(10,runernvl2)
    


def runernvl22():
    """
runer del nivel 2
    """
    global run2,ref1,direccion2,contadorruner2,x2,contgasonvl22,contvelocidad22
    menosruner2=random.randint(700,980)
    if(can2.coords(run2)[0]>=700):
            direccion2=direccion2*(-1)
            
    if(can2.coords(run2)[0]<=980):
            direccion2=direccion2*(-1)
    if(can2.coords(x)[1]==can2.coords(run2)[1]):
        can2.move(run2,menosruner2-can2.coords(run2)[0],-can2.coords(run2)[1])
    can2.move(run2,direccion2*1.5,0.5)
    if(contadorruner<950):#250
        
        contadorruner2 = contadorruner2 + 1
        posx1r2 = can2.coords(x2)[0]
        posy1r2 = can2.coords(x2)[1]
        posx2r2 = can2.coords(run2)[0]
        posy2r2 = can2.coords(run2)[1]
        
        #posx1 <= posx2 and posx2+37 <= posx1 and posy1<= posy2 and posy2 <= posy1 + 50

        if(posx1r2>=posx2r2 and posx1r2<=posx2r2+28 and posy1r2>=posy2r2 and posy1r2<=posy2r2+50 or(posx1r2+28>=posx2r2 and posx1r2+28<=posx2r2+28 and posy1r2>=posy2r2 and posy1r2<=posy2r2+50) ):
            print("crash")
            l4=x2
            x2 = can2.create_image(can2.coords(l4)[0],can2.coords(l4)[1],image=carroc)
            can2.delete(l4)
            can2.move(run2,menosruner2-can2.coords(run2)[0],-can2.coords(run2)[1])
            nvl2.after(10,runernvl22)
            contgasonvl22=contgasonvl22-2
            contvelocidad22=0
            can2.move(y2,0,-can2.coords(y2)[1])
        else:
            contadorruner2=0
            nvl2.after(10,runernvl22)
    

###-------------------------------------------------------------------runner
######--------------------------------------------------------------fighter
            
def fighterrnvl2():
    """
    esta funcion es para mover el fighter
    """
    
    global fight,reloadfighter,x,contgasonvl2,contvelocidad,y
    menosfighter=random.randint(280,500)
    if(can2.coords(x)[0]<can2.coords(fight)[0]):
        can2.move(fight,-0.9,2)
    elif(can2.coords(x)[0]>can2.coords(fight)[0]):
        can2.move(fight,0.9,2)
    else:
        can2.move(fight,0,2)
    if(can2.coords(x)[1]==can2.coords(fight)[1]):
        can2.move(fight,menosfighter-can2.coords(fight)[0],-can2.coords(fight)[1])
        #fight=c1.create_image(500,50,image=fighter)
        
    if(reloadfighter<950):#250
        
        reloadfighter = reloadfighter + 1
        posx11 = can2.coords(x)[0]
        posy11 = can2.coords(x)[1]
        posx22 = can2.coords(fight)[0]
        posy22 = can2.coords(fight)[1]
        
        #posx1 <= posx2 and posx2+37 <= posx1 and posy1<= posy2 and posy2 <= posy1 + 50

        if(posx11>=posx22 and posx11<=posx22+28 and posy11>=posy22 and posy11<=posy22+50 or(posx11+28>=posx22 and posx11+28<=posx22+28 and posy11>=posy22 and posy11<=posy22+50) ):
            print("crash")
            l2=x
            x = can2.create_image(can2.coords(l2)[0],can2.coords(l2)[1],image=carroc)
            can2.delete(l2)
            can2.move(fight,menosfighter-can2.coords(fight)[0],-can2.coords(fight)[1])
            nvl2.after(10,fighterrnvl2)
            contgasonvl2=contgasonvl2-2
            contvelocidad=0
            can2.move(y,0,-can2.coords(y)[1])
        else:
            reloadfighter=0
            nvl2.after(10,fighterrnvl2)

def fighterrnvl22():
    """
    esta funcion es para mover el fighter
    """
    
    global fight2,reloadfighter2,x2,contgasonvl22,contvelocidad22,y
    menosfighter2=random.randint(700,1000)
    if(can2.coords(x2)[0]<can2.coords(fight2)[0]):
        can2.move(fight2,-0.5,2)
    elif(can2.coords(x2)[0]>can2.coords(fight2)[0]):
        can2.move(fight2,0.5,2)
    else:
        can2.move(fight2,0,2)
    if(can2.coords(x2)[1]==can2.coords(fight2)[1]):
        can2.move(fight2,menosfighter2-can2.coords(fight2)[0],-can2.coords(fight2)[1])
        #fight=c1.create_image(500,50,image=fighter)
        
    if(reloadfighter2<950):#250
        
        reloadfighter2 = reloadfighter2 + 1
        posx11f = can2.coords(x2)[0]
        posy11f = can2.coords(x2)[1]
        posx22f= can2.coords(fight2)[0]
        posy22f = can2.coords(fight2)[1]
        
        #posx1 <= posx2 and posx2+37 <= posx1 and posy1<= posy2 and posy2 <= posy1 + 50

        if(posx11f>=posx22f and posx11f<=posx22f+28 and posy11f>=posy22f and posy11f<=posy22f+50 or(posx11f+28>=posx22f and posx11f+28<=posx22f+28 and posy11f>=posy22f and posy11f<=posy22f+50) ):
            print("crash")
            l22=x2
            x2 = can2.create_image(can2.coords(l22)[0],can2.coords(l22)[1],image=carroc)
            can2.delete(l22)
            can2.move(fight2,menosfighter2-can2.coords(fight2)[0],-can2.coords(fight2)[1])
            nvl2.after(10,fighterrnvl22)
            contgasonvl22=contgasonvl22-2
            contvelocidad22=0
            can2.move(y2,0,-can2.coords(y2)[1])
        else:
            reloadfighter2=0
            nvl2.after(10,fighterrnvl22)
        
        
    

####---------------------------------------------------fighter



####----------------------------------------------------mancha
def manchitanvl2():#mover minivan
    """
    mancha de aceite
    """
    
    global nvl1,y,p,c,z,c1,contadormini,x,contgasonvl2,contvelocidad,aceite,contaceite,resbalar
    menosaceite=random.randint(280,500)
    if(contaceite<400):
        can2.move(aceite,0,2)
        contaceite = contaceite + 1
        
    if(contaceite==400):
        #c1.delete(z)
        can2.move(aceite,menosaceite-can2.coords(aceite)[0],-can2.coords(aceite)[1])
        contaceite = 0

    if(resbalar<950):#250
        
        resbalar = resbalar + 1
        posx1x = can2.coords(x)[0]
        posy1x = can2.coords(x)[1]
        posx2a = can2.coords(aceite)[0]
        posy2a = can2.coords(aceite)[1]
        
        #posx1 <= posx2 and posx2+37 <= posx1 and posy1<= posy2 and posy2 <= posy1 + 50

        if(posx1x>=posx2a and posx1x<=posx2a+28 and posy1x>=posy2a and posy1x<=posy2a+50 or(posx1x+28>=posx2a and posx1x+28<=posx2a+28 and posy1x>=posy2a and posy1x<=posy2a+50) ):
            print("crash")
            l1=x
            can2.move(l1,-80,0)
            x = can2.create_image(can2.coords(l1)[0],can2.coords(l1)[1],image=carroc)
            can2.delete(l1)
            can2.move(aceite,menosaceite-can2.coords(aceite)[0],-can2.coords(aceite)[1])
            nvl2.after(10,manchitanvl2)
            contgasonvl2=contgasonvl2-2
            contvelocidad=0
            contaceite=0
            can2.move(y,0,-can2.coords(y)[1])
        else:
            resbalar=0
            nvl2.after(10,manchitanvl2)
            
def manchitanvl22():#mover minivan
    """
    mancha de aceite 2
    """
    
    global nvl1,y,p,c1,x2,contgasonvl22,contvelocidad22,aceite2,contaceite2,resbalar2
    menosaceite2=random.randint(700,970)
    if(contaceite2<400):
        can2.move(aceite2,0,2)
        contaceite2 = contaceite2 + 1
        
    if(contaceite2==400):
        #c1.delete(z)
        can2.move(aceite2,menosaceite2-can2.coords(aceite2)[0],-can2.coords(aceite2)[1])
        contaceite2 = 0

    if(resbalar2<950):#250
        
        resbalar2 = resbalar2 + 1
        posx1xm2 = can2.coords(x2)[0]
        posy1xm2 = can2.coords(x2)[1]
        posx2am2 = can2.coords(aceite2)[0]
        posy2am2 = can2.coords(aceite2)[1]
        
        #posx1 <= posx2 and posx2+37 <= posx1 and posy1<= posy2 and posy2 <= posy1 + 50

        if(posx1xm2>=posx2am2 and posx1xm2<=posx2am2+28 and posy1xm2>=posy2am2 and posy1xm2<=posy2am2+50 or(posx1xm2+28>=posx2am2 and posx1xm2+28<=posx2am2+28 and posy1xm2>=posy2am2 and posy1xm2<=posy2am2+50) ):
            print("crash")
            l13=x2
            can2.move(l13,-80,0)
            x2 = can2.create_image(can2.coords(l13)[0],can2.coords(l13)[1],image=carroc)
            can2.delete(l13)
            can2.move(aceite2,menosaceite2-can2.coords(aceite2)[0],-can2.coords(aceite2)[1])
            nvl2.after(10,manchitanvl22)
            contgasonvl22=contgasonvl22-2
            contvelocidad22=0
            contaceite2=0
            can2.move(y2,0,-can2.coords(y2)[1])
        else:
            resbalar2=0
            nvl2.after(10,manchitanvl22)


####--------------------------------------------------mancha

###-----------------------------------------------------------nyan
def podernvl2 ():
    """
    esta funcion es para mover el gato de la gasolina
    """
    global nvl1,y,p,c,z,can2,contadormini,x,contgasonvl2,contvelocidad,contadorpoder,reloadpoder,nyan
    menospoder=random.randint(280,500)
    if(contadorpoder<500):
        can2.move(nyan,0,5)
        contadorpoder = contadorpoder + 1
        
    if(contadorpoder==500):
        contadorpoder=0
        can2.move(nyan,menospoder-can2.coords(nyan)[0],-can2.coords(nyan)[1])

    if(reloadpoder<950):#250
        
        reloadpoder = reloadpoder + 1
        posx1ny = can2.coords(x)[0]
        posy1ny = can2.coords(x)[1]
        posx2ny = can2.coords(nyan)[0]
        posy2ny = can2.coords(nyan)[1]
        
        #posx1 <= posx2 and posx2+37 <= posx1 and posy1<= posy2 and posy2 <= posy1 + 50

        if(posx1ny>=posx2ny and posx1ny<=posx2ny+28 and posy1ny>=posy2ny and posy1ny<=posy2ny+50 or(posx1ny+28>=posx2ny and posx1ny+28<=posx2ny+28 and posy1ny>=posy2ny and posy1ny<=posy2ny+50) ):
            print("crash")
            can2.move(nyan,menospoder-can2.coords(nyan)[0],can2.coords(nyan)[1]-500)
            nvl2.after(10,podernvl2)
            contgasonvl2=contgasonvl2+2
            contadorpoder=0
        else:
            reloadpoder=0
            nvl2.after(10,podernvl2)
    
def podernvl22 ():
    """
    esta funcion es para mover el gato de la gasolina
    """
    global nvl1,y,p,c,z,can2,contadormini,x,contgasonvl22,contvelocidad,contadorpoder2,reloadpoder2,nyan2
    menospoder2=random.randint(700,980)
    if(contadorpoder2<500):
        can2.move(nyan2,0,5)
        contadorpoder2 = contadorpoder2 + 1
        
    if(contadorpoder2==500):
        contadorpoder2=0
        can2.move(nyan2,menospoder2-can2.coords(nyan2)[0],-can2.coords(nyan2)[1])

    if(reloadpoder2<950):#250
        
        reloadpoder2 = reloadpoder2 + 1
        posx1ny2 = can2.coords(x2)[0]
        posy1ny2 = can2.coords(x2)[1]
        posx2ny2 = can2.coords(nyan2)[0]
        posy2ny2 = can2.coords(nyan2)[1]
        
        #posx1 <= posx2 and posx2+37 <= posx1 and posy1<= posy2 and posy2 <= posy1 + 50

        if(posx1ny2>=posx2ny2 and posx1ny2<=posx2ny2+28 and posy1ny2>=posy2ny2 and posy1ny2<=posy2ny2+50 or(posx1ny2+28>=posx2ny2 and posx1ny2+28<=posx2ny2+28 and posy1ny2>=posy2ny2 and posy1ny2<=posy2ny2+50) ):
            print("crash")
            can2.move(nyan2,menospoder2-can2.coords(nyan2)[0],can2.coords(nyan2)[1]-500)
            nvl2.after(10,podernvl22)
            contgasonvl22=contgasonvl22+2
            contadorpoder2=0
        else:
            reloadpoder2=0
            nvl2.after(10,podernvl22)    

###-------------------------------------------------------------nyan


####---------------------------------------------------------------------------------------------------nivel 2
###---mapa
mapa3=tkinter.PhotoImage(file="mapa3333.png")#imagen del mapa

###---mapa
###-----------------------------------------------------------------------------------------------------nivel 3
def nivel3(): # Abrir la ventana del nivel 3, fusionar funcion de guardado a precionar nivel 3
    """
    Esta funcion es para abrir una nueva ventana, que abre el mapa del nivel 3
    """
    global can3,nvl3,mapa2,x,x2,z,gaso,gaso22,puntos,puntos22,velocidad,min2,y,y2,a,run2,fight,fight2,aceite,aceite2,nyan,nyan2
    nvl3 = tkinter.Toplevel(w0)#crear la ventana del nivel 2
    w0.iconify()
    nvl3.geometry("1200x850")#dimensiones de la ventana
    can3=tkinter.Canvas(nvl3,bg="black", width=1600, height=800)#canvas del nivel 2
    can3.pack()
    y=can3.create_image(400,400,image=mapa3)#mapa del nivel 2
    y2=can3.create_image(847,400,image=mapa3)
    can3.lower(y)
    can3.lower(y2)
    #label gasolina, jugadores, puntos
    lbl3=tkinter.Label(nvl3,textvariable= gaso,fg="white",bg="black", underline=True,font=("",16,"bold")).place(x=50,y=62)#GASOLINA 1
    lblgaso2=tkinter.Label(nvl3,textvariable= gaso22,fg="white",bg="black", underline=True,font=("",16,"bold")).place(x=50,y=430)#gasolina 2
    lbljugador1=tkinter.Label(nvl3,text=j1.get(),fg="white",bg="black",font=("Arial",14)).place(x=50,y=10)
    lbljugador2=tkinter.Label(nvl3,text=j2.get(),fg="white",bg="black",font=("Arial",14)).place(x=50,y=400)
    lblpuntos=tkinter.Label(nvl3,textvariable=puntos,fg="white",bg="black",font=("",16,"bold")).place(x=50,y=100)#puntos 1
    lblpuntos2=tkinter.Label(nvl3,textvariable=puntos22,fg="white",bg="black",font=("",16,"bold")).place(x=50,y=460)#puntos 2
    lblvelocidad=tkinter.Label(nvl3,textvariable=velocidad,fg="white",bg="black",font=("",16,"bold")).place(x=50,y=130)# velocidad 1
    lblvelocidad2=tkinter.Label(nvl3,textvariable=velocidad22,fg="white",bg="black",font=("",16,"bold")).place(x=50,y=490)#velocidad 2
    ##cargar imagenes del player y los enemigos
    x= can3.create_image(400+i,750+j,image=carro)#imagen carro
    a=can3.create_image(400,170,image=runner)#imagen runner
    z=can3.create_image(500,-50,image=minivan)#imagen minivan
    fight=can3.create_image(500,50,image=fighter)#imagen fighter
    aceite=can3.create_image(480,30,image=mancha)#aceite del 1
    nyan=can3.create_image(450,50,image=imagengasolina)#nyan 1
    ##2 pantalla
    x2=can3.create_image(830,750,image=carro)#imagen carro 2
    nyan2=can3.create_image(770,50,image=imagengasolina)#nyan 2
    min2=can3.create_image(830,-50,image=minivan)#minivan dos
    fight2=can3.create_image(750,50,image=fighter)#fighter 2
    run2=can3.create_image(730,50,image=runner)#imagen runner
    aceite2=can3.create_image(770,30,image=mancha)#aceite del 1
    can3.bind("<KeyPress>", keydown)
    can3.bind("<KeyRelease>", keyup)
    can3.focus_set()
    ##funciones
    gasolinanvl3()
    gasolinanvl33()
    mininvl3()
    mininvl33()
    puntosnvl3()
    puntosnvl33()
    velocidadnvl3()
    velocidadnvl33()
    fonditonvl3()
    fonditonvl33()
    runernvl3()
    runernvl33()
    fighterrnvl3()
    fighterrnvl33()
    manchitanvl3()
    manchitanvl33()
    podernvl3()
    podernvl33()
    keyy3()

###-------------------------------------------------------------players
def keyy3():
    global h, playernvl2,i,j,y,i2,x2,nvl3,playernvl22,x,can3
    if(68 in h):
        if(i<150):
            can3.delete(x)
            i = i + 3
            x = can3.create_image(400+i,750+j,image=carro)
        #else:
            #c1.delete(x)
            #x = c1.create_image(400+i,750+j,image=carroc) 
    if(65 in h):
        if(i > -140):
            can3.delete(x)
            i = i - 3
            x = can3.create_image(400+i,750+j,image=carro)
        #else:
            #c1.delete(x)
            #x = c1.create_image(400+i,750+j,image=carroc)
    if(76 in h):
        if(i2 < 160):
            can3.delete(x2)
            i2 = i2 + 3
            x2 = can3.create_image(830+i2,750+j,image=carro)
        #else:
            #c1.delete(x2)
            #x2 = c1.create_image(830+i2,750+j,image=carroc)
    if(74 in h):
        if(i2 > -130):
             can3.delete(x2)
             i2 = i2 - 3
             x2 = can3.create_image(830+i2,750+j,image=carro)
       # else:
             #c1.delete(x2)
             #x2 = c1.create_image(830+i2,750+j,image=carroc)
    if(32 in h):
        guardar3()
    nvl3.after(10,keyy3)




###-------------------------------------------------------------players
###contadores
contgasonvl3=60
contgasonvl33=60
contpuntosnvl3=0
contpuntosnvl33=0
###contadores
####----------------------------------------------------------------------------guardar y cargar
def guardar3():
    """
    """
    global h,x,j,i,y,i2,x2,contgasonvl3,contgasonvl33,contpuntosnvl3,contpuntosnvl33,can3,archivo
    archivo = open("partida3.txt", "w")
    posix1=can3.coords(x)[0]
    posix11=can3.coords(x)[1]
    posix2=can3.coords(x2)[0]
    posix22=can3.coords(x2)[1]
    if(contgasonvl3>0 and contgasonvl33>0):  
            archivo.write(str(contgasonvl3)+"\n")
            archivo.write(str(contpuntosnvl3)+"\n")
            archivo.write(str(contgasonvl33)+"\n")
            archivo.write(str(contpuntosnvl33)+"\n")
            archivo.write(str(posix1)+"\n")
            archivo.write(str(posix11)+"\n")
            archivo.write(str(posix2)+"\n")
            archivo.write(str(posix22)+"\n")
    
    
    archivo.close()
   
    
def cargar3():
    """
    """
    global h,x,j,i,y,i2,x2,contgasonvl3,contgasonvl33,contpuntosnvl3,contpuntosnvl33,can3,archivo
    archivo=open("partida3.txt","r")
    
    linea1 = archivo.readline()
    print(linea1)
    linea2=archivo.readline()
    print(linea2)
    linea3 = archivo.readline()
    print(linea3)
    linea4=archivo.readline()
    print(linea4)
    linea5 = archivo.readline()
    print(linea5)
    linea6=archivo.readline()
    print(linea6)
    linea7 = archivo.readline()
    print(linea7)
    linea8=archivo.readline()
    print(linea8)
    nivel3()
    juga1=can3.coords(x)[0]
    juga11=can3.coords(x)[1]
    juga2=can3.coords(x2)[0]
    juga22=can3.coords(x2)[1]
    contgasonvl3=int(linea1)
    contpuntosnvl3=int(linea2)
    contgasonvl33=int(linea3)
    contpuntosnvl33=int(linea4)
    juga1=float(linea5)
    juga11=float(linea6)
    juga2=float(linea7)
    juga22=float(linea8)
    
    archivo.close()

###------------------------------------------------guardar y cargar


###-------------------------------------------------------------minivan
def mininvl3():#mover minivan
    """
    Esta funcion mueve la minivan
    """
    
    global nvl3,y,p,c,z,can3,contadormini,x,contgasonvl3,contvelocidad
    menos=random.randint(280,500)
    if(c<280):
        can3.move(z,0,5)
        c = c + 1
        
    if(c==280):
        #c1.delete(z)
        
        can3.move(z,menos-can3.coords(z)[0],-can3.coords(z)[1])
        c = 0
        #z=c1.create_image(500,-50,image=minivan)

    if(contadormini<950):#250
        
        contadormini = contadormini + 1
        posx1 = can3.coords(x)[0]
        posy1 = can3.coords(x)[1]
        posx2 = can3.coords(z)[0]
        posy2 = can3.coords(z)[1]
        
        #posx1 <= posx2 and posx2+37 <= posx1 and posy1<= posy2 and posy2 <= posy1 + 50

        if(posx1>=posx2 and posx1<=posx2+28 and posy1>=posy2 and posy1<=posy2+50 or(posx1+28>=posx2 and posx1+28<=posx2+28 and posy1>=posy2 and posy1<=posy2+50) ):
            print("crash")
            l=x
            x = can3.create_image(can3.coords(l)[0],can3.coords(l)[1],image=carroc)
            can3.delete(l)
            can3.move(z,menos-can3.coords(z)[0],-can3.coords(z)[1])
            nvl3.after(10,mininvl3)
            contgasonvl3=contgasonvl3-2
            contvelocidad=0
            c=0
            can3.move(y,0,-can3.coords(y)[1])
        else:
            contadormini=0
            nvl3.after(10,mininvl3)
def mininvl33():
    """
    Esta funcion mueve la minivan del segundo mapa
    """
    
    global nvl3,y,p,c2player,can3,contadormini2,x2,contgasonvl33,contvelocidad22,min2
    menos2=random.randint(700,970)
    if(c2player<280):
        can3.move(min2,0,5)
        c2player = c2player + 1
        
    if(c2player==280):
        #c1.delete(z)
        can3.move(min2,menos2-can3.coords(min2)[0],-can3.coords(min2)[1])
        c2player = 0
        #z=c1.create_image(500,-50,image=minivan)

    if(contadormini2<950):#250
        
        contadormini2 = contadormini2 + 1
        posx1m = can3.coords(x2)[0]
        posy1m = can3.coords(x2)[1]
        posx2m = can3.coords(min2)[0]
        posy2m = can3.coords(min2)[1]
        
        #posx1 <= posx2 and posx2+37 <= posx1 and posy1<= posy2 and posy2 <= posy1 + 50

        if(posx1m>=posx2m and posx1m<=posx2m+28 and posy1m>=posy2m and posy1m<=posy2m+50 or(posx1m+28>=posx2m and posx1m+28<=posx2m+28 and posy1m>=posy2m and posy1m<=posy2m+50) ):
            print("crash")
            l3=x2
            x2 = can3.create_image(can3.coords(l3)[0],can3.coords(l3)[1],image=carroc)
            can3.delete(l3)
            can3.move(min2,menos2-can3.coords(min2)[0],-can3.coords(min2)[1])
            nvl3.after(10,mininvl33)
            contgasonvl33=contgasonvl33-2
            contvelocidad22=0
            c2player=0
            can3.move(y2,0,-can3.coords(y2)[1])
        else:
            contadormini2=0
            nvl3.after(10,mininvl33)


###---------------------------------------------------------------minivan


###-----------------------------------------------------------------------------gasolina
def gasolinanvl3():
    """
    con esta funcion se crea el label de la gasolina
    """
    global gaso,nvl3,lbl3,contgasonvl3,can3
    
    
    if(contgasonvl3>0):
        gaso.set(str(contgasonvl3)+" "+"G")
        contgasonvl3=contgasonvl3-1
    can3.after(1000,gasolinanvl3)
    if(contgasonvl3==0):
        nvl3.destroy()
        print("2 win")
    
def gasolinanvl33():
    """
    con esta funcion se crea el label de la gasolina
    """
    global gaso22,nvl3,contgasonvl33
    
    
    if(contgasonvl33>0):
        gaso22.set(str(contgasonvl33)+" "+ "G")
        contgasonvl33=contgasonvl33-1
    can3.after(1000,gasolinanvl33)
    if(contgasonvl33==0):
        nvl3.destroy()
        print("1 win")

###-----------------------------------------------------------------------------gasolina


###-----------------------------------------------------------------------------puntos
####puntos
def puntosnvl3():
    """
    control de puntos
    """
    global nvl3,contpuntosnvl3,puntos,lblpuntos
    if(contpuntosnvl3>=0):
        puntos.set(str(contpuntosnvl3)+ " "+"M")
        contpuntosnvl3=contpuntosnvl3+1
    can3.after(10,puntosnvl3)

def puntosnvl33():
    """
    control de puntos
    """
    global nvl3,contpuntosnvl33,puntos22,lblpuntos
    if(contpuntosnvl33>=0):
        puntos22.set(str(contpuntosnvl33)+" "+"M")
        contpuntosnvl33=contpuntosnvl33+1
    can3.after(10,puntosnvl33)

###------------------------------------------------------------------------puntos
###--------------------------------------------------------------------------velocidad
####velocidad
def velocidadnvl3():
    """
    funcion para el label de velocidad
    """
    global nvl3,contvelocidad,velocidad,lblvelocidad
    if(contvelocidad>=0 and contvelocidad<=180):
        velocidad.set(str(contvelocidad)+ " "+ "KM/H")
        contvelocidad=contvelocidad+1
    can3.after(100,velocidadnvl3)
def velocidadnvl33():
    """
    funcion para el label de velocidad
    """
    global nvl3,contvelocidad22,velocidad22,lblvelocidad
    if(contvelocidad22>=0 and contvelocidad22<=180):
        velocidad22.set(str(contvelocidad22)+" "+"KM/H")
        contvelocidad22=contvelocidad22+1
    can3.after(100,velocidadnvl33)

###---------------------------------------------------------------------------velocidad
###--------------------------------------------------------------------fondo
def fonditonvl3():
    """
    """
    global can3,nvl3
    c22=0
    c32=0
    if(c22<5):
        can3.move(y,0,0.8)
        c22=c22+1
        c32=c32+1
    if(can3.coords(y)[1]>=10000):
        c22=0
        can3.move(y,0,-can3.coords(y)[1])
    nvl3.after(1,fonditonvl3)
    
        
def fonditonvl33():
    """
    """
    global can3,nvl3
    c222=0
    c322=0
    if(c222<5):
        can3.move(y2,0,0.8)
        c222=c222+1
        c322=c322+1
        
    if(can3.coords(y2)[1]>=10000):
        c222=0
        can3.move(y2,0,-can3.coords(y2)[1])
    nvl3.after(1,fonditonvl33)
###------------------------------------------------------------------fondo
###---------------------------------------------------------------------runner
####enemigo runner
def runernvl3():#mover runner
    """
    esta funcion es para mover el runer
    """
    global a,ref1,direccion,contgasonvl3,contvelocidad,contadorruner,x
    menosruner=random.randint(280,500)
    if(can3.coords(a)[0]>=250):
            direccion=direccion*(-1)
            
    if(can3.coords(a)[0]<=550):
            direccion=direccion*(-1)
    if(can3.coords(x)[1]==can3.coords(a)[1]):
        can3.move(a,menosruner-can3.coords(a)[0],-can3.coords(a)[1])
    can3.move(a,direccion*3,2)
    #nvl1.after(10,runer)
    if(contadorruner<950):#250
        
        contadorruner = contadorruner + 1
        posx1r = can3.coords(x)[0]
        posy1r = can3.coords(x)[1]
        posx2r = can3.coords(a)[0]
        posy2r = can3.coords(a)[1]
        
        #posx1 <= posx2 and posx2+37 <= posx1 and posy1<= posy2 and posy2 <= posy1 + 50

        if(posx1r>=posx2r and posx1r<=posx2r+28 and posy1r>=posy2r and posy1r<=posy2r+50 or(posx1r+28>=posx2r and posx1r+28<=posx2r+28 and posy1r>=posy2r and posy1r<=posy2r+50) ):
            print("crash")
            l=x
            x = can3.create_image(can3.coords(l)[0],can3.coords(l)[1],image=carroc)
            can3.delete(l)
            can3.move(a,menosruner-can3.coords(a)[0],-can3.coords(a)[1])
            nvl3.after(10,runernvl3)
            contgasonvl3=contgasonvl3-2
            contvelocidad=0
            can3.move(y,0,-can3.coords(y)[1])
        else:
            contadorruner=0
            nvl3.after(10,runernvl3)
    


def runernvl33():
    """
runer del nivel 2
    """
    global run2,ref1,direccion2,contadorruner2,x2,contgasonvl33,contvelocidad22
    menosruner2=random.randint(700,980)
    if(can3.coords(run2)[0]>=700):
            direccion2=direccion2*(-1)
            
    if(can3.coords(run2)[0]<=980):
            direccion2=direccion2*(-1)
    if(can3.coords(x)[1]==can3.coords(run2)[1]):
        can3.move(run2,menosruner2-can3.coords(run2)[0],-can3.coords(run2)[1])
    can3.move(run2,direccion2*3,2)
    if(contadorruner<950):#250
        
        contadorruner2 = contadorruner2 + 1
        posx1r2 = can3.coords(x2)[0]
        posy1r2 = can3.coords(x2)[1]
        posx2r2 = can3.coords(run2)[0]
        posy2r2 = can3.coords(run2)[1]
        
        #posx1 <= posx2 and posx2+37 <= posx1 and posy1<= posy2 and posy2 <= posy1 + 50

        if(posx1r2>=posx2r2 and posx1r2<=posx2r2+28 and posy1r2>=posy2r2 and posy1r2<=posy2r2+50 or(posx1r2+28>=posx2r2 and posx1r2+28<=posx2r2+28 and posy1r2>=posy2r2 and posy1r2<=posy2r2+50) ):
            print("crash")
            l4=x2
            x2 = can3.create_image(can3.coords(l4)[0],can3.coords(l4)[1],image=carroc)
            can3.delete(l4)
            can3.move(run2,menosruner2-can3.coords(run2)[0],-can3.coords(run2)[1])
            nvl3.after(10,runernvl33)
            contgasonvl33=contgasonvl33-2
            contvelocidad22=0
            can3.move(y2,0,-can3.coords(y2)[1])
        else:
            contadorruner2=0
            nvl3.after(10,runernvl33)
    

###-------------------------------------------------------------------runner
######--------------------------------------------------------------fighter
            
def fighterrnvl3():
    """
    esta funcion es para mover el fighter
    """
    
    global fight,reloadfighter,x,contgasonvl3,contvelocidad,y
    menosfighter=random.randint(280,500)
    if(can3.coords(x)[0]<can3.coords(fight)[0]):
        can3.move(fight,-1.2,2)
    elif(can3.coords(x)[0]>can3.coords(fight)[0]):
        can3.move(fight,1.2,2)
    else:
        can3.move(fight,0,3)
    if(can3.coords(x)[1]==can3.coords(fight)[1]):
        can3.move(fight,menosfighter-can3.coords(fight)[0],-can3.coords(fight)[1])
        #fight=c1.create_image(500,50,image=fighter)
        
    if(reloadfighter<950):#250
        
        reloadfighter = reloadfighter + 1
        posx11 = can3.coords(x)[0]
        posy11 = can3.coords(x)[1]
        posx22 = can3.coords(fight)[0]
        posy22 = can3.coords(fight)[1]
        
        #posx1 <= posx2 and posx2+37 <= posx1 and posy1<= posy2 and posy2 <= posy1 + 50

        if(posx11>=posx22 and posx11<=posx22+28 and posy11>=posy22 and posy11<=posy22+50 or(posx11+28>=posx22 and posx11+28<=posx22+28 and posy11>=posy22 and posy11<=posy22+50) ):
            print("crash")
            l2=x
            x = can3.create_image(can3.coords(l2)[0],can3.coords(l2)[1],image=carroc)
            can3.delete(l2)
            can3.move(fight,menosfighter-can3.coords(fight)[0],-can3.coords(fight)[1])
            nvl3.after(10,fighterrnvl3)
            contgasonvl3=contgasonvl3-2
            contvelocidad=0
            can3.move(y,0,-can3.coords(y)[1])
        else:
            reloadfighter=0
            nvl3.after(10,fighterrnvl3)

def fighterrnvl33():
    """
    esta funcion es para mover el fighter
    """
    
    global fight2,reloadfighter2,x2,contgasonvl33,contvelocidad22,y
    menosfighter2=random.randint(700,1000)
    if(can3.coords(x2)[0]<can3.coords(fight2)[0]):
        can3.move(fight2,-1.2,2)
    elif(can3.coords(x2)[0]>can3.coords(fight2)[0]):
        can3.move(fight2,1.2,2)
    else:
        can3.move(fight2,0,2)
    if(can3.coords(x2)[1]==can3.coords(fight2)[1]):
        can3.move(fight2,menosfighter2-can3.coords(fight2)[0],-can3.coords(fight2)[1])
        #fight=c1.create_image(500,50,image=fighter)
        
    if(reloadfighter2<950):#250
        
        reloadfighter2 = reloadfighter2 + 1
        posx11f = can3.coords(x2)[0]
        posy11f = can3.coords(x2)[1]
        posx22f= can3.coords(fight2)[0]
        posy22f = can3.coords(fight2)[1]
        
        #posx1 <= posx2 and posx2+37 <= posx1 and posy1<= posy2 and posy2 <= posy1 + 50

        if(posx11f>=posx22f and posx11f<=posx22f+28 and posy11f>=posy22f and posy11f<=posy22f+50 or(posx11f+28>=posx22f and posx11f+28<=posx22f+28 and posy11f>=posy22f and posy11f<=posy22f+50) ):
            print("crash")
            l22=x2
            x2 = can3.create_image(can3.coords(l22)[0],can3.coords(l22)[1],image=carroc)
            can3.delete(l22)
            can3.move(fight2,menosfighter2-can3.coords(fight2)[0],-can3.coords(fight2)[1])
            nvl3.after(10,fighterrnvl33)
            contgasonvl33=contgasonvl33-2
            contvelocidad22=0
            can3.move(y2,0,-can3.coords(y2)[1])
        else:
            reloadfighter2=0
            nvl3.after(10,fighterrnvl33)
        
        
    

####---------------------------------------------------fighter
####----------------------------------------------------mancha
def manchitanvl3():#mover minivan
    """
    mancha de aceite
    """
    
    global nvl1,y,p,c,z,c1,contadormini,x,contgasonvl3,contvelocidad,aceite,contaceite,resbalar
    menosaceite=random.randint(280,500)
    if(contaceite<380):
        can3.move(aceite,0,3)
        contaceite = contaceite + 1
        
    if(contaceite==380):
        #c1.delete(z)
        can3.move(aceite,menosaceite-can3.coords(aceite)[0],-can3.coords(aceite)[1])
        contaceite = 0

    if(resbalar<950):#250
        
        resbalar = resbalar + 1
        posx1x = can3.coords(x)[0]
        posy1x = can3.coords(x)[1]
        posx2a = can3.coords(aceite)[0]
        posy2a = can3.coords(aceite)[1]
        
        #posx1 <= posx2 and posx2+37 <= posx1 and posy1<= posy2 and posy2 <= posy1 + 50

        if(posx1x>=posx2a and posx1x<=posx2a+28 and posy1x>=posy2a and posy1x<=posy2a+50 or(posx1x+28>=posx2a and posx1x+28<=posx2a+28 and posy1x>=posy2a and posy1x<=posy2a+50) ):
            print("crash")
            l1=x
            can3.move(l1,-80,0)
            x = can3.create_image(can3.coords(l1)[0],can3.coords(l1)[1],image=carroc)
            can3.delete(l1)
            can3.move(aceite,menosaceite-can3.coords(aceite)[0],-can3.coords(aceite)[1])
            nvl3.after(10,manchitanvl3)
            contgasonvl3=contgasonvl3-2
            contvelocidad=0
            contaceite=0
            can3.move(y,0,-can3.coords(y)[1])
        else:
            resbalar=0
            nvl3.after(10,manchitanvl3)
            
def manchitanvl33():#mover minivan
    """
    mancha de aceite 2
    """
    
    global nvl1,y,p,c1,x2,contgasonvl33,contvelocidad22,aceite2,contaceite2,resbalar2
    menosaceite2=random.randint(700,970)
    if(contaceite2<380):
        can3.move(aceite2,0,3)
        contaceite2 = contaceite2 + 1
        
    if(contaceite2==380):
        #c1.delete(z)
        can3.move(aceite2,menosaceite2-can3.coords(aceite2)[0],-can3.coords(aceite2)[1])
        contaceite2 = 0

    if(resbalar2<950):#250
        
        resbalar2 = resbalar2 + 1
        posx1xm2 = can3.coords(x2)[0]
        posy1xm2 = can3.coords(x2)[1]
        posx2am2 = can3.coords(aceite2)[0]
        posy2am2 = can3.coords(aceite2)[1]
        
        #posx1 <= posx2 and posx2+37 <= posx1 and posy1<= posy2 and posy2 <= posy1 + 50

        if(posx1xm2>=posx2am2 and posx1xm2<=posx2am2+28 and posy1xm2>=posy2am2 and posy1xm2<=posy2am2+50 or(posx1xm2+28>=posx2am2 and posx1xm2+28<=posx2am2+28 and posy1xm2>=posy2am2 and posy1xm2<=posy2am2+50) ):
            print("crash")
            l13=x2
            can3.move(l13,-80,0)
            x2 = can3.create_image(can3.coords(l13)[0],can3.coords(l13)[1],image=carroc)
            can3.delete(l13)
            can3.move(aceite2,menosaceite2-can3.coords(aceite2)[0],-can3.coords(aceite2)[1])
            nvl3.after(10,manchitanvl33)
            contgasonvl33=contgasonvl33-2
            contvelocidad22=0
            contaceite2=0
            can3.move(y2,0,-can3.coords(y2)[1])
        else:
            resbalar2=0
            nvl3.after(10,manchitanvl33)


####--------------------------------------------------mancha
###-----------------------------------------------------------nyan
def podernvl3 ():
    """
    esta funcion es para mover el gato de la gasolina
    """
    global nvl3,y,p,c,z,can2,contadormini,x,contgasonvl3,contvelocidad,contadorpoder,reloadpoder,nyan
    menospoder=random.randint(280,500)
    if(contadorpoder<500):
        can3.move(nyan,0,6)
        contadorpoder = contadorpoder + 1
        
    if(contadorpoder==500):
        contadorpoder=0
        can3.move(nyan,menospoder-can3.coords(nyan)[0],-can3.coords(nyan)[1])

    if(reloadpoder<950):#250
        
        reloadpoder = reloadpoder + 1
        posx1ny = can3.coords(x)[0]
        posy1ny = can3.coords(x)[1]
        posx2ny = can3.coords(nyan)[0]
        posy2ny = can3.coords(nyan)[1]
        
        #posx1 <= posx2 and posx2+37 <= posx1 and posy1<= posy2 and posy2 <= posy1 + 50

        if(posx1ny>=posx2ny and posx1ny<=posx2ny+28 and posy1ny>=posy2ny and posy1ny<=posy2ny+50 or(posx1ny+28>=posx2ny and posx1ny+28<=posx2ny+28 and posy1ny>=posy2ny and posy1ny<=posy2ny+50) ):
            print("crash")
            can3.move(nyan,menospoder-can3.coords(nyan)[0],can3.coords(nyan)[1]-500)
            nvl3.after(10,podernvl3)
            contgasonvl3=contgasonvl3+2
            contadorpoder=0
        else:
            reloadpoder=0
            nvl3.after(10,podernvl3)
    
def podernvl33 ():
    """
    esta funcion es para mover el gato de la gasolina
    """
    global nvl3,y,p,c,z,can2,contadormini,x,contgasonvl33,contvelocidad,contadorpoder2,reloadpoder2,nyan2
    menospoder2=random.randint(700,980)
    if(contadorpoder2<500):
        can3.move(nyan2,0,6)
        contadorpoder2 = contadorpoder2 + 1
        
    if(contadorpoder2==500):
        contadorpoder2=0
        can3.move(nyan2,menospoder2-can3.coords(nyan2)[0],-can3.coords(nyan2)[1])

    if(reloadpoder2<950):#250
        
        reloadpoder2 = reloadpoder2 + 1
        posx1ny2 = can3.coords(x2)[0]
        posy1ny2 = can3.coords(x2)[1]
        posx2ny2 = can3.coords(nyan2)[0]
        posy2ny2 = can3.coords(nyan2)[1]
        
        #posx1 <= posx2 and posx2+37 <= posx1 and posy1<= posy2 and posy2 <= posy1 + 50

        if(posx1ny2>=posx2ny2 and posx1ny2<=posx2ny2+28 and posy1ny2>=posy2ny2 and posy1ny2<=posy2ny2+50 or(posx1ny2+28>=posx2ny2 and posx1ny2+28<=posx2ny2+28 and posy1ny2>=posy2ny2 and posy1ny2<=posy2ny2+50) ):
            print("crash")
            can3.move(nyan2,menospoder2-can3.coords(nyan2)[0],can3.coords(nyan2)[1]-500)
            nvl3.after(10,podernvl33)
            contgasonvl33=contgasonvl33+2
            contadorpoder2=0
        else:
            reloadpoder2=0
            nvl3.after(10,podernvl33)    

###-------------------------------------------------------------nyan

###---mapa
mapa4=tkinter.PhotoImage(file="mapa4444.png")#imagen del mapa

###---mapa

    
###---------------------------------------------------------------------------------------------------nivel 3

###-----------------------------------------------------------------------------------------------------nivel 4
    
def nivel4(): # Abrir la ventana del nivel 4, fusionar funcion de guardado a presionar nivel 4
    """
    Esta funcion es para abrir una nueva ventana, que abre el mapa del nivel 4
    """
    global can4,nvl4,mapa2,x,x2,z,gaso,gaso22,puntos,puntos22,velocidad,min2,y,y2,a,run2,fight,fight2,aceite,aceite2,nyan,nyan2
    nvl4 = tkinter.Toplevel(w0)#crear la ventana del nivel 2
    w0.iconify()
    nvl4.geometry("1200x850")#dimensiones de la ventana
    can4=tkinter.Canvas(nvl4,bg="black", width=1600, height=800)#canvas del nivel 2
    can4.pack()
    y=can4.create_image(400,400,image=mapa4)#mapa del nivel 2
    y2=can4.create_image(847,400,image=mapa4)
    can4.lower(y)
    can4.lower(y2)
    #label gasolina, jugadores, puntos
    lbl3=tkinter.Label(nvl4,textvariable= gaso,fg="white",bg="black", underline=True,font=("",16,"bold")).place(x=50,y=62)#GASOLINA 1
    lblgaso2=tkinter.Label(nvl4,textvariable= gaso22,fg="white",bg="black", underline=True,font=("",16,"bold")).place(x=50,y=430)#gasolina 2
    lbljugador1=tkinter.Label(nvl4,text=j1.get(),fg="white",bg="black",font=("Arial",14)).place(x=50,y=10)
    lbljugador2=tkinter.Label(nvl4,text=j2.get(),fg="white",bg="black",font=("Arial",14)).place(x=50,y=400)
    lblpuntos=tkinter.Label(nvl4,textvariable=puntos,fg="white",bg="black",font=("",16,"bold")).place(x=50,y=100)#puntos 1
    lblpuntos2=tkinter.Label(nvl4,textvariable=puntos22,fg="white",bg="black",font=("",16,"bold")).place(x=50,y=460)#puntos 2
    lblvelocidad=tkinter.Label(nvl4,textvariable=velocidad,fg="white",bg="black",font=("",16,"bold")).place(x=50,y=130)# velocidad 1
    lblvelocidad2=tkinter.Label(nvl4,textvariable=velocidad22,fg="white",bg="black",font=("",16,"bold")).place(x=50,y=490)#velocidad 2
    ##cargar imagenes del player y los enemigos
    x= can4.create_image(400+i,750+j,image=carro)#imagen carro
    a=can4.create_image(400,170,image=runner)#imagen runner
    z=can4.create_image(500,-50,image=minivan)#imagen minivan
    fight=can4.create_image(500,50,image=fighter)#imagen fighter
    aceite=can4.create_image(480,30,image=mancha)#aceite del 1
    nyan=can4.create_image(450,50,image=imagengasolina)#nyan 1
    ##2 pantalla
    x2=can4.create_image(830,750,image=carro)#imagen carro 2
    nyan2=can4.create_image(770,50,image=imagengasolina)#nyan 2
    min2=can4.create_image(830,-50,image=minivan)#minivan dos
    fight2=can4.create_image(750,50,image=fighter)#fighter 2
    run2=can4.create_image(730,50,image=runner)#imagen runner
    aceite2=can4.create_image(770,30,image=mancha)#aceite del 1
    can4.bind("<KeyPress>", keydown)
    can4.bind("<KeyRelease>", keyup)
    can4.focus_set()
    #funciones
    gasolinanvl4()
    gasolinanvl44()
    mininvl4()
    mininvl44()
    puntosnvl4()
    puntosnvl44()
    velocidadnvl4()
    velocidadnvl44()
    fonditonvl4()
    fonditonvl44()
    runernvl4()
    runernvl44()
    fighterrnvl4()
    fighterrnvl44()
    manchitanvl4()
    manchitanvl44()
    podernvl4()
    podernvl44()
    keyy4()

###-------------------------------------------------------------players
def keyy4():
    global h, playernvl2,i,j,y,i2,x2,nvl4,playernvl22,x,can4
    if(68 in h):
        if(i<150):
            can4.delete(x)
            i = i + 3
            x = can4.create_image(400+i,750+j,image=carro)
        #else:
            #c1.delete(x)
            #x = c1.create_image(400+i,750+j,image=carroc) 
    if(65 in h):
        if(i > -140):
            can4.delete(x)
            i = i - 3
            x = can4.create_image(400+i,750+j,image=carro)
        #else:
            #c1.delete(x)
            #x = c1.create_image(400+i,750+j,image=carroc)
    if(76 in h):
        if(i2 < 160):
            can4.delete(x2)
            i2 = i2 + 3
            x2 = can4.create_image(830+i2,750+j,image=carro)
        #else:
            #c1.delete(x2)
            #x2 = c1.create_image(830+i2,750+j,image=carroc)
    if(74 in h):
        if(i2 > -130):
             can4.delete(x2)
             i2 = i2 - 3
             x2 = can4.create_image(830+i2,750+j,image=carro)
       # else:
             #c1.delete(x2)
             #x2 = c1.create_image(830+i2,750+j,image=carroc)
    if(32 in h):
        guardar4()
    nvl4.after(10,keyy4)




###-------------------------------------------------------------players
###contadores
contgasonvl4=60
contgasonvl44=60
contpuntosnvl4=0
contpuntosnvl44=0
###contadores
####----------------------------------------------------------------------------guardar y cargar
def guardar4():
    """
    """
    global h,x,j,i,y,i2,x2,contgasonvl4,contgasonvl44,contpuntosnvl4,contpuntosnvl44,can4,archivo
    archivo = open("partida4.txt", "w")
    posix1=can4.coords(x)[0]
    posix11=can4.coords(x)[1]
    posix2=can4.coords(x2)[0]
    posix22=can4.coords(x2)[1]
    if(contgasonvl4>0 and contgasonvl44>0):  
            archivo.write(str(contgasonvl4)+"\n")
            archivo.write(str(contpuntosnvl4)+"\n")
            archivo.write(str(contgasonvl44)+"\n")
            archivo.write(str(contpuntosnvl44)+"\n")
            archivo.write(str(posix1)+"\n")
            archivo.write(str(posix11)+"\n")
            archivo.write(str(posix2)+"\n")
            archivo.write(str(posix22)+"\n")
    
    
    archivo.close()
   
    
def cargar4():
    """
    """
    global h,x,j,i,y,i2,x2,contgasonvl4,contgasonvl44,contpuntosnvl4,contpuntosnvl44,can4,archivo
    archivo=open("partida4.txt","r")
    
    linea1 = archivo.readline()
    print(linea1)
    linea2=archivo.readline()
    print(linea2)
    linea3 = archivo.readline()
    print(linea3)
    linea4=archivo.readline()
    print(linea4)
    linea5 = archivo.readline()
    print(linea5)
    linea6=archivo.readline()
    print(linea6)
    linea7 = archivo.readline()
    print(linea7)
    linea8=archivo.readline()
    print(linea8)
    nivel4()
    juga1=can4.coords(x)[0]
    juga11=can4.coords(x)[1]
    juga2=can4.coords(x2)[0]
    juga22=can4.coords(x2)[1]
    contgasonvl4=int(linea1)
    contpuntosnvl4=int(linea2)
    contgasonvl44=int(linea3)
    contpuntosnvl44=int(linea4)
    juga1=float(linea5)
    juga11=float(linea6)
    juga2=float(linea7)
    juga22=float(linea8)
    
    archivo.close()

###------------------------------------------------guardar y cargar

###-------------------------------------------------------------minivan
def mininvl4():#mover minivan
    """
    Esta funcion mueve la minivan
    """
    
    global nvl4,y,p,c,z,can4,contadormini,x,contgasonvl4,contvelocidad
    menos=random.randint(280,500)
    if(c<240):
        can4.move(z,0,8)
        c = c + 1
        
    if(c==240):
        #c1.delete(z)
        
        can4.move(z,menos-can4.coords(z)[0],-can4.coords(z)[1])
        c = 0
        #z=c1.create_image(500,-50,image=minivan)

    if(contadormini<950):#250
        
        contadormini = contadormini + 1
        posx1 = can4.coords(x)[0]
        posy1 = can4.coords(x)[1]
        posx2 = can4.coords(z)[0]
        posy2 = can4.coords(z)[1]
        
        #posx1 <= posx2 and posx2+37 <= posx1 and posy1<= posy2 and posy2 <= posy1 + 50

        if(posx1>=posx2 and posx1<=posx2+28 and posy1>=posy2 and posy1<=posy2+50 or(posx1+28>=posx2 and posx1+28<=posx2+28 and posy1>=posy2 and posy1<=posy2+50) ):
            print("crash")
            l=x
            x = can4.create_image(can4.coords(l)[0],can4.coords(l)[1],image=carroc)
            can4.delete(l)
            can4.move(z,menos-can4.coords(z)[0],-can4.coords(z)[1])
            nvl4.after(10,mininvl4)
            contgasonvl4=contgasonvl4-2
            contvelocidad=0
            c=0
            can4.move(y,0,-can4.coords(y)[1])
        else:
            contadormini=0
            nvl4.after(10,mininvl4)
def mininvl44():
    """
    Esta funcion mueve la minivan del segundo mapa
    """
    
    global nvl4,y,p,c2player,can4,contadormini2,x2,contgasonvl44,contvelocidad22,min2
    menos2=random.randint(700,970)
    if(c2player<240):
        can4.move(min2,0,8)
        c2player = c2player + 1
        
    if(c2player==240):
        #c1.delete(z)
        can4.move(min2,menos2-can4.coords(min2)[0],-can4.coords(min2)[1])
        c2player = 0
        #z=c1.create_image(500,-50,image=minivan)

    if(contadormini2<950):#250
        
        contadormini2 = contadormini2 + 1
        posx1m = can4.coords(x2)[0]
        posy1m = can4.coords(x2)[1]
        posx2m = can4.coords(min2)[0]
        posy2m = can4.coords(min2)[1]
        
        #posx1 <= posx2 and posx2+37 <= posx1 and posy1<= posy2 and posy2 <= posy1 + 50

        if(posx1m>=posx2m and posx1m<=posx2m+28 and posy1m>=posy2m and posy1m<=posy2m+50 or(posx1m+28>=posx2m and posx1m+28<=posx2m+28 and posy1m>=posy2m and posy1m<=posy2m+50) ):
            print("crash")
            l3=x2
            x2 = can4.create_image(can4.coords(l3)[0],can4.coords(l3)[1],image=carroc)
            can4.delete(l3)
            can4.move(min2,menos2-can4.coords(min2)[0],-can4.coords(min2)[1])
            nvl4.after(10,mininvl44)
            contgasonvl44=contgasonvl44-2
            contvelocidad22=0
            c2player=0
            can4.move(y2,0,-can4.coords(y2)[1])
        else:
            contadormini2=0
            nvl4.after(10,mininvl44)


###---------------------------------------------------------------minivan
###-----------------------------------------------------------------------------gasolina
def gasolinanvl4():
    """
    con esta funcion se crea el label de la gasolina
    """
    global gaso,nvl4,lbl3,contgasonvl4,can4
    
    
    if(contgasonvl4>0):
        gaso.set(str(contgasonvl4)+" "+"G")
        contgasonvl4=contgasonvl4-1
    can4.after(1000,gasolinanvl4)
    if(contgasonvl4==0):
        nvl4.destroy()
        print("2 win")
    
def gasolinanvl44():
    """
    con esta funcion se crea el label de la gasolina
    """
    global gaso22,nvl4,contgasonvl44
    
    
    if(contgaso22>0):
        gaso22.set(str(contgasonvl44)+" "+ "G")
        contgasonvl44=contgasonvl44-1
    can4.after(1000,gasolinanvl44)
    if(contgasonvl44==0):
        nvl4.destroy()
        print("1 win")

###-----------------------------------------------------------------------------gasolina
###-----------------------------------------------------------------------------puntos
####puntos
def puntosnvl4():
    """
    control de puntos
    """
    global nvl4,contpuntosnvl4,puntos,lblpuntos
    if(contpuntosnvl4>=0):
        puntos.set(str(contpuntosnvl4)+ " "+"M")
        contpuntosnvl4=contpuntosnvl4+1
    can4.after(10,puntosnvl4)

def puntosnvl44():
    """
    control de puntos
    """
    global nvl4,contpuntosnvl44,puntos22,lblpuntos
    if(contpuntosnvl44>=0):
        puntos22.set(str(contpuntosnvl44)+" "+"M")
        contpuntosnvl44=contpuntosnvl44+1
    can4.after(10,puntosnvl44)

###------------------------------------------------------------------------puntos
###--------------------------------------------------------------------------velocidad
####velocidad
def velocidadnvl4():
    """
    funcion para el label de velocidad
    """
    global nvl4,contvelocidad,velocidad,lblvelocidad
    if(contvelocidad>=0 and contvelocidad<=180):
        velocidad.set(str(contvelocidad)+ " "+ "KM/H")
        contvelocidad=contvelocidad+1
    can4.after(100,velocidadnvl4)
def velocidadnvl44():
    """
    funcion para el label de velocidad
    """
    global nvl4,contvelocidad22,velocidad22,lblvelocidad
    if(contvelocidad22>=0 and contvelocidad22<=180):
        velocidad22.set(str(contvelocidad22)+" "+"KM/H")
        contvelocidad22=contvelocidad22+1
    can4.after(100,velocidadnvl44)

###---------------------------------------------------------------------------velocidad
###--------------------------------------------------------------------fondo
def fonditonvl4():
    """
    """
    global can4,nvl4
    c22=0
    c32=0
    if(c22<5):
        can4.move(y,0,1.5)
        c22=c22+1
        c32=c32+1
    if(can4.coords(y)[1]>=10000):
        c22=0
        can4.move(y,0,-can4.coords(y)[1])
    nvl4.after(1,fonditonvl4)
    
        
def fonditonvl44():
    """
    """
    global can4,nvl4
    c222=0
    c322=0
    if(c222<5):
        can4.move(y2,0,1.5)
        c222=c222+1
        c322=c322+1
        
    if(can4.coords(y2)[1]>=10000):
        c222=0
        can4.move(y2,0,-can4.coords(y2)[1])
    nvl4.after(1,fonditonvl44)
###------------------------------------------------------------------fondo
###---------------------------------------------------------------------runner
####enemigo runner
def runernvl4():#mover runner
    """
    esta funcion es para mover el runer
    """
    global a,ref1,direccion,contgasonvl4,contvelocidad,contadorruner,x
    menosruner=random.randint(280,500)
    if(can4.coords(a)[0]>=250):
            direccion=direccion*(-1)
            
    if(can4.coords(a)[0]<=550):
            direccion=direccion*(-1)
    if(can4.coords(x)[1]==can4.coords(a)[1]):
        can4.move(a,menosruner-can4.coords(a)[0],-can4.coords(a)[1])
    can4.move(a,direccion*5,2)
    #nvl1.after(10,runer)
    if(contadorruner<950):#250
        
        contadorruner = contadorruner + 1
        posx1r = can4.coords(x)[0]
        posy1r = can4.coords(x)[1]
        posx2r = can4.coords(a)[0]
        posy2r = can4.coords(a)[1]
        
        #posx1 <= posx2 and posx2+37 <= posx1 and posy1<= posy2 and posy2 <= posy1 + 50

        if(posx1r>=posx2r and posx1r<=posx2r+28 and posy1r>=posy2r and posy1r<=posy2r+50 or(posx1r+28>=posx2r and posx1r+28<=posx2r+28 and posy1r>=posy2r and posy1r<=posy2r+50) ):
            print("crash")
            l=x
            x = can4.create_image(can4.coords(l)[0],can4.coords(l)[1],image=carroc)
            can4.delete(l)
            can4.move(a,menosruner-can4.coords(a)[0],-can4.coords(a)[1])
            nvl4.after(10,runernvl4)
            contgasonvl4=contgasonvl4-2
            contvelocidad=0
            can4.move(y,0,-can4.coords(y)[1])
        else:
            contadorruner=0
            nvl4.after(10,runernvl4)
    


def runernvl44():
    """
runer del nivel 2
    """
    global run2,ref1,direccion2,contadorruner2,x2,contgasonvl44,contvelocidad22
    menosruner2=random.randint(700,980)
    if(can4.coords(run2)[0]>=700):
            direccion2=direccion2*(-1)
            
    if(can4.coords(run2)[0]<=980):
            direccion2=direccion2*(-1)
    if(can4.coords(x)[1]==can4.coords(run2)[1]):
        can4.move(run2,menosruner2-can4.coords(run2)[0],-can4.coords(run2)[1])
    can4.move(run2,direccion2*5,2)
    if(contadorruner<950):#250
        
        contadorruner2 = contadorruner2 + 1
        posx1r2 = can4.coords(x2)[0]
        posy1r2 = can4.coords(x2)[1]
        posx2r2 = can4.coords(run2)[0]
        posy2r2 = can4.coords(run2)[1]
        
        #posx1 <= posx2 and posx2+37 <= posx1 and posy1<= posy2 and posy2 <= posy1 + 50

        if(posx1r2>=posx2r2 and posx1r2<=posx2r2+28 and posy1r2>=posy2r2 and posy1r2<=posy2r2+50 or(posx1r2+28>=posx2r2 and posx1r2+28<=posx2r2+28 and posy1r2>=posy2r2 and posy1r2<=posy2r2+50) ):
            print("crash")
            l4=x2
            x2 = can4.create_image(can4.coords(l4)[0],can4.coords(l4)[1],image=carroc)
            can4.delete(l4)
            can4.move(run2,menosruner2-can4.coords(run2)[0],-can4.coords(run2)[1])
            nvl4.after(10,runernvl44)
            contgasonvl44=contgasonvl44-2
            contvelocidad22=0
            can4.move(y2,0,-can4.coords(y2)[1])
        else:
            contadorruner2=0
            nvl4.after(10,runernvl44)
    

###-------------------------------------------------------------------runner
######--------------------------------------------------------------fighter
            
def fighterrnvl4():
    """
    esta funcion es para mover el fighter
    """
    
    global fight,reloadfighter,x,contgasonvl4,contvelocidad,y
    menosfighter=random.randint(280,500)
    if(can4.coords(x)[0]<can4.coords(fight)[0]):
        can4.move(fight,-1.4,2)
    elif(can4.coords(x)[0]>can4.coords(fight)[0]):
        can4.move(fight,1.4,2)
    else:
        can4.move(fight,0,4)
    if(can4.coords(x)[1]==can4.coords(fight)[1]):
        can4.move(fight,menosfighter-can4.coords(fight)[0],-can4.coords(fight)[1])
        #fight=c1.create_image(500,50,image=fighter)
        
    if(reloadfighter<950):#250
        
        reloadfighter = reloadfighter + 1
        posx11 = can4.coords(x)[0]
        posy11 = can4.coords(x)[1]
        posx22 = can4.coords(fight)[0]
        posy22 = can4.coords(fight)[1]
        
        #posx1 <= posx2 and posx2+37 <= posx1 and posy1<= posy2 and posy2 <= posy1 + 50

        if(posx11>=posx22 and posx11<=posx22+28 and posy11>=posy22 and posy11<=posy22+50 or(posx11+28>=posx22 and posx11+28<=posx22+28 and posy11>=posy22 and posy11<=posy22+50) ):
            print("crash")
            l2=x
            x = can4.create_image(can4.coords(l2)[0],can4.coords(l2)[1],image=carroc)
            can4.delete(l2)
            can4.move(fight,menosfighter-can4.coords(fight)[0],-can4.coords(fight)[1])
            nvl4.after(10,fighterrnvl4)
            contgasonvl4=contgasonvl4-2
            contvelocidad=0
            can4.move(y,0,-can4.coords(y)[1])
        else:
            reloadfighter=0
            nvl4.after(10,fighterrnvl4)

def fighterrnvl44():
    """
    esta funcion es para mover el fighter
    """
    
    global fight2,reloadfighter2,x2,contgasonvl44,contvelocidad22,y
    menosfighter2=random.randint(700,1000)
    if(can4.coords(x2)[0]<can4.coords(fight2)[0]):
        can4.move(fight2,-1.4,2)
    elif(can4.coords(x2)[0]>can4.coords(fight2)[0]):
        can4.move(fight2,1.4,2)
    else:
        can4.move(fight2,0,4)
    if(can4.coords(x2)[1]==can4.coords(fight2)[1]):
        can4.move(fight2,menosfighter2-can4.coords(fight2)[0],-can4.coords(fight2)[1])
        #fight=c1.create_image(500,50,image=fighter)
        
    if(reloadfighter2<950):#250
        
        reloadfighter2 = reloadfighter2 + 1
        posx11f = can4.coords(x2)[0]
        posy11f = can4.coords(x2)[1]
        posx22f= can4.coords(fight2)[0]
        posy22f = can4.coords(fight2)[1]
        
        #posx1 <= posx2 and posx2+37 <= posx1 and posy1<= posy2 and posy2 <= posy1 + 50

        if(posx11f>=posx22f and posx11f<=posx22f+28 and posy11f>=posy22f and posy11f<=posy22f+50 or(posx11f+28>=posx22f and posx11f+28<=posx22f+28 and posy11f>=posy22f and posy11f<=posy22f+50) ):
            print("crash")
            l22=x2
            x2 = can4.create_image(can4.coords(l22)[0],can4.coords(l22)[1],image=carroc)
            can4.delete(l22)
            can4.move(fight2,menosfighter2-can4.coords(fight2)[0],-can4.coords(fight2)[1])
            nvl4.after(10,fighterrnvl44)
            contgasonvl44=contgasonvl44-2
            contvelocidad22=0
            can4.move(y2,0,-can4.coords(y2)[1])
        else:
            reloadfighter2=0
            nvl4.after(10,fighterrnvl44)
        
        
    

####---------------------------------------------------fighter
####----------------------------------------------------mancha
def manchitanvl4():#mover minivan
    """
    mancha de aceite
    """
    
    global nvl4,y,p,c,z,can4,contadormini,x,contgasonvl4,contvelocidad,aceite,contaceite,resbalar
    menosaceite=random.randint(280,500)
    if(contaceite<340):
        can4.move(aceite,0,5)
        contaceite = contaceite + 1
        
    if(contaceite==340):
        #c1.delete(z)
        can4.move(aceite,menosaceite-can4.coords(aceite)[0],-can4.coords(aceite)[1])
        contaceite = 0

    if(resbalar<950):#250
        
        resbalar = resbalar + 1
        posx1x = can4.coords(x)[0]
        posy1x = can4.coords(x)[1]
        posx2a = can4.coords(aceite)[0]
        posy2a = can4.coords(aceite)[1]
        
        #posx1 <= posx2 and posx2+37 <= posx1 and posy1<= posy2 and posy2 <= posy1 + 50

        if(posx1x>=posx2a and posx1x<=posx2a+28 and posy1x>=posy2a and posy1x<=posy2a+50 or(posx1x+28>=posx2a and posx1x+28<=posx2a+28 and posy1x>=posy2a and posy1x<=posy2a+50) ):
            print("crash")
            l1=x
            can4.move(l1,-80,0)
            x = can4.create_image(can4.coords(l1)[0],can4.coords(l1)[1],image=carroc)
            can4.delete(l1)
            can4.move(aceite,menosaceite-can4.coords(aceite)[0],-can4.coords(aceite)[1])
            nvl4.after(10,manchitanvl4)
            contgasonvl4=contgasonvl4-2
            contvelocidad=0
            contaceite=0
            can4.move(y,0,-can4.coords(y)[1])
        else:
            resbalar=0
            nvl4.after(10,manchitanvl4)
            
def manchitanvl44():#mover minivan
    """
    mancha de aceite 2
    """
    
    global nvl4,y,p,can4,x2,contgasonvl44,contvelocidad22,aceite2,contaceite2,resbalar2
    menosaceite2=random.randint(700,970)
    if(contaceite2<340):
        can4.move(aceite2,0,5)
        contaceite2 = contaceite2 + 1
        
    if(contaceite2==340):
        #c1.delete(z)
        can4.move(aceite2,menosaceite2-can4.coords(aceite2)[0],-can4.coords(aceite2)[1])
        contaceite2 = 0

    if(resbalar2<950):#250
        
        resbalar2 = resbalar2 + 1
        posx1xm2 = can4.coords(x2)[0]
        posy1xm2 = can4.coords(x2)[1]
        posx2am2 = can4.coords(aceite2)[0]
        posy2am2 = can4.coords(aceite2)[1]
        
        #posx1 <= posx2 and posx2+37 <= posx1 and posy1<= posy2 and posy2 <= posy1 + 50

        if(posx1xm2>=posx2am2 and posx1xm2<=posx2am2+28 and posy1xm2>=posy2am2 and posy1xm2<=posy2am2+50 or(posx1xm2+28>=posx2am2 and posx1xm2+28<=posx2am2+28 and posy1xm2>=posy2am2 and posy1xm2<=posy2am2+50) ):
            print("crash")
            l13=x2
            can4.move(l13,-80,0)
            x2 = can4.create_image(can4.coords(l13)[0],can4.coords(l13)[1],image=carroc)
            can4.delete(l13)
            can4.move(aceite2,menosaceite2-can4.coords(aceite2)[0],-can4.coords(aceite2)[1])
            nvl4.after(10,manchitanvl44)
            contgasonvl44=contgasonvl44-2
            contvelocidad22=0
            contaceite2=0
            can4.move(y2,0,-can4.coords(y2)[1])
        else:
            resbalar2=0
            nvl4.after(10,manchitanvl44)


####--------------------------------------------------mancha
###-----------------------------------------------------------nyan
def podernvl4 ():
    """
    esta funcion es para mover el gato de la gasolina
    """
    global nvl4,y,p,c,z,can4,contadormini,x,contgasonvl4,contvelocidad,contadorpoder,reloadpoder,nyan
    menospoder=random.randint(280,500)
    if(contadorpoder<500):
        can4.move(nyan,0,6)
        contadorpoder = contadorpoder + 1
        
    if(contadorpoder==500):
        contadorpoder=0
        can4.move(nyan,menospoder-can4.coords(nyan)[0],-can4.coords(nyan)[1])

    if(reloadpoder<950):#250
        
        reloadpoder = reloadpoder + 1
        posx1ny = can4.coords(x)[0]
        posy1ny = can4.coords(x)[1]
        posx2ny = can4.coords(nyan)[0]
        posy2ny = can4.coords(nyan)[1]
        
        #posx1 <= posx2 and posx2+37 <= posx1 and posy1<= posy2 and posy2 <= posy1 + 50

        if(posx1ny>=posx2ny and posx1ny<=posx2ny+28 and posy1ny>=posy2ny and posy1ny<=posy2ny+50 or(posx1ny+28>=posx2ny and posx1ny+28<=posx2ny+28 and posy1ny>=posy2ny and posy1ny<=posy2ny+50) ):
            print("crash")
            can4.move(nyan,menospoder-can4.coords(nyan)[0],can4.coords(nyan)[1]-500)
            nvl4.after(10,podernvl4)
            contgasonvl4=contgasonvl4+2
            contadorpoder=0
        else:
            reloadpoder=0
            nvl4.after(10,podernvl4)
    
def podernvl44 ():
    """
    esta funcion es para mover el gato de la gasolina
    """
    global nvl4,y,p,c,z,can4,contadormini,x,contgasonvl44,contvelocidad,contadorpoder2,reloadpoder2,nyan2
    menospoder2=random.randint(700,980)
    if(contadorpoder2<500):
        can4.move(nyan2,0,6)
        contadorpoder2 = contadorpoder2 + 1
        
    if(contadorpoder2==500):
        contadorpoder2=0
        can4.move(nyan2,menospoder2-can4.coords(nyan2)[0],-can4.coords(nyan2)[1])

    if(reloadpoder2<950):#250
        
        reloadpoder2 = reloadpoder2 + 1
        posx1ny2 = can4.coords(x2)[0]
        posy1ny2 = can4.coords(x2)[1]
        posx2ny2 = can4.coords(nyan2)[0]
        posy2ny2 = can4.coords(nyan2)[1]
        
        #posx1 <= posx2 and posx2+37 <= posx1 and posy1<= posy2 and posy2 <= posy1 + 50

        if(posx1ny2>=posx2ny2 and posx1ny2<=posx2ny2+28 and posy1ny2>=posy2ny2 and posy1ny2<=posy2ny2+50 or(posx1ny2+28>=posx2ny2 and posx1ny2+28<=posx2ny2+28 and posy1ny2>=posy2ny2 and posy1ny2<=posy2ny2+50) ):
            print("crash")
            can4.move(nyan2,menospoder2-can4.coords(nyan2)[0],can4.coords(nyan2)[1]-500)
            nvl4.after(10,podernvl44)
            contgasonvl44=contgasonvl44+2
            contadorpoder2=0
        else:
            reloadpoder2=0
            nvl4.after(10,podernvl44)    

###-------------------------------------------------------------nyan



###-----------------------------------------------------------------------------------------------------------nivel4
###---mapa
mapa5=tkinter.PhotoImage(file="mapa5555.png")#imagen del mapa

###---mapa

###-----------------------------------------------------------------------------------------------------------nivel5
    
def nivel5(): # Abrir la ventana del nivel 5, fusionar funcion de guardado a precionar nivel 5
    """
    Esta funcion es para abrir una nueva ventana, que abre el mapa del nivel 5
    """
    global can5,nvl5,mapa2,x,x2,z,gaso,gaso22,puntos,puntos22,velocidad,min2,y,y2,a,run2,fight,fight2,aceite,aceite2,nyan,nyan2
    nvl5 = tkinter.Toplevel(w0)#crear la ventana del nivel 2
    w0.iconify()
    nvl5.geometry("1200x850")#dimensiones de la ventana
    can5=tkinter.Canvas(nvl5,bg="black", width=1600, height=800)#canvas del nivel 2
    can5.pack()
    y=can5.create_image(400,400,image=mapa5)#mapa del nivel 2
    y2=can5.create_image(847,400,image=mapa5)
    can5.lower(y)
    can5.lower(y2)
    #label gasolina, jugadores, puntos
    lbl3=tkinter.Label(nvl5,textvariable= gaso,fg="white",bg="black", underline=True,font=("",16,"bold")).place(x=50,y=62)#GASOLINA 1
    lblgaso2=tkinter.Label(nvl5,textvariable= gaso22,fg="white",bg="black", underline=True,font=("",16,"bold")).place(x=50,y=430)#gasolina 2
    lbljugador1=tkinter.Label(nvl5,text=j1.get(),fg="white",bg="black",font=("Arial",14)).place(x=50,y=10)
    lbljugador2=tkinter.Label(nvl5,text=j2.get(),fg="white",bg="black",font=("Arial",14)).place(x=50,y=400)
    lblpuntos=tkinter.Label(nvl5,textvariable=puntos,fg="white",bg="black",font=("",16,"bold")).place(x=50,y=100)#puntos 1
    lblpuntos2=tkinter.Label(nvl5,textvariable=puntos22,fg="white",bg="black",font=("",16,"bold")).place(x=50,y=460)#puntos 2
    lblvelocidad=tkinter.Label(nvl5,textvariable=velocidad,fg="white",bg="black",font=("",16,"bold")).place(x=50,y=130)# velocidad 1
    lblvelocidad2=tkinter.Label(nvl5,textvariable=velocidad22,fg="white",bg="black",font=("",16,"bold")).place(x=50,y=490)#velocidad 2
    ##cargar imagenes del player y los enemigos
    x= can5.create_image(400,750,image=carro)#imagen carro
    a=can5.create_image(400,170,image=runner)#imagen runner
    z=can5.create_image(500,-50,image=minivan)#imagen minivan
    fight=can5.create_image(500,50,image=fighter)#imagen fighter
    aceite=can5.create_image(480,30,image=mancha)#aceite del 1
    nyan=can5.create_image(450,50,image=imagengasolina)#nyan 1
    ##2 pantalla
    x2=can5.create_image(830,750,image=carro)#imagen carro 2
    nyan2=can5.create_image(770,50,image=imagengasolina)#nyan 2
    min2=can5.create_image(830,-50,image=minivan)#minivan dos
    fight2=can5.create_image(750,50,image=fighter)#fighter 2
    run2=can5.create_image(730,50,image=runner)#imagen runner
    aceite2=can5.create_image(770,30,image=mancha)#aceite del 1
    can5.bind("<KeyPress>", keydown)
    can5.bind("<KeyRelease>", keyup)
    can5.focus_set()
    #funciones
    gasolinanvl5()
    gasolinanvl55()
    mininvl5()
    mininvl55()
    puntosnvl5()
    puntosnvl55()
    velocidadnvl5()
    velocidadnvl55()
    fonditonvl5()
    fonditonvl55()
    runernvl5()
    runernvl55()
    fighterrnvl5()
    fighterrnvl55()
    manchitanvl5()
    manchitanvl55()
    podernvl5()
    podernvl55()
    keyy5()
    
###-------------------------------------------------------------players
def keyy5():
    global h, playernvl2,i,j,y,i2,x2,nvl5,playernvl22,x,can5
    if(68 in h):
        if(i<150):
            can5.delete(x)
            i = i + 3
            x = can5.create_image(400+i,750+j,image=carro)
        #else:
            #c1.delete(x)
            #x = c1.create_image(400+i,750+j,image=carroc) 
    if(65 in h):
        if(i > -140):
            can5.delete(x)
            i = i - 3
            x = can5.create_image(400+i,750+j,image=carro)
        #else:
            #c1.delete(x)
            #x = c1.create_image(400+i,750+j,image=carroc)
    if(76 in h):
        if(i2 < 160):
            can5.delete(x2)
            i2 = i2 + 3
            x2 = can5.create_image(830+i2,750+j,image=carro)
        #else:
            #c1.delete(x2)
            #x2 = c1.create_image(830+i2,750+j,image=carroc)
    if(74 in h):
        if(i2 > -130):
             can5.delete(x2)
             i2 = i2 - 3
             x2 = can5.create_image(830+i2,750+j,image=carro)
       # else:
             #c1.delete(x2)
             #x2 = c1.create_image(830+i2,750+j,image=carroc)
    if(32 in h):
        guardar5()
    nvl5.after(10,keyy5)




###-------------------------------------------------------------players
###contadores
contgasonvl5=60
contgasonvl55=60
contpuntosnvl5=0
contpuntosnvl55=0
###contadores
####----------------------------------------------------------------------------guardar y cargar
def guardar5():
    """
    """
    global h,x,j,i,y,i2,x2,contgasonvl5,contgasonvl55,contpuntosnvl5,contpuntosnvl55,can5,archivo
    archivo = open("partida5.txt", "w")
    posix1=can5.coords(x)[0]
    posix11=can5.coords(x)[1]
    posix2=can5.coords(x2)[0]
    posix22=can5.coords(x2)[1]
    if(contgasonvl5>0 and contgasonvl55>0):  
            archivo.write(str(contgasonvl5)+"\n")
            archivo.write(str(contpuntosnvl5)+"\n")
            archivo.write(str(contgasonvl55)+"\n")
            archivo.write(str(contpuntosnvl55)+"\n")
            archivo.write(str(posix1)+"\n")
            archivo.write(str(posix11)+"\n")
            archivo.write(str(posix2)+"\n")
            archivo.write(str(posix22)+"\n")
    
    
    archivo.close()
   
    
def cargar5():
    """
    """
    global h,x,j,i,y,i2,x2,contgasonvl5,contgasonvl55,contpuntosnvl5,contpuntosnvl55,can5,archivo
    archivo=open("partida5.txt","r")
    
    linea1 = archivo.readline()
    print(linea1)
    linea2=archivo.readline()
    print(linea2)
    linea3 = archivo.readline()
    print(linea3)
    linea4=archivo.readline()
    print(linea4)
    linea5 = archivo.readline()
    print(linea5)
    linea6=archivo.readline()
    print(linea6)
    linea7 = archivo.readline()
    print(linea7)
    linea8=archivo.readline()
    print(linea8)
    nivel5()
    juga1=can5.coords(x)[0]
    juga11=can5.coords(x)[1]
    juga2=can5.coords(x2)[0]
    juga22=can5.coords(x2)[1]
    contgasonvl5=int(linea1)
    contpuntosnvl5=int(linea2)
    contgasonvl55=int(linea3)
    contpuntosnvl55=int(linea4)
    juga1=float(linea5)
    juga11=float(linea6)
    juga2=float(linea7)
    juga22=float(linea8)
    
    archivo.close()

###------------------------------------------------guardar y cargar

###-------------------------------------------------------------minivan
def mininvl5():#mover minivan
    """
    Esta funcion mueve la minivan
    """
    
    global nvl5,y,p,c,z,can5,contadormini,x,contgasonvl5,contvelocidad
    menos=random.randint(280,500)
    if(c<180):
        can5.move(z,0,12)
        c = c + 1
        
    if(c==180):
        #c1.delete(z)
        
        can5.move(z,menos-can5.coords(z)[0],-can5.coords(z)[1])
        c = 0
        #z=c1.create_image(500,-50,image=minivan)

    if(contadormini<950):#250
        
        contadormini = contadormini + 1
        posx1 = can5.coords(x)[0]
        posy1 = can5.coords(x)[1]
        posx2 = can5.coords(z)[0]
        posy2 = can5.coords(z)[1]
        
        #posx1 <= posx2 and posx2+37 <= posx1 and posy1<= posy2 and posy2 <= posy1 + 50

        if(posx1>=posx2 and posx1<=posx2+28 and posy1>=posy2 and posy1<=posy2+50 or(posx1+28>=posx2 and posx1+28<=posx2+28 and posy1>=posy2 and posy1<=posy2+50) ):
            print("crash")
            l=x
            x = can5.create_image(can5.coords(l)[0],can5.coords(l)[1],image=carroc)
            can5.delete(l)
            can5.move(z,menos-can5.coords(z)[0],-can5.coords(z)[1])
            nvl5.after(10,mininvl5)
            contgasonvl5=contgasonvl5-2
            contvelocidad=0
            c=0
            can5.move(y,0,-can5.coords(y)[1])
        else:
            contadormini=0
            nvl5.after(10,mininvl5)
def mininvl55():
    """
    Esta funcion mueve la minivan del segundo mapa
    """
    
    global nvl5,y,p,c2player,can5,contadormini2,x2,contgasonvl55,contvelocidad22,min2
    menos2=random.randint(700,970)
    if(c2player<180):
        can5.move(min2,0,12)
        c2player = c2player + 1
        
    if(c2player==180):
        #c1.delete(z)
        can5.move(min2,menos2-can5.coords(min2)[0],-can5.coords(min2)[1])
        c2player = 0
        #z=c1.create_image(500,-50,image=minivan)

    if(contadormini2<950):#250
        
        contadormini2 = contadormini2 + 1
        posx1m = can5.coords(x2)[0]
        posy1m = can5.coords(x2)[1]
        posx2m = can5.coords(min2)[0]
        posy2m = can5.coords(min2)[1]
        
        #posx1 <= posx2 and posx2+37 <= posx1 and posy1<= posy2 and posy2 <= posy1 + 50

        if(posx1m>=posx2m and posx1m<=posx2m+28 and posy1m>=posy2m and posy1m<=posy2m+50 or(posx1m+28>=posx2m and posx1m+28<=posx2m+28 and posy1m>=posy2m and posy1m<=posy2m+50) ):
            print("crash")
            l3=x2
            x2 = can5.create_image(can5.coords(l3)[0],can5.coords(l3)[1],image=carroc)
            can5.delete(l3)
            can5.move(min2,menos2-can5.coords(min2)[0],-can5.coords(min2)[1])
            nvl5.after(10,mininvl55)
            contgasonvl55=contgasonvl55-2
            contvelocidad22=0
            c2player=0
            can5.move(y2,0,-can5.coords(y2)[1])
        else:
            contadormini2=0
            nvl5.after(10,mininvl55)


###---------------------------------------------------------------minivan

###-----------------------------------------------------------------------------gasolina
def gasolinanvl5():
    """
    con esta funcion se crea el label de la gasolina
    """
    global gaso,nvl5,lbl3,contgasonvl5,can5
    
    
    if(contgasonvl5>0):
        gaso.set(str(contgasonvl5)+" "+"G")
        contgasonvl5=contgasonvl5-1
    can5.after(1000,gasolinanvl5)
    if(contgasonvl5==0):
        nvl5.destroy()
        print("2 win")
    
def gasolinanvl55():
    """
    con esta funcion se crea el label de la gasolina
    """
    global gaso22,nvl5,contgasonvl55
    
    
    if(contgasonvl55>0):
        gaso22.set(str(contgasonvl55)+" "+ "G")
        contgasonvl55=contgasonvl55-1
    can5.after(1000,gasolinanvl55)
    if(contgasonvl55==0):
        nvl5.destroy()
        print("1 win")

###-----------------------------------------------------------------------------gasolina
###-----------------------------------------------------------------------------puntos
####puntos
def puntosnvl5():
    """
    control de puntos
    """
    global nvl5,contpuntosnvl5,puntos,lblpuntos
    if(contpuntosnvl5>=0):
        puntos.set(str(contpuntosnvl5)+ " "+"M")
        contpuntosnvl5=contpuntosnvl5+1
    can5.after(10,puntosnvl5)

def puntosnvl55():
    """
    control de puntos
    """
    global nvl5,contpuntosnvl55,puntos22,lblpuntos
    if(contpuntosnvl55>=0):
        puntos22.set(str(contpuntosnvl55)+" "+"M")
        contpuntosnvl55=contpuntosnvl55+1
    can5.after(10,puntosnvl55)

###------------------------------------------------------------------------puntos

###--------------------------------------------------------------------------velocidad
####velocidad
def velocidadnvl5():
    """
    funcion para el label de velocidad
    """
    global nvl5,contvelocidad,velocidad,lblvelocidad
    if(contvelocidad>=0 and contvelocidad<=180):
        velocidad.set(str(contvelocidad)+ " "+ "KM/H")
        contvelocidad=contvelocidad+1
    can5.after(100,velocidadnvl5)
def velocidadnvl55():
    """
    funcion para el label de velocidad
    """
    global nvl5,contvelocidad22,velocidad22,lblvelocidad
    if(contvelocidad22>=0 and contvelocidad22<=180):
        velocidad22.set(str(contvelocidad22)+" "+"KM/H")
        contvelocidad22=contvelocidad22+1
    can5.after(100,velocidadnvl55)

###---------------------------------------------------------------------------velocidad
###--------------------------------------------------------------------fondo
def fonditonvl5():
    """
    """
    global can5,nvl5
    c22=0
    c32=0
    if(c22<5):
        can5.move(y,0,1.5)
        c22=c22+1
        c32=c32+1
    if(can5.coords(y)[1]>=10000):
        c22=0
        can5.move(y,0,-can5.coords(y)[1])
    nvl5.after(1,fonditonvl5)
    
        
def fonditonvl55():
    """
    """
    global can5,nvl5
    c222=0
    c322=0
    if(c222<5):
        can5.move(y2,0,1.5)
        c222=c222+1
        c322=c322+1
        
    if(can5.coords(y2)[1]>=10000):
        c222=0
        can5.move(y2,0,-can5.coords(y2)[1])
    nvl5.after(1,fonditonvl55)
###------------------------------------------------------------------fondo


###---------------------------------------------------------------------runner
####enemigo runner
def runernvl5():#mover runner
    """
    esta funcion es para mover el runer
    """
    global a,ref1,direccion,contgasonvl5,contvelocidad,contadorruner,x
    menosruner=random.randint(280,500)
    if(can5.coords(a)[0]>=250):
            direccion=direccion*(-1)
            
    if(can5.coords(a)[0]<=550):
            direccion=direccion*(-1)
    if(can5.coords(x)[1]==can5.coords(a)[1]):
        can5.move(a,menosruner-can5.coords(a)[0],-can5.coords(a)[1])
    can5.move(a,direccion*9,5)
    #nvl1.after(10,runer)
    if(contadorruner<950):#250
        
        contadorruner = contadorruner + 1
        posx1r = can5.coords(x)[0]
        posy1r = can5.coords(x)[1]
        posx2r = can5.coords(a)[0]
        posy2r = can5.coords(a)[1]
        
        #posx1 <= posx2 and posx2+37 <= posx1 and posy1<= posy2 and posy2 <= posy1 + 50

        if(posx1r>=posx2r and posx1r<=posx2r+28 and posy1r>=posy2r and posy1r<=posy2r+50 or(posx1r+28>=posx2r and posx1r+28<=posx2r+28 and posy1r>=posy2r and posy1r<=posy2r+50) ):
            print("crash")
            l=x
            x = can5.create_image(can5.coords(l)[0],can5.coords(l)[1],image=carroc)
            can5.delete(l)
            can5.move(a,menosruner-can5.coords(a)[0],-can5.coords(a)[1])
            nvl5.after(10,runernvl5)
            contgasonvl5=contgasonvl5-2
            contvelocidad=0
            can5.move(y,0,-can5.coords(y)[1])
        else:
            contadorruner=0
            nvl5.after(10,runernvl5)
    


def runernvl55():
    """
runer del nivel 2
    """
    global run2,ref1,direccion2,contadorruner2,x2,contgasonvl55,contvelocidad22
    menosruner2=random.randint(700,980)
    if(can5.coords(run2)[0]>=700):
            direccion2=direccion2*(-1)
            
    if(can5.coords(run2)[0]<=980):
            direccion2=direccion2*(-1)
    if(can5.coords(x)[1]==can5.coords(run2)[1]):
        can5.move(run2,menosruner2-can5.coords(run2)[0],-can5.coords(run2)[1])
    can5.move(run2,direccion2*9,5)
    if(contadorruner<950):#250
        
        contadorruner2 = contadorruner2 + 1
        posx1r2 = can5.coords(x2)[0]
        posy1r2 = can5.coords(x2)[1]
        posx2r2 = can5.coords(run2)[0]
        posy2r2 = can5.coords(run2)[1]
        
        #posx1 <= posx2 and posx2+37 <= posx1 and posy1<= posy2 and posy2 <= posy1 + 50

        if(posx1r2>=posx2r2 and posx1r2<=posx2r2+28 and posy1r2>=posy2r2 and posy1r2<=posy2r2+50 or(posx1r2+28>=posx2r2 and posx1r2+28<=posx2r2+28 and posy1r2>=posy2r2 and posy1r2<=posy2r2+50) ):
            print("crash")
            l4=x2
            x2 = can5.create_image(can5.coords(l4)[0],can5.coords(l4)[1],image=carroc)
            can5.delete(l4)
            can5.move(run2,menosruner2-can5.coords(run2)[0],-can5.coords(run2)[1])
            nvl5.after(10,runernvl55)
            contgasonvl55=contgasonvl55-2
            contvelocidad22=0
            can5.move(y2,0,-can5.coords(y2)[1])
        else:
            contadorruner2=0
            nvl5.after(10,runernvl55)
    

###-------------------------------------------------------------------runner
######--------------------------------------------------------------fighter
            
def fighterrnvl5():
    """
    esta funcion es para mover el fighter
    """
    
    global fight,reloadfighter,x,contgasonvl5,contvelocidad,y
    menosfighter=random.randint(280,500)
    if(can5.coords(x)[0]<can5.coords(fight)[0]):
        can5.move(fight,-1.8,2)
    elif(can5.coords(x)[0]>can5.coords(fight)[0]):
        can5.move(fight,1.8,2)
    else:
        can5.move(fight,0,7)
    if(can5.coords(x)[1]==can5.coords(fight)[1]):
        can5.move(fight,menosfighter-can5.coords(fight)[0],-can5.coords(fight)[1])
        #fight=c1.create_image(500,50,image=fighter)
        
    if(reloadfighter<950):#250
        
        reloadfighter = reloadfighter + 1
        posx11 = can5.coords(x)[0]
        posy11 = can5.coords(x)[1]
        posx22 = can5.coords(fight)[0]
        posy22 = can5.coords(fight)[1]
        
        #posx1 <= posx2 and posx2+37 <= posx1 and posy1<= posy2 and posy2 <= posy1 + 50

        if(posx11>=posx22 and posx11<=posx22+28 and posy11>=posy22 and posy11<=posy22+50 or(posx11+28>=posx22 and posx11+28<=posx22+28 and posy11>=posy22 and posy11<=posy22+50) ):
            print("crash")
            l2=x
            x = can5.create_image(can5.coords(l2)[0],can5.coords(l2)[1],image=carroc)
            can5.delete(l2)
            can5.move(fight,menosfighter-can5.coords(fight)[0],-can5.coords(fight)[1])
            nvl5.after(10,fighterrnvl5)
            contgasonvl5=contgasonvl5-2
            contvelocidad=0
            can5.move(y,0,-can5.coords(y)[1])
        else:
            reloadfighter=0
            nvl5.after(10,fighterrnvl5)

def fighterrnvl55():
    """
    esta funcion es para mover el fighter
    """
    
    global fight2,reloadfighter2,x2,contgasonvl55,contvelocidad22,y
    menosfighter2=random.randint(700,1000)
    if(can5.coords(x2)[0]<can5.coords(fight2)[0]):
        can5.move(fight2,-1.8,2)
    elif(can5.coords(x2)[0]>can5.coords(fight2)[0]):
        can5.move(fight2,1.8,2)
    else:
        can5.move(fight2,0,7)
    if(can5.coords(x2)[1]==can5.coords(fight2)[1]):
        can5.move(fight2,menosfighter2-can5.coords(fight2)[0],-can5.coords(fight2)[1])
        #fight=c1.create_image(500,50,image=fighter)
        
    if(reloadfighter2<950):#250
        
        reloadfighter2 = reloadfighter2 + 1
        posx11f = can5.coords(x2)[0]
        posy11f = can5.coords(x2)[1]
        posx22f= can5.coords(fight2)[0]
        posy22f = can5.coords(fight2)[1]
        
        #posx1 <= posx2 and posx2+37 <= posx1 and posy1<= posy2 and posy2 <= posy1 + 50

        if(posx11f>=posx22f and posx11f<=posx22f+28 and posy11f>=posy22f and posy11f<=posy22f+50 or(posx11f+28>=posx22f and posx11f+28<=posx22f+28 and posy11f>=posy22f and posy11f<=posy22f+50) ):
            print("crash")
            l22=x2
            x2 = can5.create_image(can5.coords(l22)[0],can5.coords(l22)[1],image=carroc)
            can5.delete(l22)
            can5.move(fight2,menosfighter2-can5.coords(fight2)[0],-can5.coords(fight2)[1])
            nvl5.after(10,fighterrnvl55)
            contgasonvl55=contgasonvl55-2
            contvelocidad22=0
            can5.move(y2,0,-can5.coords(y2)[1])
        else:
            reloadfighter2=0
            nvl5.after(10,fighterrnvl55)
        
        
    

####---------------------------------------------------fighter
####----------------------------------------------------mancha
def manchitanvl5():#mover minivan
    """
    mancha de aceite
    """
    
    global nvl5,y,p,c,z,can5,contadormini,x,contgasonvl5,contvelocidad,aceite,contaceite,resbalar
    menosaceite=random.randint(280,500)
    if(contaceite<320):
        can5.move(aceite,0,7)
        contaceite = contaceite + 1
        
    if(contaceite==320):
        #c1.delete(z)
        can5.move(aceite,menosaceite-can5.coords(aceite)[0],-can5.coords(aceite)[1])
        contaceite = 0

    if(resbalar<950):#250
        
        resbalar = resbalar + 1
        posx1x = can5.coords(x)[0]
        posy1x = can5.coords(x)[1]
        posx2a = can5.coords(aceite)[0]
        posy2a = can5.coords(aceite)[1]
        
        #posx1 <= posx2 and posx2+37 <= posx1 and posy1<= posy2 and posy2 <= posy1 + 50

        if(posx1x>=posx2a and posx1x<=posx2a+28 and posy1x>=posy2a and posy1x<=posy2a+50 or(posx1x+28>=posx2a and posx1x+28<=posx2a+28 and posy1x>=posy2a and posy1x<=posy2a+50) ):
            print("crash")
            l1=x
            can5.move(l1,-80,0)
            x = can5.create_image(can5.coords(l1)[0],can5.coords(l1)[1],image=carroc)
            can5.delete(l1)
            can5.move(aceite,menosaceite-can5.coords(aceite)[0],-can5.coords(aceite)[1])
            nvl5.after(10,manchitanvl5)
            contgasonvl5=contgasonvl5-2
            contvelocidad=0
            contaceite=0
            can5.move(y,0,-can5.coords(y)[1])
        else:
            resbalar=0
            nvl5.after(10,manchitanvl5)
            
def manchitanvl55():#mover minivan
    """
    mancha de aceite 2
    """
    
    global nvl5,y,p,can5,x2,contgasonvl55,contvelocidad22,aceite2,contaceite2,resbalar2
    menosaceite2=random.randint(700,970)
    if(contaceite2<320):
        can5.move(aceite2,0,7)
        contaceite2 = contaceite2 + 1
        
    if(contaceite2==320):
        #c1.delete(z)
        can5.move(aceite2,menosaceite2-can5.coords(aceite2)[0],-can5.coords(aceite2)[1])
        contaceite2 = 0

    if(resbalar2<950):#250
        
        resbalar2 = resbalar2 + 1
        posx1xm2 = can5.coords(x2)[0]
        posy1xm2 = can5.coords(x2)[1]
        posx2am2 = can5.coords(aceite2)[0]
        posy2am2 = can5.coords(aceite2)[1]
        
        #posx1 <= posx2 and posx2+37 <= posx1 and posy1<= posy2 and posy2 <= posy1 + 50

        if(posx1xm2>=posx2am2 and posx1xm2<=posx2am2+28 and posy1xm2>=posy2am2 and posy1xm2<=posy2am2+50 or(posx1xm2+28>=posx2am2 and posx1xm2+28<=posx2am2+28 and posy1xm2>=posy2am2 and posy1xm2<=posy2am2+50) ):
            print("crash")
            l13=x2
            can5.move(l13,-80,0)
            x2 = can5.create_image(can5.coords(l13)[0],can5.coords(l13)[1],image=carroc)
            can5.delete(l13)
            can5.move(aceite2,menosaceite2-can5.coords(aceite2)[0],-can5.coords(aceite2)[1])
            nvl5.after(10,manchitanvl55)
            contgasonvl55=contgasonvl55-2
            contvelocidad22=0
            contaceite2=0
            can5.move(y2,0,-can5.coords(y2)[1])
        else:
            resbalar2=0
            nvl5.after(10,manchitanvl55)


####--------------------------------------------------mancha
###-----------------------------------------------------------nyan
def podernvl5 ():
    """
    esta funcion es para mover el gato de la gasolina
    """
    global nvl5,y,p,c,z,can5,contadormini,x,contgasonvl5,contvelocidad,contadorpoder,reloadpoder,nyan
    menospoder=random.randint(280,500)
    if(contadorpoder<500):
        can5.move(nyan,0,6)
        contadorpoder = contadorpoder + 1
        
    if(contadorpoder==500):
        contadorpoder=0
        can5.move(nyan,menospoder-can5.coords(nyan)[0],-can5.coords(nyan)[1])

    if(reloadpoder<950):#250
        
        reloadpoder = reloadpoder + 1
        posx1ny = can5.coords(x)[0]
        posy1ny = can5.coords(x)[1]
        posx2ny = can5.coords(nyan)[0]
        posy2ny = can5.coords(nyan)[1]
        
        #posx1 <= posx2 and posx2+37 <= posx1 and posy1<= posy2 and posy2 <= posy1 + 50

        if(posx1ny>=posx2ny and posx1ny<=posx2ny+28 and posy1ny>=posy2ny and posy1ny<=posy2ny+50 or(posx1ny+28>=posx2ny and posx1ny+28<=posx2ny+28 and posy1ny>=posy2ny and posy1ny<=posy2ny+50) ):
            print("crash")
            can5.move(nyan,menospoder-can5.coords(nyan)[0],can5.coords(nyan)[1]-500)
            nvl5.after(10,podernvl5)
            contgasonvl5=contgasonvl5+2
            contadorpoder=0
        else:
            reloadpoder=0
            nvl5.after(10,podernvl5)
    
def podernvl55 ():
    """
    esta funcion es para mover el gato de la gasolina
    """
    global nvl5,y,p,c,z,can5,contadormini,x,contgasonvl55,contvelocidad,contadorpoder2,reloadpoder2,nyan2
    menospoder2=random.randint(700,980)
    if(contadorpoder2<500):
        can5.move(nyan2,0,6)
        contadorpoder2 = contadorpoder2 + 1
        
    if(contadorpoder2==500):
        contadorpoder2=0
        can5.move(nyan2,menospoder2-can5.coords(nyan2)[0],-can5.coords(nyan2)[1])

    if(reloadpoder2<950):#250
        
        reloadpoder2 = reloadpoder2 + 1
        posx1ny2 = can5.coords(x2)[0]
        posy1ny2 = can5.coords(x2)[1]
        posx2ny2 = can5.coords(nyan2)[0]
        posy2ny2 = can5.coords(nyan2)[1]
        
        

        if(posx1ny2>=posx2ny2 and posx1ny2<=posx2ny2+28 and posy1ny2>=posy2ny2 and posy1ny2<=posy2ny2+50 or(posx1ny2+28>=posx2ny2 and posx1ny2+28<=posx2ny2+28 and posy1ny2>=posy2ny2 and posy1ny2<=posy2ny2+50) ):
            print("crash")
            can5.move(nyan2,menospoder2-can5.coords(nyan2)[0],can5.coords(nyan2)[1]-500)
            nvl5.after(10,podernvl55)
            contgasonvl55=contgasonvl55+2
            contadorpoder2=0
        else:
            reloadpoder2=0
            nvl5.after(10,podernvl55)    

###-------------------------------------------------------------nyan

###--------------------------------------------------------------------------------------------------nivel 5
##botones
b1=tkinter.Button(w0,text="Nivel 1",fg="white",bg="black",font=("Verdana",12),command=nivel1).place(x=600,y=10) #Boton nvl1
b2=tkinter.Button(w0,text="Nivel 2",fg="white",bg="black",font=("Verdana",12),command=nivel2).place(x=600,y=60) #Boton nvl2
b3=tkinter.Button(w0,text="Nivel 3",fg="white",bg="black",font=("Verdana",12),command=nivel3).place(x=600,y=110) #Boton nvl3
b4=tkinter.Button(w0,text="Nivel 4",fg="white",bg="black",font=("Verdana",12),command=nivel4).place(x=600,y=160)  #Boton nvl4
b5=tkinter.Button(w0,text="Nivel 5",fg="white",bg="black",font=("Verdana",12),command=nivel5).place(x=600,y=210) #Boton nvl5
b6=tkinter.Button(w0,text="Nivel 1",fg="white",bg="black",font=("Verdana",12),command=cargar).place(x=100,y=350)#Cargar partida
b7=tkinter.Button(w0,text="Nivel 2",fg="white",bg="black",font=("Verdana",12),command=cargar2).place(x=200,y=350)#Cargar partida
b8=tkinter.Button(w0,text="Nivel 3",fg="white",bg="black",font=("Verdana",12),command=cargar3).place(x=300,y=350)#Cargar partida
b9=tkinter.Button(w0,text="Nivel 4",fg="white",bg="black",font=("Verdana",12),command=cargar4).place(x=400,y=350)#Cargar partida
b10=tkinter.Button(w0,text="Nivel 5",fg="white",bg="black",font=("Verdana",12),command=cargar5).place(x=500,y=350)#Cargar partida

w0.mainloop()
nvl1.mainloop()
nvl2.mainloop()
nvl3.mainloop()
nvl4.mainloop()
nvl5.mainloop()
