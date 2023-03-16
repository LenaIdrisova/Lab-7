#Идрисова Лена, 368234, вариант 4

import numpy as np
import random
import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation, PillowWriter

def start():
    list1 = []
    for _ in range(1000000):
        list1.append(random.random())

    list2 = []
    for _ in range(1000000):
        list2.append(random.random())

    start_time1 = time.perf_counter()

    mult1 = np.multiply(list1, list2)

    end_time1 = time.perf_counter()

    all_time1 = end_time1 - start_time1

    arr1 = np.random.rand(1000000)
    arr2 = np.random.rand(1000000)

    start_time2 = time.perf_counter()

    mult2 = np.multiply(arr1, arr2)

    end_time2 = time.perf_counter()

    all_time2 = end_time2 - start_time2
    print('Разница выполения:', all_time1 - all_time2)

def hist():
    arr = np.genfromtxt('data2.csv', delimiter=',', names=True)
    hd = arr['Hardness']
    np.float_(hd)

    plt.hist(hd, color='pink', edgecolor='black', bins=20)
    plt.title('Histogram')
    plt.xlabel('hardness value')
    plt.ylabel('number')
    plt.show()

    plt.hist(hd, color='pink', edgecolor='black', bins=20, density=True)
    plt.title('Normalize histogram')
    plt.xlabel('hardness value')
    plt.ylabel('number')
    plt.show()

    print('Среднеквадратичное отклонение:', np.nanstd(hd))

def plot3d():
    x = np.linspace(-5, 5, 60)
    y = x
    z = np.sin(x ** y)

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.plot(x, y, z, c='pink')
    plt.show()

def animation():
    fig = plt.figure()
    line, = plt.plot([], [], 'k')

    plt.xlim(-7.5, 7.5)
    plt.ylim(-1.5, 1.5)

    writer = PillowWriter(fps=30)
    x_coord = []
    y_coord = []
    with writer.saving(fig, "animatoin_sin.gif", 100):
        for x in np.linspace(-7.5, 7.5, 100):
            x_coord.append(x)
            y_coord.append(np.sin(x))
            line.set_data(x_coord, y_coord)
            writer.grab_frame()

if __name__ == '__main__':
    start()
    hist()
    plot3d()
    animation()
