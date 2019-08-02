import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button

AXES_COLOR = 'lightgoldenrodyellow'

# pi / 4
TOTAL_DOTS = 0
RED_DOTS = 0
EST_PI = float(0)

def create_button(name, pos, color, hover_color='0.975'):
    axes = plt.axes(pos)
    return Button(axes, name, color=color, hovercolor=hover_color)


def update_next(val, axs):
    x = np.random.rand(100)
    y = np.random.rand(100)

    global TOTAL_DOTS, RED_DOTS, EST_PI
    TOTAL_DOTS += 100
    RED_DOTS += len([i for i in (x ** 2 + y ** 2) if i <= 1])
    EST_PI = RED_DOTS / TOTAL_DOTS * 4
    axs.set_title(f'N = {TOTAL_DOTS}, PI = {EST_PI}')

    col = np.where(x**2 + y ** 2 <= 1, 'r', 'k')
    axs.scatter(x, y, s=1, c=col)
    fig.canvas.draw_idle()


if __name__ == "__main__":
    fig, axs = plt.subplots()
    plt.subplots_adjust(left=0.2, bottom=0.2)
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    axs.set_title(f'N = {TOTAL_DOTS}, PI = {EST_PI}')
    # Button init
    btn_next = create_button('Next', [0.8, 0.065, 0.1, 0.04], AXES_COLOR)

    btn_next.on_clicked(lambda x: update_next(x, axs))

    plt.show()
