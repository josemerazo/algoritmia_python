# adivina un numero del 1 al 10
import random
numero_secreto = random.randint(1, 10)

while(True):
    numero_usuario = int(input("Ingrese Número: "))
    if(numero_usuario == numero_secreto):
        break
print("Haz adivinado el número")
