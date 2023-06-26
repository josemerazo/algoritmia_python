# de un arregLo de nùmeros determinar cual es el mayor

arreglo= [54,63,30,96,47,62,32,89,100]
num_mayor = -50000

for elemento in arreglo:
    if(elemento>num_mayor):
        num_mayor = elemento
        
print("El numero mayor es ", num_mayor)

num_menor= 5000
for elemento in arreglo:
    if (elemento<num_menor):
        num_menor = elemento
print("El numero menor es ", num_menor)