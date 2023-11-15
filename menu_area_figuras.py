#Menú de calculo de área, presione 1 para el cálculo de area 
#de un rectángulo, 2 y para la de un triángulo

def area_rectangulo(b, h):
    area = b * h
    return area    

def area_triangulo():
    base = float(input("Ingrese base: "))
    altura = float(input("Ingrese altura: "))
    return (base * altura) / 2

def area_circulo():
    radio = float(input("Ingrese radio: "))
    area = 3.1416 * radio * radio
    print("El area es del circulo es ",area)
    
opcion = "0"
while opcion != "4":
    print("1.- Rectangulo")
    print("2.- Triangulo")
    print("3.- Circulo")
    print("4.- Salir")
    opcion = input("Ingrese opcion: ")
    if(opcion=="1"): #Calculo de arae de rectangulo
        base = float(input("Ingrese base:"))
        altura = float(input("Ingrese altura:"))
        respuesta = area_rectangulo(base, altura)
        print("El area es del rectangulo ",respuesta)
    elif(opcion=="2"):
        print("El area es del triangulo ",area_triangulo())
    elif(opcion=="3"):
        area_circulo()
    else:
        print("No ha ingresado la opcion correcta")
