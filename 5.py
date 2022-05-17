import random
def numal(listnum):
    
    i=(int)(input("Introduzca numero de parametros"))
    while i!=0:
       listnum.append(random.randint(0,10)) 
       i=i-1
    print(listnum)
listnum=[]
print(numal(listnum))