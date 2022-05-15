import sys
from time import time
import numpy as np
import time
metodo=0
#funcion 1:main
#verifica que se haya digitado el nombre del archivo y metodo de resolucion
def main():
    global  metodo
    if len(sys.argv)<3 or len(sys.argv)>3:    
        print("Debió introducir el nombre del archibo y metodo de resolucion")
        sys.exit()
    else:
        metodo=int(sys.argv[1])
        leer(sys.argv[2])

#función 2: leer
#abre el archivo txt y regresa los datos en de los pesos y beneficios
#en forma de matriz
def  leer (nombre_archivo):
    with open(nombre_archivo) as archivo:
        contenido = archivo.readlines()
    lista_contenido = convierteListaMatriz (contenido)
    matrizProblema=convertValMatriz(lista_contenido[1:])
    pesoMax=int(lista_contenido[0][0])
    menu(matrizProblema,pesoMax)

# Funcion 3:convierteListaMatriz
# funcion auxiliar de la función 2 que convierte en matris la cadena
# la lista de strings extraida del txt
def  convierteListaMatriz (lista): 
    res = [] 
    for datos in lista:
        sub=datos.rstrip()#yo lo agregué del cod original
        sublista = sub.split(',')
        res.append(sublista) 
    return res 
#Funcion 4:convertValMatriz
#convierte en enteros los valores de la matriz y le agrega un indice
#al inicio de cada fila
def convertValMatriz(matrix):
    count = 1
    newMat= []
    for i in  matrix:
        row=[]
        row.append(count)
        for j in i:
            row.append(int(j))
        count+=1
        newMat.append(row)
    return newMat
#Función 5:menu
#de acuerdo al metodo introducido llama a las funciones necesarias
#para resolver el problema de la mochila de esa manera
def menu(matriz,peso):
    global metodo
    #print(metodo)
    if metodo ==1:
        inicio = time.time()
        mochilaFuerzaBruta(matriz,peso)
        fin = time.time()#para calcular el tiempo de ejeucion de la funcion
        print("tiempo de ejecucion: ",fin - inicio)
    else:
        a=quitarInx(matriz)
        mochila2(a,peso) 
       
#Funcion6:hacerCombinaciones
#ingresa una matriz y retorna otra con todas las posibles combinaciones
#que se pueden hacer con los elementos de la matriz parametro
def hacerCombinaciones(matriz):
    resp=[[]]
    for i in matriz:
        combinacion= [comb+[i] for comb in resp]
        resp.extend(combinacion)
    return resp
#funcion7: mochilaFuerzaBruta
#funcion encargada de resolver el problema de la mochila por la fuerza
#recorre la matriz que posee todas las combinaciones y retorna la combinación con mayor
#beneficio que se adapte al peso maximo de la mochila
def mochilaFuerzaBruta(matriz,pesoMax):
    mochila=[]
    pesoOptimo=0
    beneficioOptimo=0
    for i in hacerCombinaciones(matriz):
        pesoActual=getTotalPeso_Beneficio(i,1)
        beneficioActual=getTotalPeso_Beneficio(i,2)
        if beneficioActual>beneficioOptimo and pesoActual<=pesoMax:
            beneficioOptimo=beneficioActual
            pesoOptimo=pesoActual
            mochila=i
    mostrarResultados(mochila,pesoOptimo,beneficioOptimo,pesoMax)
    return mochila
#funcion 8: getTotalPeso_Beneficio
#funcion auxiliar de mochilaFuerzaBruta, hace la sumatora de los beneficios o peso de cada combinacion
def getTotalPeso_Beneficio(combinacion,pos):
    resp=[]
    for i in combinacion:
        resp.append(i[pos])
    total=sum(resp)
    return total
#funcion 9: mostrarResultados
#muestra en consola los resultados del problema de la mochila
def mostrarResultados(mochila,pesoOptimo,beneficioOptimo,pesoMax):
    print("Beneficio máximo: ",beneficioOptimo)
    a="Incluidos: "
    for i in mochila:
        a+=(str(i[0]))
        a+=(",")
    print(a)

def quitarInx(matriz):
    resp=[]
    for i in matriz:
        resp.append(i[1:])
   # print(resp)
    return(resp)
#######################################
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
def mochila2(matrizInput,pesoInput):
    inicio = time.time()#para calcular el tiempo de ejeucion de la funcion
    tablapeso = matrizInput
    # ----------------------------------------------
    w = pesoInput
    listsol = []
    # ------------------------------------------------
    # esta lista guarda el valor de la fila que entra en la solucion
    tablamochila = crearmatriz(tablapeso,w)
    asginarfila(w,tablamochila)
    asginarcolumna(tablapeso,tablamochila)
    mochila(tablapeso,w,tablamochila)
    print("------imprimiendo la solucion-----")
    solucion(tablapeso,w,tablamochila,listsol)
    fin = time.time()#para calcular el tiempo de ejeucion de la funcion
    print("tiempo de ejecucion: ",fin - inicio)
#------------------------------------------------------------
  
main()
