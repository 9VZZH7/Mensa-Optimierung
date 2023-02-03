import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm

from trafficSimulator import *
from examples import mensa
from scipy import interpolate as ip 

import multiprocessing as mp

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
    
    sim = mensa.run(steps = 'whole', weights = spawning(0.72, 0.5, 0.5))
    
    
    plt.plot(spline(time / 60 / 41) * 0.27)
    plt.plot(sim.vehicle_dist)


def var_speed_and_dist(N_speed, N_dist):
    eva = np.zeros((N_speed,N_dist + 1))
    speeds = np.arange(10, 20, 10/N_speed)
    dists = np.arange(0,1 + 1/N_dist, 1/N_dist)
    for i, speed in enumerate(speeds):
        for j, dist in enumerate(dists):
            w = spawning(dist, 0.5, 0.5)
            sim = mensa.run(weights = w, steps = 'whole', fixed_cycle = False, v_max = speed)
            eva[i,j] = sim.norm
    x, y = np.meshgrid(dists, speeds)
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    ax.plot_surface(x, y, eva, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    plt.show()
    return eva

def par_speed_and_dist(N_speed, N_dist):
    eva = np.zeros((N_speed,N_dist + 1))
    speeds = np.arange(10, 20, 10/N_speed)
    dists = np.arange(0,1 + 1/N_dist, 1/N_dist)
    pool = mp.Pool(mp.cpu_count())
    for i, dist in enumerate(dists):
            eva[:, i] = [pool.apply(mensa.run,args = ('whole', speed, 'variable', 'variable', spawning(dist, 0.5, 0.5), False, 10)) for speed in speeds]
    x, y = np.meshgrid(dists, speeds)
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    ax.plot_surface(x, y, eva, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    plt.show()
    pool.close()
    return eva

def test_diff_spawning():
    all_same = (2,2,1,1,1,1,2,2)
    all_same_sim = mensa.run(steps = 'whole', fixed_cycle = False, v_weight = 'const', weights = const_spawning(*all_same), v_rate = 20)
    
    side_heavy = (10,10,1,1,1,1,10,10)
    side_heavy_sim = mensa.run(steps = 'whole', fixed_cycle = False, v_weight = 'const', weights = const_spawning(*side_heavy), v_rate = 20)
    
    mid_heavy = (1,1,5,5,5,5,1,1)
    mid_heavy_sim = mensa.run(steps = 'whole', fixed_cycle = False, v_weight = 'const', weights = const_spawning(*mid_heavy), v_rate = 20)
    
    return all_same_sim, side_heavy_sim, mid_heavy_sim
