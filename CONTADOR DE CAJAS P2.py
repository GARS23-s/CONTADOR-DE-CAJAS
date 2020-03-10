from tkinter import *
global P,M,G,en
P=0
M=0
G=0
en=1
def inicio():
    global P,M,G,en
    
    B1=Button(ventana,text="CAJAS PEQUEÑAS",command=A,state="normal",bg="yellow").grid(column=1,row=1)
    B2=Button(ventana,text="CAJAS MEDIANAS",command=B,state="normal",bg="orange").grid(column=2,row=1)
    B3=Button(ventana,text="CAJAS GRANDES",command=C,state="normal",bg="red").grid(column=3,row=1)
    B4=Button(ventana,text="TOTAL DE CAJAS",command=D,state="normal",bg="green").grid(column=4,row=1)
  

def A ():
    global P
    P=P+1
def B ():
    global M
    M=M+1
def C ():
    global G
    G=G+1
def D ():
    global P,M,G
    l=Label(ventana,text="El total de CAJAS PEQUEÑAS es:"+str(P)).grid(column=0,row=2) 
    l=Label(ventana,text="El total de CAJAS MEDIANAS es:"+str(M)).grid(column=0,row=3)
    l=Label(ventana,text="El total de CAJAS GRANDES es:"+str(G)).grid(column=0,row=4)
    l=Label(ventana,text="EL TOTAL DE CAJAS CONTADAS ES:"+str(P+M+G)).grid(column=0,row=5)

            
    if(en==1):
            inicio()

        
ventana=Tk()
inicio()
ventana.mainloop()



