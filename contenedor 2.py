import numpy as np
import time


#cuanta la cantidad de elementos en la matriz
def cont(matriz):
    cont=0
    for i in range(len(matriz)):
        cont+=1
    #print(cont)
    return cont
#----------------------------------------------------------
#crear una matriz nula de manera dinamica
def crearmatriz(matriz,peso):
    cont = 0
    for i in range(len(matriz)):
        cont += 1
    tablamochila=np.full((cont+2,peso+2),0)
    #print(tablamochila)
    return (tablamochila)
#-----------------------------------------------------------

#---------------------------------------------------
#asigna los valores correpondiete de la fila que va desde el 0 hasta n
def asginarfila(p,matriz):
    i=0
    aux = p
    x=1
    while (i<=aux):
        if i==0:
            matriz[0][i]=-1
        elif i==1:
            matriz[0][i] = 0
        else:
            matriz[0][i] = i-1
            x=x+1
        i=i+1
    matriz[0][i] = i-1
#-----------------------------------------
#asigna los valores correpondiete de la colunma que va desde el 0 hasta el valor de W
def asginarcolumna(matriz,matriz2):
    i=1
    x=0
    aux = cont(matriz)+1
    while (i<=aux):
        matriz2[i][0] = x
        i=i+1
        x=x+1
#-------------------------------------------------------------
#asigna el peso actual de fila que se esta recorriendo
def asginarpeso(temp,matriz):
    for i in range(len(matriz)):
        if i==temp:
            x=matriz[i][0]
            return x
#-------------------------------------------------------------
#asigna el beneficio actual de fila que se esta recorriendo
def asginarbeneficio(temp,matriz):
    for i in range(len(matriz)):
        if i==temp:
            x=matriz[i][1]
            return x
#-------------------------------------------------------------
#Se rellena la matriz con los datos correspondientes
def mochila (matriz,peso,matriz2):
    x=cont(matriz)
    w=peso
    for i in range(x+2): #cantidad de fielas en la matriz
        if i >=2:
            for l in range(w+2):#la cantidad de columnas en la matriz
                if l >=2:
                    x=matriz2[i][0]
                    wi=asginarpeso(x-1,matriz)#el peso actual de la fila
                    bi=asginarbeneficio(x-1,matriz)#el beneficio actual de la fila
                    p=matriz2[0][l]
                    if wi>p:
                        matriz2[i][l]=matriz2[i-1][l]
                    else:
                        if bi+matriz2[i-1][l-wi]>matriz2[i-1][l]:
                            matriz2[i][l]=bi+matriz2[i-1][l-wi]
                        else:
                            matriz2[i][l]=matriz2[i-1][l]
#-----------------------------------------------------------
#imprime la informacion de la lista listsol que contiene los elementos de la solucion
def imprimilistapeso(matriz):
    for i in range(len(matriz)):
        print(matriz[i])
#------------------------------------------------------------
#Genera la solucion final del problema de la mochila
def solucion(matriz,peso,matriz2,lista):
    i=cont(matriz)+1
    w = peso
    k=w+1
    p=w
    beneficioMAX=matriz2[i][k]
    aux=cont(matriz)

    while aux>0:
        if matriz2[i][k] != matriz2[i-1][k]:
            f=matriz2[i][0]
            wi=matriz[f-1][0]
            lista.insert(0,matriz2[i][0])
            p=p-wi
            k=k-wi
            i=i-1
            aux=aux-1
        else:
            i=i-1
            aux=aux-1
    print("el beneficio maximo es: ",beneficioMAX)
    print("elemtos en la solucion son los siguientes: ")
    #imprimilistapeso(lista)
    print(lista)
#------------------------------------------------------------
def mochila2():
    inicio = time.time()#para calcular el tiempo de ejeucion de la funcion
    tablapeso = [[5, 20], [15, 50], [10, 60], [10, 62], [8, 40]]
    # tablapeso = [[2, 3], [3, 4], [4, 5], [5, 6]]
    # ----------------------------------------------
    # pero maximo de la tabla
    # el w es el peso maximo de la mochila
    w = 30
    # w = 5
    listsol = []
    # ------------------------------------------------
    # esta lista guarda el valor de la fila que entra en la solucion
    tablamochila = crearmatriz(tablapeso,w)
    #print(tablamochila)
    asginarfila(w,tablamochila)
    asginarcolumna(tablapeso,tablamochila)
    print("matriz")
    print(tablamochila)
    mochila(tablapeso,w,tablamochila)
    print("-----imprimiendo nueva matriz-----")
    print(tablamochila)
    print("------imprimiendo la solucion-----")
    solucion(tablapeso,w,tablamochila,listsol)
    fin = time.time()#para calcular el tiempo de ejeucion de la funcion
    print("tiempo de ejecucion: ",fin - inicio)
#------------------------------------------------------------
if __name__ == '__main__':
    mochila2()


