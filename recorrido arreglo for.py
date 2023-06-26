edad = 32
arreglo1 = [1,edad,3,4,5]

print ("Recorrido con for")
for elemento in arreglo1:
    print(elemento)


print("Recorrido con while")
indice = 0
while indice < len(arreglo1):
    print(arreglo1[indice])
    indice += 1 
