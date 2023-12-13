"""
Permitir el ingreso de n números por teclado,
hasta que el usuario ingrese el 0
- Cuando el usuario ingrese el 0, se deberá mostrar 
la suma de todos los números ingresados
- Se deberá mostrar la cantidad de números ingresados
por el usuario que sean múltiplos de 3
- Se deberá mostrar cuantos números primos ingresó el 
usuario
"""
def esPrimo(numero):
def esPrimo(numero):
    contador = 0
    for i in range(1,numero+1):
        if(numero%i==0):
            contador +=1
    if(contador>2):
        return False
    else:
        return True
    
acumulador = 0
contador_primos = 0
contador_mult_3 = 0
n=1
while(n!=0):
    n=int(input("Ingrese: "))
    acumulador = acumulador + n
    if n % 3 == 0:
        contador_mult_3 += 1
    if esPrimo(n):
        contador_primos += 1

print("La suma total es", acumulador)
print("Los multiplos de 3 son ", contador_mult_3)
print("La cantidad de primos es ", contador_primos)
    
