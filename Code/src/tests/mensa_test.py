'''

This file contains a lot of functions to evaluate different models and
distrubutions of students and dishes. Most of them plot the results neatly.

'''

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm

from trafficSimulator import *
from examples import mensa, mensa_with_checkouts
from scipy import interpolate as ip

from functools import partial
from joblib import Parallel, delayed

def test_east_west():
    """ Tests a realistic canteen with different distributions across east and west stairs. """
    eva = []
    for _, eastwest in enumerate((0,25,50,74,100)):
        weights = spawning(eastwest / 100, 0.5, 0.5)
        sim = mensa.run(weights = weights,steps='whole', fixed_cycle = False)
        eva.append(sim)
    return eva

def plot_student_spawning_fun():
    """ Plots the spline used to generate students and the effect it has on the model """
    t = np.array([0, 0, 0, 0, 45, 70, 80, 100, 115, 155, 155, 155, 155] )
    c = [96, 197.66604206, -87.57521343, 145.25315264, -30.11543723, 180.5093985, -124.12274568, 265.26061658, 3, 0, 0, 0, 0]
    k = 3
    spline = ip.BSpline(t,c,k)
    time = np.arange(0,9300 * 41,1)

    sim = mensa.run(steps = 'whole', weights = spawning(0.72, 0.5, 0.5))


    plt.plot(spline(time / 60 / 41) * 0.27)
    plt.plot(sim.vehicle_dist)


def var_speed_and_dist(N_speed, N_dist):
    """ Runs N_speed times N_dist non-parallelized simulations with slightly different
    values for max speed and distribution across stairs, seleted from given arrays. """
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
    ax.plot_surface(x, y, eva, cmap=cm.RdYlGn_r, linewidth=0, antialiased=False)
    plt.show()
    return eva

def par_speed_and_dist(N_speed, N_dist):
    """ Runs N_speed times N_dist parallelized simulations with slightly different v
    alues for max speed and distribution across stairs, seleted from given arrays. """
    speeds = np.arange(8, 22, 10/N_speed)
    dists = np.arange(0, 1 + 1e-6, 1/(N_dist))
    eva = np.zeros((len(speeds),len(dists)), dtype = object)
    for i in range(len(speeds)):
        speed = speeds[i]
        helper = partial(mensa_helper,steps = 'whole', fixed_cycle = False, v_max = speed)
        output = Parallel(n_jobs=5)(delayed(helper)(dist) for dist in dists)
        eva[i,:] = output
    norms = np.zeros_like(eva, dtype = np.float64)
    for i in range(len(norms)):
        for j in range(len(norms[i])):
            norms[i, j] = eva[i, j].norm
    x, y = np.meshgrid(dists, speeds)
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    ax.plot_surface(x, y, norms, cmap=cm.RdYlGn_r, linewidth=0, antialiased=False)
    plt.show()
    return eva, norms, fig, ax

def par_speed_and_dist_checkouts(N_speed, N_dist):
    """ Runs N_speed times N_dist parallelized simulations with slightly different
    values for max speed and distribution across stairs, seleted from given arrays.
    Except this time there are checkouts. """
    speeds = np.arange(8, 22, 10/N_speed)
    dists = np.arange(0, 1 + 1e-6, 1/(N_dist))
    eva = np.zeros((len(speeds),len(dists)), dtype = object)
    for i in range(len(speeds)):
        speed = speeds[i]
        helper = partial(mensa_checkout_helper,steps = 'whole', fixed_cycle = False, v_max = speed, v_rate = 32, spawn = 'const')
        output = Parallel(n_jobs=5)(delayed(helper)(dist) for dist in dists)
        eva[i,:] = output
    norms = np.zeros_like(eva, dtype = np.float64)
    for i in range(len(norms)):
        for j in range(len(norms[i])):
            norms[i, j] = eva[i, j].norm
    x, y = np.meshgrid(dists, speeds)
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    ax.plot_surface(x, y, norms, cmap=cm.RdYlGn_r, linewidth=0, antialiased=False)
    plt.show()
    return eva, norms, fig, ax

def par_speed_and_dist_const(N_speed, N_dist, rate):
    """ Runs N_speed times N_dist parallelized simulations with slightly different
    values for max speed and distribution across stairs, seleted from given arrays.
    Excpet the student spawning rate is now constant over time. """
    speeds = np.arange(8, 22, 10/N_speed)
    dists = np.arange(0, 1 + 1e-6, 1/(N_dist))
    eva = np.zeros((len(speeds),len(dists)), dtype = object)
    for i in range(len(speeds)):
        speed = speeds[i]
        helper = partial(mensa_helper,steps = 'whole', fixed_cycle = False, v_max = speed, v_rate = rate)
        output = Parallel(n_jobs=5)(delayed(helper)(dist) for dist in dists)
        eva[i,:] = output
    norms = np.zeros_like(eva, dtype = np.float64)
    for i in range(len(norms)):
        for j in range(len(norms[i])):
            norms[i, j] = eva[i, j].norm
    x, y = np.meshgrid(dists, speeds)
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    ax.plot_surface(x, y, norms, cmap=cm.RdYlGn_r, linewidth=0, antialiased=False)
    plt.show()
    return eva, norms, fig, ax

def par_speed_and_dist_const_const(N_speed, N_dist):
    """ Runs N_speed times N_dist parallelized simulations with slightly different
    values for max speed and distribution across stairs, seleted from given arrays.
    Excpet the student spawning rate is now constant over time and all dishes are
    equally likely to be picked by every student. """
    speeds = np.arange(8, 22, 10/N_speed)
    dists = np.arange(0, 1 + 1e-6, 1/(N_dist))
    eva = np.zeros((len(speeds),len(dists)), dtype = object)
    for i in range(len(speeds)):
        speed = speeds[i]
        helper = partial(mensa_helper,steps = 'whole', fixed_cycle = False, v_max = speed, v_rate = 32, spawn = 'const')
        output = Parallel(n_jobs=5)(delayed(helper)(dist) for dist in dists)
        eva[i,:] = output
    norms = np.zeros_like(eva, dtype = np.float64)
    for i in range(len(norms)):
        for j in range(len(norms[i])):
            norms[i, j] = eva[i, j].norm
    x, y = np.meshgrid(dists, speeds)
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    ax.plot_surface(x, y, norms, cmap=cm.RdYlGn_r, linewidth=0, antialiased=False)
    plt.show()
    return eva, norms, fig, ax

def mensa_helper(dist,steps, fixed_cycle, v_max, v_rate = 'variable', spawn = 'var'):
    if spawn == 'var':
        return mensa.run(weights = spawning(dist, 0.5, 0.5), steps = steps, fixed_cycle = fixed_cycle, v_max = v_max, v_rate = v_rate)
    else:
        return mensa.run(weights = const_spawning(2*(dist),2*(dist),dist,dist,1-dist,1-dist,2*(1-dist),2*(1-dist)), steps = steps, fixed_cycle = fixed_cycle, v_max = v_max, v_rate = v_rate, v_weight = 'const')

def mensa_checkout_helper(dist,steps, fixed_cycle, v_max, v_rate = 'variable', spawn = 'var'):
    if spawn == 'var':
        return mensa_with_checkouts.run(weights = spawning(dist, 0.5, 0.5), steps = steps, fixed_cycle = fixed_cycle, v_max = v_max, v_rate = v_rate)
    else:
        return mensa_with_checkouts.run(weights = const_spawning(2*(dist),2*(dist),dist,dist,1-dist,1-dist,2*(1-dist),2*(1-dist)), steps = steps, fixed_cycle = fixed_cycle, v_max = v_max, v_rate = v_rate, v_weight = 'const')

def test_diff_spawning():
    """ Different dishes are more likely to be picked. """
    all_same = (2,2,1,1,1,1,2,2)
    all_same_sim = mensa.run(steps = 'whole', fixed_cycle = False, v_weight = 'const', weights = const_spawning(*all_same), v_rate = 20)

    side_heavy = (10,10,1,1,1,1,10,10)
    side_heavy_sim = mensa.run(steps = 'whole', fixed_cycle = False, v_weight = 'const', weights = const_spawning(*side_heavy), v_rate = 20)

    mid_heavy = (1,1,5,5,5,5,1,1)
    mid_heavy_sim = mensa.run(steps = 'whole', fixed_cycle = False, v_weight = 'const', weights = const_spawning(*mid_heavy), v_rate = 20)
    # refernece
    vgl_times = mensa.run(steps = 'whole', fixed_cycle = False, v_weight = 'variable', weights = spawning(0.7,0.5,0.5), v_rate = 20)
    return all_same_sim, side_heavy_sim, mid_heavy_sim, vgl_times

def test_diff_dishes():
    """ There are counters that don't offer dishes anymore. """
    all_same = (1,0,0,1,1,0,0,1)
    one_per_side = mensa.run(steps = 'whole', fixed_cycle = False, v_weight = 'const', weights = const_spawning(*all_same), v_rate = 20)

    side_heavy = (0,0,1,1,1,1,0,0)
    all_mid = mensa.run(steps = 'whole', fixed_cycle = False, v_weight = 'const', weights = const_spawning(*side_heavy), v_rate = 20)

    mid_heavy = (2,0,1,1,0,0,2,2)
    less_left = mensa.run(steps = 'whole', fixed_cycle = False, v_weight = 'const', weights = const_spawning(*mid_heavy), v_rate = 20)
    # reference
    vgl_times = mensa.run(steps = 'whole', fixed_cycle = False, v_weight = 'variable', weights = spawning(0.7,0.5,0.5), v_rate = 20)
    return one_per_side, all_mid, less_left, vgl_times

def plot_diff_spawning():
    ass, shs, mhs, vgl = test_diff_spawning()
    fig, ax = plt.subplots()
    dists = ['Jedes Essen gleich', 'Essen an der Seite beliebt', 'Essen in der Mitte beliebt', 'Vergleich, Realität']
    norms = [ass.norm, shs.norm, mhs.norm, vgl.norm]
    ax.bar(dists,norms)
    ax.set_ylabel('Warte-Norm')
    plt.show()

def plot_less_dishes():
    ass, shs, mhs, vgl = test_diff_dishes()
    fig, ax = plt.subplots()
    dists = ['Nur ein Gericht pro Seite', 'Nur in der Mitte', 'Alternativkonzept', 'Vergleich, Realität']
    norms = [ass.norm, shs.norm, mhs.norm, vgl.norm]
    ax.bar(dists,norms)
    ax.set_ylabel('Warte-Norm')
    plt.show()

def test_tabletts_abholen():
    """ Testing the influence of slow students picking up their trays. """
    times = []
    lim = [2, 4, 8, 10, float('inf')]
    x_label = [2, 4, 8, 10, 'INF']
    for i in lim:
        times.append(mensa.run(steps = 'whole', fixed_cycle = False, speed_lim = i).norm)
    plt.plot(x_label,times)
