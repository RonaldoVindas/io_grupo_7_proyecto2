#Instituto Tecnológico de Costa Rica
#Ronaldo Vindas B.
#2018238697


#problema 2 - Minas Dinamico

Mina = [[1,3,3], [2,1,3], [0, 6,4]]
#Mina = [[1, 3, 1, 5], [2, 2, 4, 1], [5, 0, 2, 3], [0, 6, 1, 2]  ]
 


def  leer (nombre_archivo):
    with open(nombre_archivo) as archivo:
        contenido = archivo.readlines()

    lista_contenido = convierteListaMatriz (contenido)
    #print("lista_contenido: ",lista_contenido)
    return lista_contenido
    
#---------------------------------------------------------------------------------------------      Funciones auxiliares para la lectura del archivo    ---------------------------------------------------------------------------------------------#
def  convierteListaMatriz (lista): 
    res = [] 
    for datos in lista:
        sublista = datos.split(', ')
        res.append(sublista) 
    return res





#---------------------------------------------------------------------------------------------      Funciones auxiliares para la lectura del archivo    ---------------------------------------------------------------------------------------------#

quanRows = len(Mina)
quanColumns = len(Mina[0])
totalGold = 0
optimalValue = 0

cellRoute= []

def getLastColumnOptimalValue(Mina, quanColumns, totalGold):
#Se consigue la columna actual y se saca su valor máximo
    
    column = []
    if quanColumns == 0:
        for i in range(len(Mina)):
            column.append(Mina[i][quanColumns-1])
        optimalValue = max(column)
        totalGold += optimalValue
        for i in range(len(Mina)):
            for j in range(len(Mina[i])):
                if Mina[i][j] == optimalValue:
                    cellRoute_str = "(" + str(i) + ", " + str(j) + ")"
                    cellRoute.append(cellRoute_str)
                    cellRoute.reverse()
        

        return totalGold
    
    for i in range(len(Mina)):
        column.append(Mina[i][quanColumns-1])
    optimalValue = max(column)
    totalGold += optimalValue
    for i in range(len(Mina)):
        for j in range(len(Mina[i])):
            if Mina[i][j] == optimalValue:
                cellRoute_str = "(" + str(i) + ", " + str(j) + ")"
                cellRoute.append(cellRoute_str)
    quanColumns -= 1
    print(optimalValue)
    print(cellRoute)
    print("Output: " + str(totalGold))
    
    getLastColumnOptimalValue(Mina, quanColumns, totalGold)
    
    

            
 
    

    
#    for j in range(len(column)):
#        if Mina[i][j-1] == optimalValue:
#            route_str = "( " + str(i) + ", " + str(j) + " )"
#            cellRoute.append(route_str)
        
        


getLastColumnOptimalValue(Mina , quanColumns, totalGold)












    
