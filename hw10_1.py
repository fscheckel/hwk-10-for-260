import numpy as np
import matplotlib.pyplot as plt

#d^2x/dt^2 - (dx/dt)^2 + x + 5 = 0

def orig(r):
    return r[1]**2 - r[0] - 5

def froggy(arr, t, h, tmax):
    first = arr
    second = arr + 0.5 * h * orig(arr)
    full = []
    for i in range(tmax):
        first = first + h * orig(second)
        second = second + h * orig(first)
        full.append(first)
    return full

if __name__ == "__main__":
    tmax = 50
    arr = [1,0]
    t = np.arange(0, 50, 0.001)
    frog = froggy(arr, 0, 0.001, tmax)

    plt.figure()    
    plt.plot(t, frog)    
    plt.xlabel('time')
    plt.ylabel('displacement')
    plt.show()
