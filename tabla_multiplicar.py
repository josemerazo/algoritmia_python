# Ingrese un nùmero y muestre la tabla de multiplicar de ese nùmero desde el 0 hasta el 12

print("* * Tabla de multiplicar * *")
num = int(input("Ingrese número: "))
contador = 0
while contador <= 12:
    print(num, " X ",contador, " = ", num * contador)
    contador=contador+1
    
# print("Fin del programa")
