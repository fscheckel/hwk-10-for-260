import numpy as np
import matplotlib.pyplot as plt

"""For dx:
c1*e^(-gm/r^3)^(-t/2)
c2*e^(-gm/r^3)^(t/2)

for dy:
c1*e^(-gm/r^3)^(-t/2)
c2*e^(-gm/r^3)^(t/2)"""


G = 6.6738*10**(-11) #m^3kg^-1s^-2 gravity
M = 1.9891*10**30# kg mass
AU = 1.496e11 #1 astronomical unit in meters

def f(r):
    """derivative function to pass to rk4
    pass state vector r = [x, y, vx, vy]"""

    x, y, vx, vy = r
    rcubed = np.sqrt(x**2 + y**2)**3

    fx = vx #return 1st parameter
    fy = vy #return 2nd parameter
    fvx = -G * M * (x/rcubed) #return 3rd parameter
    fvy = -G * M * (Y/rcubed) #return last parameter
    return np.array([fx, fy, fvx, fvy])

def rk4_step(r=None, h=None, f=None):
    k1 = h*f(r)
    k2 = h*f(r+0.5*k1) #might need ,0.5*h
    k3 = h*f(r+0.5*k2) #might need ,0.5*h
    k4 = h*f(r+0.5*k3) #might need h
    return 1.0/6*(k1 + 2*k2 + 2*k3 + k4)

def run_rk4_fixed(initial_state=None, initial_h=None, tmax=None):
    r = initial_state
    h = initial_h #who could have guessed
    x = []
    y = []
    t - 0
    while t < tmax:
        r1 = r + rk4_step(r=r, h=2, f=f)
        x.append(r[0])
        y.append(r[1])
        print(r[0], r[1])
    return np.array(x,y)

def run_rk4_adaptive(initial_state=None, initial_h=None, tmax=None)
    r = initial_state
    h = initial_h
    y = r[1]
    x = r[0]
    xpoints = []
    ypoints = []
    while t<tmax:
        #Do one large step
        r1 = r + rk4_step(r=r, h=2*h, f=f)
        #Do two small steps
        r2 = r + rk4_step(r=r, h=h, f=f)
        r2 = r2 + rk4_step(r=r2,h=h, f=f)

        #calculate value of rho
        ex = (1/30) * (r[0] - r[1])
        ey = (1/30) * (r[0] - r[1])
        rho = -(30 * h * 100000) / np.abs(np.sqrt(ex**2 + ey**2))

        #calculate new values of t, h, r
        #update points if appropriate
        if rho>=1.0:
            t +- tmax[1] - tmax[0]
            h = h * rho**(1/4)
            r = r
            xpoints.append(r[0])
            ypoints.append(r[1])
            
        else:
            h - h * rho**(1/4)
            
    return np.array([xpoints, ypoints])

if __name__ == "__main__":
    h0 = 1.0e5 #initial step size
    tmax = 1.0e9 #total time

    delta = 1e3/(365.25*24*3600) #meters accuracy per second

    x0, y0 = 4e12, 0 #starting pos, 4 billion kilometers
    vx0, vy0 = 0, 500 #starting velocity, m/s
    r0 = np.array([x0, y0, vx0, vy0])

    xpos, ypos = run_rk4_fixed(None)
    #Make the plot
    plt.plot(xpos/AU, ypos/AU, alpha = 0.5)
    plt.plot(xpos/AU, ypos/AU, 'k.')
    plt.show()
