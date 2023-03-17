from curses.ascii import EM
import math
g=9.81

def Vb(h):
    return(math.sqrt(2*g*h))


def Vc(eMecanica,m):
    return(math.sqrt((2*eMecanica)/m))


def Hd(eMecanica,m):
    return(eMecanica/(m*g))


def Emec(m,h):
    return(m*g*h)#4.905

l=2
m=0.1
h=5
fk=0.3
w=(fk*m*g)*2*-1       #-0.5886J
b=100
eMecanica=Emec(m,h)
i=1
print("Va=0")
print("-----------------------\n")

while h>0:
    #ida
    print("       ",i,"\n")
    i=i+1
    #repetir el los pasos hasta que se pare la masa
    print("Emec antes de pasar por el fondo= ",eMecanica,"joules")
    b=Vb(h)
    print("Vb= ",b,"m/s")
    c=Vc(eMecanica,m)
    print("Vc= ",c,"m/s")
    eMecanica=eMecanica+w
    print("Emec despues de pasar el fondo= ",eMecanica,"joules")
    d=Hd(eMecanica,m)
    h=d
    print("Hd= ",d,"m")


    if(eMecanica>0):
        print("-----------------------") 
        print("       ",i,"\n")
        #vuelta
        print("Emec antes de pasar por el fondo= ",eMecanica,"joules")
        c=Vc(eMecanica,m)
        print("Vc= ",c,"m/s")
        b=Vb(h)
        print("Vb= ",b,"m/s")
        eMecanica=eMecanica+w
        print("Emec despues de pasar el fondo= ",eMecanica,"joules")
        d=Hd(eMecanica,m)
        h=d
        print("Ha= ",d,"m")
        print("                                                   vuelta",i/2)
        i=i+1
        print("-----------------------")
    else:
        print("______________________________________________________\n")
        print("valor de c:",(0.5*(math.pow(c,2))))
        print("valor del denominador:",(fk*g))
        print("la masa se quedo a= ",(0.5*(math.pow(c,2))/(fk*g)),"m del fondo")
        print("______________________________________________________-")




    