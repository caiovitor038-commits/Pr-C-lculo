import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

F = sp.Function('F')
x = sp.symbols('x')

x = sp.symbols("x")
f_expr = sp.sin(x) #Função analisada
df_expr = sp.diff(f_expr, x)

f = sp.lambdify(x, f_expr, "numpy")
df = sp.lambdify(x, df_expr, "numpy")


def Raízes():
        xs = np.linspace(-10, 10, 20000) #Intervalo de procura
        intervals = []

        for i in range(len(xs)-1): #Primeiro passo de aproximação para encontrar f(x) = 0
            if f(xs[i]) * f(xs[i+1]) < 0 or abs(f(xs[i])) < 1e-4:
                intervals.append((xs[i], xs[i+1]))

        def bissec(a, b): #Refinando as raízes encontradas, "Método Bissecção"
            for _ in range(60):
                m = (a + b)/2
                if f(a)*f(m) < 0:
                    b = m
                else:
                    a = m
            return (a+b)/2
        root = []
        for a,b in intervals: 
            val = round(bissec(a,b),8)
            if val not in root:
                root.append(val)
        return root

if len(Raízes()) > 0:
    r = Raízes()
else:
    r = []
    print("Nenhuma raiz encontrada")
    
inf = min(r)
sup = max(r)

if inf > 0 and sup > 0: #Intervalo para o gráfico
    x = np.linspace(0, sup + abs(sup)*0.1, 400)
elif inf < 0 and sup < 0:
    x = np.linspace(inf - abs(inf)*0.1, 0, 400)
else:
    x = np.linspace(inf - abs(inf)*0.1, sup + abs(sup)*0.1, 400)

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(x, f(x), lw=1.5)
ax.axhline(0, ls=':', color='k')
ax.axvline(0, ls=':', color='k')
ax.set_xlabel(r'$x$', fontsize=18)
ax.set_ylabel(r'$f(x)$', fontsize=18)


tol = 1e-7
R = []
for i in r: #Método de Newton para refinar todas as possíveis raízes encontradas
    xk = float(i)
    while True:
        if abs(df(xk)) < 1e-12:
            break
        x_new = xk - f(xk)/df(xk)
        if abs(x_new - xk) < tol and abs(f(x_new)) < tol:
            xk = x_new
            break
        xk = x_new

    R.append(xk)
R = np.round(np.array(R), 8)

roots = []
tol = 5e-3


for r in R: #Aproxima raízes muito parecidas
    if all(abs(r - x) > tol for x in roots):
        roots.append(r)


for i in roots: #Marca os as raízes no gráfico
    ax.plot(i, f(i), 'ro', markersize=8)

ax.set_title(r"$f(x) = " + sp.latex(f_expr) + "$")
plt.grid()
plt.show()

n = 1
for i in roots: #Mostra as raízes encontradas
    print(f"Raiz {n}: {i: .6f}")
    n += 1
plt.show()