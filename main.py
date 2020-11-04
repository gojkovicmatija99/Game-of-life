import time

from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from modules.processPool import processPool
from modules.serial import serial

def animate(steps):

    def init():
        im.set_data(steps[0])
        return [im]

    def animate(i):
        im.set_data(steps[i])
        return [im]

    im = plt.matshow(steps[0], interpolation='None', animated=True);

    anim = FuncAnimation(im.get_figure(), animate, init_func=init,
                         frames=len(steps), interval=500, blit=True, repeat=False);
    return anim


if __name__ == '__main__':
    n = 500
    iterations = 5
    parts = 8
    print("Starting...")
    start = time.time()
    #steps = serial(n, iterations)
    steps = processPool(n, iterations, parts)
    sec = time.time() - start
    print(f"End {sec} s")
    anim = animate(steps)
    f = open("animation.html", "w")
    f.write(anim.to_html5_video())
    f.close()