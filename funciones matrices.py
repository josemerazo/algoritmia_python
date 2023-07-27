matriz1= [[2,8],[4,10]]
matriz2= [[5,3],[4,2]]



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
        
print("Matriz 1: ")
imprime_matriz(matriz1)
print('Matriz 2: ')
imprime_matriz(matriz2)
print("Ingrese Matriz 3:")

matriz3 = ingresa_matriz(2,3)

imprime_matriz(matriz3)




