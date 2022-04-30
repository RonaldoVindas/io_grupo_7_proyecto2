def  leer (nombre_archivo):
    with open(nombre_archivo) as archivo:
        contenido = archivo.readlines()

    lista_contenido = convierteListaMatriz (contenido)
    print("lista_contenido: ",lista_contenido)

    

#---------------------------------------------------------------------------------------------      Funciones auxiliares para la lectura del archivo    ---------------------------------------------------------------------------------------------#
def  convierteListaMatriz (lista): 
    res = [] 
    for datos in lista:
        sublista = datos.split(', ')
        res.append(sublista) 
    return(res) 
