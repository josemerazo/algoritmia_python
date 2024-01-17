import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('datos_generados.csv')

plt.plot(df['X'], df['Y'], label="Linea ejemplo") 
#df["X"] - toma los datos de la columna x y los convierte en un arreglo

plt.show()
