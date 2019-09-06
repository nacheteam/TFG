import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import animation

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'o', label="Anomalías", c="red")

plt.title("Ejemplo en una dimensión")

ax.scatter([70,72,68,65,76,80,75,64,70,71], [10,10,10,10,10,10,10,10,10,10], c="blue", label="Normales")

def init():
    ax.set_xlim(0, 100)
    ax.set_ylim(5, 15)
    return ln,

def update(frame):
    xdata.append(frame)
    ydata.append(10)
    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, update, frames=np.linspace(5, 40, 100),
                    init_func=init, blit=True)

plt.legend()
inp = input("Plot or save [p/s]: ")
if inp=="p":
    plt.show()
else:
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=50000)

    ani.save('outlier_1d.mp4', writer=writer, dpi=500)
