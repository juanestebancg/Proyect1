import tkinter

w0=tkinter.Tk()# se crea la ventana

w0.geometry("700x500")#tamaño de la ventana

fondo=tkinter.PhotoImage(file="vector.png")#fondo de la pantalla

lblfondo=tkinter.Label(w0,image=fondo).place(x=0)#Label del fondo

#campo de entrada label jugador 1
lblfondo=tkinter.Label(w0,text="Jugador 1: ",font=("Arial",14)).place(x=10,y=10)

#jugador 1 campo

j1=tkinter.StringVar()
j1.set("")
j1txt=tkinter.Entry(w0,textvariable=j1).place(x=120,y=10)

#campo de entrada label jugador 2
lblfondo=tkinter.Label(w0,text="Jugador 2: ",font=("Arial",14)).place(x=10,y=40)

#jugador 1 campo

j2=tkinter.StringVar()
j2.set("")
j2txt=tkinter.Entry(w0,textvariable=j2).place(x=120,y=40)

global c1,nvl1,mapa,lblmapa

def nivel1(): # Abrir la ventana del nivel 1, fusionar funcion de guardado a precionar nivel 1
    """
    Esta funcion es para abrir una nueva ventana, que abre el mapa del nivel 1
    """
    nvl1 = tkinter.Tk()#crear la ventana del nivel 1
    nvl1.geometry("800x850")#dimensiones de la ventana
    c1=tkinter.Canvas(nvl1, width=200, height=100).pack
    mapa=tkinter.PhotoImage(file="1nivel.png")#imagen del mapa
    lblmapa=tkinter.Label(nvl1,image=mapa)
#######
def gasolina():
    """
    con esta funcion se crea el label de la gasolina
    """
    global gaso,nvl1,lbl3,cont1
    
    
    if(cont1>=0):
        gaso.set(str(cont1))
        cont1=cont1-1
    c1.after(1000,gasolina)
    if(cont1<0):
        nvl1.destroy()
    

#####mover player    
def key(event): #teclas para mover el jugador
    """
    """
    global x,i,j,y
    tecla = repr(event.char)
    #print(tecla)
    if(tecla == "'d'"):
        if(i < 190):
            c1.delete(x)
            i = i + 10
            x = c1.create_image(400+i,750+j,image=carro)
            
        else:
            c1.delete(x)
            x = c1.create_image(400+i,750+j,image=carroc2)            
    if(tecla == "'a'"):
        if(i > -195):
            c1.delete(x)
            i = i - 10
            x = c1.create_image(400+i,750+j,image=carro)
        else:
            c1.delete(x)
            x = c1.create_image(400+i,750+j,image=carroc2)

####mover player
def mini():#mover minivan
    """
    """
    global nvl1,y,p,c,z,c1
    
    if(c<350):
        c1.move(z,0,2)
        c = c + 1
        nvl1.after(10,mini)
        
        
    if(c==350):
        c1.delete(z)
        c = 0
        z=c1.create_image(500,-50,image=minivan)
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
        nvl1.after(1,fondito)
def fondito2():
    """
    """
    global c1,nvl1
    c222=0
    c322=0
    if(c222<5):
        c1.move(y2,0,0.8)
        c22=c222+1
        c32=c322+1
        nvl1.after(1,fondito2)

###mover fondo            

def nivel2(): # Abrir la ventana del nivel 2, fusionar funcion de guardado a precionar nivel 2
    """
    Esta funcion es para abrir una nueva ventana, que abre el mapa del nivel 2
    """
    nvl2 = tkinter.Tk()

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


b1=tkinter.Button(w0,text="Nivel 1",font=("Arial",14),command=nivel1).place(x=400,y=10) #Boton nvl1
b2=tkinter.Button(w0,text="Nivel 2",font=("Arial",14),command=nivel2).place(x=400,y=60) #Boton nvl2
b3=tkinter.Button(w0,text="Nivel 3",font=("Arial",14),command=nivel3).place(x=400,y=110) #Boton nvl3
b4=tkinter.Button(w0,text="Nivel 4",font=("Arial",14),command=nivel4).place(x=400,y=160)  #Boton nvl4
b5=tkinter.Button(w0,text="Nivel 5",font=("Arial",14),command=nivel5).place(x=400,y=210) #Boton nvl5



w0.mainloop()
nvl1.mainloop()
nvl2.mainloop()
nvl3.mainloop()
nvl4.mainloop()
nvl5.mainloop()
