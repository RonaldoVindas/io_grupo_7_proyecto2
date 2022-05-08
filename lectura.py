# Funcion encargade de abre el archivo txt y extraer los datos de este, los devuelve en una lista de string
def  leer (nombre_archivo):
    with open(nombre_archivo) as archivo:
        contenido = archivo.readlines()

    lista_contenido = convierteListaMatriz (contenido)
    print("lista_contenido: ",lista_contenido)
    return lista_contenido
    
    
#---------------------------------------------------------------------------------------------      Funciones auxiliares para la lectura del archivo    ---------------------------------------------------------------------------------------------#
# funcion que convierte en matriz la lista de strings extraida del txt
def  convierteListaMatriz (lista): 
    res = [] 
    for datos in lista:
        sublista = datos.split(', ')
        res.append(sublista) 
    return res


# Convierte todos los datos de una matriz de String en una matriz de enteros 
def convierteListaStringInt (matriz):
    I = len(matriz)
    J = len(matriz[0])
    res = []
    for lista in matriz:
        temp = []
        for j in lista:
            temp.append(int(j))
        res += [temp]
    return res
