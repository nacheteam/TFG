import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import animation

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'o', label="Anomalías", c="red")

plt.title("Ejemplo de anomalías en dos dimensiones")

ax.scatter([0,1,2,7,-3,-4,0,4,2,0,1,2,7,-3,-4,0,4,2, 100,102,98,99,100,104,106,96,94,100,102,103,98], [0,1,2,7,-3,-4,0,4,2,2,5,-3,1,-6,8,7,2,-3, 98,107,96,100,102,93,101,103,97,100,96,105,102], c="blue", label="Normales")

def init():
    ax.set_xlim(-10, 110)
    ax.set_ylim(-10, 110)
    return ln,

def update(frame):
    xdata.append(frame)
    ydata.append(frame)
    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, update, frames=np.linspace(30, 70, 100),
                    init_func=init, blit=True)

plt.legend()
inp = input("Plot or save [p/s]: ")
if inp=="p":
    plt.show()
else:
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=50000)

    ani.save('outlier_2d_case2.mp4', writer=writer, dpi=500)
