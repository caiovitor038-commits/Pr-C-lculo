import numpy as np
import matplotlib.pyplot as plt

def F(x):
    return np.sin(x)
def G(x):
    return np.cos(x)

x = np.linspace(-2*np.pi, 2*np.pi, 250)

y = F(x)
v = G(x)

plt.plot(x, y, label="seno", color="orange",linewidth=2)
plt.plot(x, v, label="cosseno", color="blue",linewidth=2)
plt.axhline(0, color="black", linewidth=1)
plt.axvline(0, color="black", linewidth=1)
plt.legend()    
plt.title("Gráfico da função seno e cosseno")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.show()