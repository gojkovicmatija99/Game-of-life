from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from IPython.display import HTML, display
from processPool import processPool

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


n = 20
iterations = 20
parts = 20
steps = processPool(n, iterations, parts)
anim = animate(steps)
f = open("animation.html", "w")
f.write(anim.to_html5_video())
f.close()