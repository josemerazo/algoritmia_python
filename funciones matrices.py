



def ingresa_matriz(rows=0, columns=0):
    matriz = []
    for i in range(rows):
        fila = []
        for j in range(columns):
            valor = int(input(f"Ingrese el valor de la posición[{i}][{j}]: "))
            fila.append(valor)
        matriz.append(fila)
    return matriz
        

def imprime_matriz(matriz1):
    for d1 in range(len(matriz1)):
        for d2 in range(len(matriz1[d1])):
            print(matriz1[d1][d2],end=' ')
        print('')
        

def transponer_matrices(matriz):
    matriz_transpuesta = []
    rows = len(matriz)
    columns = len(matriz[0])
    
    for j in range(columns):
        fila_transpuesta = []
        for i in range(rows):
            fila_transpuesta.append(matriz[i][j])
        matriz_transpuesta.append(fila_transpuesta)
    return matriz_transpuesta

def suma_matrices(matriz1, matriz2):
    filas = len(matriz1)
    columnas = len(matriz1[0])
    
    matriz_respuesta = []
    for i in range(filas):
        fila_suma = []
        for j in range(columnas):
            suma_elemento=matriz1[i][j] + matriz2[i][j] 
            fila_suma.append(suma_elemento)
        matriz_respuesta.append(fila_suma)
    return matriz_respuesta
    
        
matriz1= [[2,8],[4,10]]
matriz2= [['a','b','c'],['d','e','f'],['g','h','i']]
 
print("Matriz 1: ")
imprime_matriz(matriz1)
print('Matriz 2: ')
imprime_matriz(matriz2)

print("Transponer Matriz 2: ")
imprime_matriz(transponer_matrices(matriz2))

"""
print("Ingrese Matriz 3:")
matriz3 = ingresa_matriz(2,3)

imprime_matriz(matriz3)
"""

matriz_nueva = ingresa_matriz(2,2)
matriz_nueva_transpuesta = transponer_matrices(matriz_nueva)
imprime_matriz(matriz_nueva_transpuesta)
#en una sola linea
#imprime_matriz(transponer_matrices(ingresa_matriz(2,2)))

imprime_matriz(suma_matrices(matriz_nueva, matriz1))

