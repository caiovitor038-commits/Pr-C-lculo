import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from matplotlib.animation import FuncAnimation

x = sp.symbols('x')
f_expr = sp.sin(x)
g_expr = sp.cos(x)

f = sp.lambdify(x, f_expr, "numpy")
g = sp.lambdify(x, g_expr, "numpy")

x = np.linspace(0, 3*np.pi, 400)


A = max(np.max(np.abs(f(x))), np.max(np.abs(g(x))))

fig, ax = plt.subplots()
ax.set_xlim(x.min(), x.max())
ax.set_ylim(-1.1*A, 1.1*A)
ax.grid()

line, = ax.plot([], [], color="orange", linewidth=2)
line2, = ax.plot([], [], color="blue", linewidth=2)
ax.axhline(0, color="black", linewidth=1)
ax.legend([r"$f(x) = " + sp.latex(f_expr) + "$", r"$g(x) = " + sp.latex(g_expr) + "$"])

ax.set_title("Gráfico de comparação")
text = ax.text(0.02, 0.45, "", transform=ax.transAxes)

def init():
    line.set_data([], [])
    line2.set_data([], [])
    text.set_text("")
    return line, line2, text


def update(frame):
    line.set_data(x[:frame], f(x[:frame]))
    line2.set_data(x[:frame], g(x[:frame]))
    text.set_text(f"x = {x[frame]:.2f}")
    return line, line2, text

ani = FuncAnimation(
    fig,
    update,
    frames=len(x),
    init_func=init,
    interval=20,
    blit=True
)

ani.save("seno.gif", writer="pillow")
plt.show()
