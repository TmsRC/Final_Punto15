import numpy as np
import matplotlib.pyplot as plt

datos = np.loadtxt("datos.dat").T

plt.figure()
plt.plot(datos[1],datos[2])
plt.title("Trayectoria")
plt.ylabel("Y")
plt.xlabel("X")
plt.savefig("RubioTomas_final_15.pdf")

plt.figure()
plt.plot(datos[1],datos[2])
plt.title("Trayectoria")
plt.ylabel("Y")
plt.xlabel("X")
plt.savefig("RubioTomas_final_15.png")