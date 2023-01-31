import numpy as np
from matplotlib import pyplot as plt

from trafficSimulator import *
from examples import mensa
from scipy import interpolate as ip 

def test_east_west():
    eva = []
    for _, eastwest in enumerate((0,25,50,74,100)):
        weights = spawning(eastwest / 100, 0.5, 0.5)
        sim = mensa.run(weights = weights,steps='whole', fixed_cycle = False)
        eva.append(sim)
    return eva

def plot_fun_and_stuff():
    t = np.array([0, 0, 0, 0, 45, 70, 80, 100, 115, 155, 155, 155, 155] )
    c = [96, 197.66604206, -87.57521343, 145.25315264, -30.11543723, 180.5093985, -124.12274568, 265.26061658, 3, 0, 0, 0, 0] 
    k = 3
    spline = ip.BSpline(t,c,k)
    time = np.arange(0,9300 * 41,1)
    plt.plot(spline(time / 60 / 41) * 0.27)
    
    sim = mensa.run(weights = spawning(0.72, 0.5, 0.5))
    plt.plot(sim.vehicle_dist)

