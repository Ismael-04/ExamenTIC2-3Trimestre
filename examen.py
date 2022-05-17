


# ----  Ejercicios ---- 

#Ejercicio 1
import random


def Menu():
    print("1- Guardar asignatura ")
    print("2- Borrar asignatura")
    print("3- Ver Nota media")
    print("4- Ver todas las asignaturas ")
    print("5- Salir ")
    opc=0
    while opc<1 or opc>5:
        try:
            opc=(int)(input("Introduzca una opcion de menu."))
        except:
            print("Te has esquivocado")
    return opc

#Fin ejercicio 1



#Ejercicio 3

def listasignatu(lista):
    asignatura=input("Introduzca una asignatura")
    lista.append(asignatura)
    print(lista)
    return lista
#Ejercicio 5
def numal():
    i=5
    listnum=[]
    while i!=0:
       listnum.append(random.randint(0,10)) 
       i=i-1
    return listnum
  
#Ejercicio 6

def opc3():
    suma=0
    notas = numal()
    media=0
    cont=par
    for cont in notas:
        suma=suma+cont
    media=(suma/len(notas))
    return media



# ---- Programa principal -----

#Ejercicio 2
opc=Menu()
par=0
lista=[]
while opc!=5:
    if opc==1:
        print("1- Guardar asignatura ")
        listasignatu(lista)
       
    if opc==2:
        print("2- Borrar asignatura")
        
    if opc==3:
        print("3- Ver Nota media")
        numal()
        opc3()

        
    if opc==4:
        print("4- Ver todas las asignaturas")
       
    opc=Menu()
    if opc==5:
        print("Ha finalizado")

