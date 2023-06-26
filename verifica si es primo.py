
#ingresar un número y identificar si es primo

print("* * * Verificar si es primo")

numero = int(input("Ingrese número: "))


contador_divisible = 0
for i in range(1,numero+1):
    if(numero % i == 0):
        contador_divisible += 1
if(contador_divisible==2):
    print("Es un número es primo")
else:
    print("No es un número primo")
    
