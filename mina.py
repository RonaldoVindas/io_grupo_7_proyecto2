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
        start_time = time()
        minaFuerzaBruta(Matriz,[])
        elapsed_time = time() - start_time
        print("Tiempo de ejecución:" , elapsed_time, "segundos")
    else:
        print("LLAMA A MINA DINAMICA")

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
    for camino in caminos:
        mayor = listaMayor(mayor, camino, Matriz,J)

    i = 0
    rest = 0
    while (i < J):
        rest += Matriz[mayor[i][0]] [mayor[i][1]]
        i += 1
    print ("Output : " + str(rest))
    #lectura.leer("mina1.txt")
    return mayor


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
        return lista2
    else:
        return lista1

      
#----------------------------------------------------------      Funciones de Programacion Dinamica      ----------------------------------------------------------# 
