#Uniòn e intersección de conjuntos


def interseccion(array1, array2):
    arregloResultante = []
    for elemento1 in array1:
        for elemento2 in array2:
            if elemento1 == elemento2:
                arregloResultante.append(elemento1)
    return arregloResultante

def union(array1, array2):
    respuesta = []
    for ele1 in array1:
        if not ele1 in respuesta:
            respuesta.append(ele1)
    for ele2 in array2:
        if not ele2 in respuesta:
            respuesta.append(ele2)
    return respuesta
            

arreglo1 = [1,2,7,4,5]
arreglo2 = [3,4,5,6,7]

def diferencia_simetria(array1, array2):
    resultante = []
    for ele1 in array1:
        if not ele1 in array2:
            resultante.append(ele1)
    for ele2 in array2:
          if not ele2 in array1:
              resultante.append(ele2)
    return resultante

print("Intersección", interseccion(arreglo1, arreglo2))
print("Unión", union(arreglo1, arreglo2))
print("Diferencia Simetrica", diferencia_simetria(arreglo1, arreglo2))


                
