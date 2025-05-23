from matplotlib import pyplot as plt
import numpy as np

def plot_log():
    x = np.linspace(0, 3, 100)
    y = np.log(x)
    plt.plot(x, y)
    plt.title('Log plot')
    plt.xlabel('x')
    plt.ylabel('log(x)')
    plt.legend(['log(x)'])
    plt.show()

def plot_sin_cos():
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)*2
    y2 = np.cos(x)*2+5
    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.plot(x, y1, "b")
    ax1.set_title("2sinx")
    ax2.plot(x, y2, "r")
    ax2.set_title("2cosx+5")
    ax1.legend(["2sinx"], loc="upper left")
    ax2.legend(["2cosx+5"], loc="upper left")
    plt.show()

plot_sin_cos()
plot_log()