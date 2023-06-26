areadecasa = input("Ingrese el valor del área de la casa: ")
preciom2 = input("Precio por metro cuadrado: ")
valordecasaxm2 = float(areadecasa) * float(preciom2)
incluyePiscina = input("¿Desea incluir piscina? (S/N) ")
if incluyePiscina == "S":
    valordecasaxm2+=10000
print("El valor total de la casa es " + str(valordecasaxm2))