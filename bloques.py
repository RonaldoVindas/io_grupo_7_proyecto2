from itertools import permutations
import sys
from time import time
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
    matrizProblema=convertValMatriz(lista_contenido)
    menu(matrizProblema)

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
#convierte en enteros los valores de la matriz 
def convertValMatriz(matrix):
    newMat= []
    for i in  matrix:
        row=[]
        for j in i:
            row.append(int(j))
        newMat.append(row)
    return newMat

#Función 5:menu
#de acuerdo al metodo introducido llama a las funciones necesarias
#para resolver el problema de la mochila de esa manera
def menu(matriz):
    global metodo
    if metodo ==1:
        inicio = time.time()
        matBloquesRotados=invertirBloques(matriz)
        MatComb=hacerTodasCombinaciones(matBloquesRotados)
        bloquesFuerzaBruta(MatComb)
        fin = time.time()#para calcular el tiempo de ejeucion de la funcion
        print("tiempo de ejecucion: ",fin - inicio)
    else:
        inicio = time.time()
        seleciondemayores(matriz)
        fin = time.time()#para calcular el tiempo de ejeucion de la funcion
        print("tiempo de ejecucion: ",fin - inicio)
       
#Función 6:invertirBloques
#encuentra las rotaciones validas de cada figura y las guarda en una matriz
def invertirBloques(matriz):
    res=[]
    for i in matriz:
        temp = permutations(i)
        for j in list(temp):
            if j[0]<=j[1]:
                res.append(list(j))             
    return res

#Función 7:hacerTodasCombinaciones
#encuentra todas las combinaciones que se pueden hacer con los bloques
def hacerTodasCombinaciones(matriz):
    resp=[[]]
    for i in matriz:
        combinacion= [comb+[i] for comb in resp]
        resp.extend(combinacion)
    return resp

#Función 8:combo
#conserva solo las combinaciones que cumplen que el bloque de encima 
# sea estrictamente menor que la de abajo
def combo(matriz):
    combinaciones = []
    for i in matriz:
        if len(i)==1:
            combinaciones.append(i)
        elif len(i)>1:
            #combinaciones.append(ordenarbloques(i))
            temporal=ordenarbloques(i)
            if revisarLista(temporal)==True:
                combinaciones.append(temporal)
    return combinaciones

#Función 9:revisarLista
#función auxiliar de combo,revisa que el bloque de encima 
# sea estrictamente menor que la de abajo para cada bloque de la combinación          
def revisarLista(mat):
    n = len(mat)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if (mat[j][0]<=mat[j+1][0]) or (mat[j][1]<=mat[j + 1][1]):
                return False
    return True

#Función 10:revisarLista
#función auxiliar de combo,ordena las combinaciones de acuerdo al perimetro de su base( frente y profundidad)
def ordenarbloques(mat):
    n = len(mat)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if (mat[j][0]+mat[j][1]) < (mat[j + 1][0]+mat[j + 1][1]) :
                mat[j], mat[j + 1] =mat[j + 1], mat[j]
    return mat

#funcion11: bloquesFuerzaBruta
#funcion encargada de resolver el problema de los bloques por la fuerza
#recorre la matriz que posee todas las combinaciones  validas(F <= P  y bloque superior debe ser menor al inferior)
# y retorna la combinación con mayor altura  
def bloquesFuerzaBruta(matriz):
    bloques=[]
    alturaMax=0
    for i in combo(matriz):
        alturaActual=getTotalAltura(i,2)
        if alturaActual>alturaMax:
            alturaMax=alturaActual
            bloques=i
    mostrarResultados(bloques,alturaMax)
    return bloques

#funcion 12: getTotalAltura
#funcion auxiliar de bloquesFuerzaBruta, hace la sumatora de las alturas de cada combinacion 
def getTotalAltura(combinacion,pos):
    resp=[]
    for i in combinacion:
        resp.append(i[pos])
    total=sum(resp)
    return total

#funcion 13: mostrarResultados
#muestra en consola los resultados del problema de los bloques
def mostrarResultados(bloques,altura):
    print("Altura máxima: ",altura)
    a="bloques: "
    for i in bloques:
        a+=(str(i))
        a+=(",")
    print(a)

#-------------------------------------
# Función 14:contador
# retorna la cantidad de elementos de una matriz
def contador(lista):
    cont=0
    for i in range(len(lista)):
        cont=cont+1
    return cont

# Función 15:alturamax
# retorna el total de altura de la mejor combinacion de bloques
def alturamax(matriz):
    altura=0
    for i in range(len(matriz)):
        altura=altura+matriz[i][2]
    return altura

# Función 16:mayor
# retorna el bloque con dimensiones mayores en la base(frente y profundidad)
def mayor(lista):
    listaaux=invertirBloques(lista)
    frenteaux=0
    profundidadaux=0
    alturaaux=0
    listsol=[]
    for i in range(len(listaaux)):
        if frenteaux<=listaaux[i][0] and profundidadaux<=listaaux[i][1]:
            frenteaux=listaaux[i][0]
            profundidadaux=listaaux[i][1]
            alturaaux=listaaux[i][2]
    listsol.append([frenteaux,profundidadaux,alturaaux])
    return listsol


#funcion18: seleciondemayores
#funcion encargada de resolver el problema de los bloques de forma dinamica
#recorre la matriz  crea y verifica las combinaciones  validas(F <= P  y bloque superior debe ser menor al inferior)
# y retorna la combinación con mayor altura  
def seleciondemayores(mat):
    listaprincipal=invertirBloques(mat)
    cont=contador(listaprincipal)
    listasolucion=[]
    contaux=0
    while cont>0:
        frenteaux = 0
        profundidadaux = 0
        alturaaux = 0
        insertar = False
        for i in range(len(listaprincipal)):
            if frenteaux<=listaprincipal[i][0] and profundidadaux<=listaprincipal[i][1]:
                frenteaux=listaprincipal[i][0]
                profundidadaux=listaprincipal[i][1]
                alturaaux=listaprincipal[i][2]
                contaux=i
        x = contador(listasolucion)
        if listasolucion==[]:
            listasolucion.append([frenteaux,profundidadaux,alturaaux])
            insertar = True
        elif listasolucion!=[] and listasolucion[x-1][0]>frenteaux and listasolucion[x-1][1]>profundidadaux:
            listasolucion.append([frenteaux,profundidadaux,alturaaux])
            insertar=True
        elif insertar==False:
            y=contador(listasolucion)
            if listasolucion[y-2][0]>frenteaux and listasolucion[y-2][1]>profundidadaux and listasolucion[y-1][2]<alturaaux and listasolucion[y-1][0]<=frenteaux:              
                del listasolucion[y-1]
                listasolucion.insert(x, [frenteaux, profundidadaux, alturaaux])
        del listaprincipal[contaux]
        cont=cont-1
    alturamaxima=alturamax(listasolucion)
    print(listasolucion," ", "altura: ",alturamaxima)

main()