import time


#retorna el elmento de mayor valor en la lista
def mayor(lista):
    res=lista[0]
    for i in lista:
        if i>res :
            res=i
    return res 

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
if __name__ == '__main__':

    #minaDinamica([[1, 3, 1, 5], [2, 2, 4, 1,], [5, 0, 2, 3],[0, 6, 1, 2]])
    minaDinamica([[1,3,3],[2,1,4],[0,6,4]])
