import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def F(x):
    return np.sin(x)
def G(x):
    return np.cos(x)

x = np.linspace(0, 3*np.pi, 400)
y = F(x)
g = G(x)

A = max(np.max(np.abs(y)), np.max(np.abs(g)))

fig, ax = plt.subplots()
ax.set_xlim(x.min(), x.max())
ax.set_ylim(-1.1*A, 1.1*A)
ax.grid()

line, = ax.plot([], [], color="orange", linewidth=2)
line2, = ax.plot([], [], color="blue", linewidth=2)
ax.axhline(0, color="black", linewidth=1)
ax.legend(["Sen(x)", "Cos(x)"])

ax.set_title("Gráfico da função seno e cosseno")
text = ax.text(0.02, 0.45, "", transform=ax.transAxes)

def init():
    line.set_data([], [])
    line2.set_data([], [])
    text.set_text("")
    return line, line2, text


def update(frame):
    line.set_data(x[:frame], y[:frame])
    line2.set_data(x[:frame], g[:frame])
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
