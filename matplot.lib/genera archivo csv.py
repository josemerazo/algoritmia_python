import csv
import random

# Genera datos ficticios
datos = [(i, i**3) for i in range(100)]

# Escribe los datos en un archivo CSV
nombre_archivo = 'datos_generados.csv'
with open(nombre_archivo, 'w', newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)

    # Escribe la cabecera
    escritor_csv.writerow(['X', 'Y'])

    # Escribe los datos
    escritor_csv.writerows(datos)

print(f'Se ha creado el archivo CSV: {nombre_archivo}')

