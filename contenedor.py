import sys
from time import time
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
    if metodo ==1:
        start_time = time()
        mochilaFuerzaBruta(matriz,peso)
        elapsed_time = time() - start_time
        print("Tiempo de ejecución:" , elapsed_time, "segundos")
    else:
        print("aqui va parte dinamica de mochila")
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

main()

