import lectura
import sys
from time import time
import time 

algoritmo=0
#----------------------------------------------------------     Funcion principal    ----------------------------------------------------------#
#verifica que se haya digitado el nombre del archivo y metodo de resolucion
def main():
    global  algoritmo
    if len(sys.argv)<3 or len(sys.argv)>3:
        print("Debió introducir el nombre del archibo y algoritmo de resolucion")
        sys.exit()
    else:
        algoritmo=int(sys.argv[1])
        matriz = lectura.leer(sys.argv[2])
    
    if algoritmo ==1:
        Matriz = lectura.convierteListaStringInt (matriz)
        #print(Matriz)
        inicio = time.time()
        minaFuerzaBruta(Matriz,[])
        fin = time.time()#para calcular el tiempo de ejeucion de la funcion
        print("tiempo de ejecucion: ",fin - inicio)
    else:
        Matriz = lectura.convierteListaStringInt (matriz)
        #inicio = time.time()
        minaDinamica(Matriz)
        #fin = time.time()#para calcular el tiempo de ejeucion de la funcion
        #print("tiempo de ejecucion: ",fin - inicio)
        
#----------------------------------------------------------        Funciones de Fuerza Bruta        ----------------------------------------------------------# 
# funcion encargada de resolver el problema de la Mina de Oro por medio de la fuerza bruta.
# recorre la matriz que posee todos los valores de la mina en toneladas. 
# retorna el camino con mayor beneficio y el Output de este.
def minaFuerzaBruta(Matriz,Res):
    I = len(Matriz)
    J = len(Matriz[0])
    i = 0
    caminos = []
    while(i < I):
        caminos += obtenercaminos_aux([[i,0]], I,J,Matriz,[])
        i += 1
    mayor = caminos[0]
    caminosMayores = [mayor]
    for camino in caminos[1:]:
        listMayor = listaMayor(mayor, camino, Matriz,J)
        if (listMayor == 0):
            caminosMayores = caminosMayores + [camino]
        elif (listMayor == 2):
            caminosMayores =  [camino]
            mayor = camino
    i = 0
    rest = 0
    while (i < J):
        rest += Matriz[mayor[i][0]] [mayor[i][1]]
        i += 1
    print ("Output : " + str(rest))
    if(len(caminosMayores) > 1):
        print("Caminos:")
    else:
        print("Camino:")
    for camino in caminosMayores:
        print(camino)
    return caminosMayores

# Funcion encargada de encontrar todos los camninos posibles, desde una posicion en especifico, 
# se detiene cuando llega a la ultima posicion, se hizo uso de cola para su elaboracion. 
def obtenercaminos_aux(posI, I,J,matriz,Res):
    UltPosi = posI[-1]
    i = UltPosi[0]
    j = UltPosi[1] + 1
    if (j < J):
        temp = []
        if(i-1 >= 0):
            temp += obtenercaminos_aux(posI+[ [i-1, j] ], I,J,matriz,Res)
        if(i+1 < I):
            temp += obtenercaminos_aux(posI+[ [i+1, j] ], I,J,matriz,Res)
        temp += obtenercaminos_aux(posI+[ [i, j] ], I,J,matriz,Res)
        return Res + temp
    else:
        return [posI]
# Funcion encargada de recibir dos caminos distintos, extrae los valores de este y 
# compara cual de estos dos caminos posee mayor beneficio
def listaMayor (lista1,lista2, matriz, largo):
    rest1 = 0
    rest2 = 0
    i = 0
    while (i < largo):
        rest1 += matriz[lista1[i][0]] [lista1[i][1]]
        rest2 += matriz[lista2[i][0]] [lista2[i][1]]
        i += 1
    if (rest1 < rest2):
        return 2
    elif (rest1 == rest2):
        return 0
    else:
        return 1
#############################Dinamico#######################################

#funcion:mayor, input(una lista de 3 elementos)
#retorna el elmento de mayor valor en la lista
def mayor(lista):
    res=lista[0]
    for i in lista:
        if i>res :
            res=i
    return res 
#funcion: minaDinamica, input:una matriz
#funcion encargada de resolver el problema de los minas de forma dinamica
#recorre la matriz  verifica y encuentrael camino optimo(de mayor valor) mediante etapas
# y retorna (imprime en consola) la cantidad de oro mayor y el camino para obtenerlo 
def minaDinamica(matriz):
    inicio = time.time() # para calcular el tiempo de ejeucion de la funcion
    cantFilas=len(matriz)
    cantColumnas=len(matriz[0])

    derecha = 0
    diagonalArriba = 0
    diagonalAbajo = 0
    resultado = 0

    listaaux =[]
    aux=0
    listasolucion=[]
    mina2=matriz

    # crear una matriz para los valores
    matrizVal = []
    for i in range(cantFilas):
        sub=[]
        for j in range(cantColumnas):
            sub.append(0)
        matrizVal.append(sub)
 #encargada de resolver las etapas
    for col in range(cantColumnas - 1, -1, -1):
        for fila in range(cantFilas):
            #  diagonal derecha arriba
            if (fila == 0 or col == cantColumnas - 1):
                diagonalArriba = 0
            else:
                diagonalArriba = matrizVal[fila - 1][col + 1]
            # Derecha
            if (col == cantColumnas - 1):
                derecha = 0
            else:
                derecha = matrizVal[fila][col + 1]
            # diagonal derecha abajo
            if (fila == cantFilas - 1 or col == cantColumnas - 1):
                diagonalAbajo = 0
            else:
                diagonalAbajo = matrizVal[fila + 1][col + 1]
            matrizVal[fila][col] = matriz[fila][col] + mayor([derecha,diagonalArriba,diagonalAbajo])
            x=matriz[fila][col] + mayor([derecha, diagonalArriba, diagonalAbajo])
            listaaux.append([matriz[fila][col], mayor([derecha, diagonalArriba, diagonalAbajo])])
            aux=aux+1
            if aux==cantFilas:
                listasolucion.append(listaaux)
                listaaux=[]
                aux=0

    resultado = matrizVal[0][0]
    for n in range(cantFilas):
        resultado = max(resultado, matrizVal[n][0])
    listaposicion=camino(resultado, cantFilas, listasolucion)
    posicion(listaposicion,cantFilas,mina2)
    fin = time.time()  # para calcular el tiempo de ejeucion de la funcion
    print("Total de oro: ",resultado)
    print("tiempo de ejecucion: ", fin - inicio)
#--------------------------------------------------------------------------------------------
#función:contador, input: una lista
#retorna la cantidad de elementos que posee la lista ingresada
def contador(lista):
    cont=0
    for i in range(len(lista)):
        cont=cont+1
    return cont
#---------------------------------------------------------------------------------------------
#esta funcion de devuelve los nodos por donde se obtuvo la mayor cantidad de oro
def camino(valormayor,cantFilas,lista):
    cont=contador(lista)-1
    listasol=[]
    aux=1
    aux2=0
    while cont>=0:
        aux3 = cantFilas
        contaux=cont
        while aux3>=0:
            if lista[cont][contaux][0]+lista[cont][contaux][1]==valormayor and aux==1:
                listasol.append(lista[cont][contaux])
                aux=aux+1
                aux2=lista[cont][contaux][1]
                break
            elif lista[cont][contaux][0]+lista[cont][contaux][1]==aux2 and aux>=2:
                listasol.append(lista[cont][contaux])
                aux = aux + 1
                aux2 = lista[cont][contaux][1]
                break
            aux3=aux3-1
            contaux=contaux-1
        cont=cont-1
    return listasol
#---------------------------------------------------------------------------------------------
#esta funcion de devuelve la posicion en la matriz de los nodos por donde se obtuvo la mayor cantidad de oro
def posicion(lista,cantFilas,matriz):
    aux=cantFilas-1
    cont=contador(lista)-1
    listaposicion=[]
    while aux>=0:
        aux2=cantFilas-1
        x=lista[cont][0]
        while aux2>=0:
            if matriz[aux2][aux]==x:
                listaposicion.insert(0,[aux2,aux])
                break
            aux2=aux2-1
        cont=cont-1
        aux=aux-1
    print(listaposicion)
#if __name__ == '__main__':

    #minaDinamica([[1, 3, 1, 5], [2, 2, 4, 1,], [5, 0, 2, 3],[0, 6, 1, 2]])
    #minaDinamica([[1,3,3],[2,1,4],[0,6,4]])

main()      
#----------------------------------------------------------      Funciones de Programacion Dinamica      ----------------------------------------------------------# 
