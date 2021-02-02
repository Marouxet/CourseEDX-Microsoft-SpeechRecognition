# Desarrollo analitico del silenciador de cámara de expansión, para ver la elección de n
import numpy as np
import matplotlib.pyplot as plt

# Camara 1

L1 = 0.953
L2 = 0.318
m = 5 #Esto está forzado, no es el resultado de ningun calculo
c= 337.3
f = np.array([20, 10, 2000])
k1 = 2*np.pi*f*L1/c
k2 = 2*np.pi*f*L2/c

TL1 = 10*np.log10(1+1/4*(m+1/m)**2*np.sin(k1*L1)**2)
TL2 = 10*np.log10(1+1/4*(m+1/m)**2*np.sin(k2*L2)**2)

plt.plot(k1, L1, k2, L2)
plt.show()