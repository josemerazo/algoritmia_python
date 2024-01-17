import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)
# Senoidal
fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()

#Linea en el plano
x = [1,2,3,4,5,6]
y = [2,4,6,8,10,12]

plt.plot(x, y, label='Linea de ejemplo')
plt.xlabel('Eje X')
plt.ylabel('Eje de las Y')
plt.title("Grafico de linea simple")
print("Se realiza gráfica con ",x,y)
plt.legend()
plt.show()



