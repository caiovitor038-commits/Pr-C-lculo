import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

x = sp.symbols('x')

f_expr = 2*sp.sin(x) #Função 1
g_expr = sp.cos(x) #Função 2

f = sp.lambdify(x, f_expr, "numpy")
g = sp.lambdify(x, g_expr, "numpy")

x_vals = np.linspace(-2*np.pi, 2*np.pi, 250) #Intervalo

plt.plot(x_vals, f(x_vals),
         label=r"$f(x) = " + sp.latex(f_expr) + "$",
         linewidth=2)

plt.plot(x_vals, g(x_vals),
         label=r"$g(x) = " + sp.latex(g_expr) + "$",
         linewidth=2)

plt.axhline(0, ls=':', color='k')
plt.axvline(0, ls=':', color='k')
plt.legend()
plt.title("Gráfico das funções")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.savefig("seno_cosseno.png", dpi=300, bbox_inches='tight')
plt.show()