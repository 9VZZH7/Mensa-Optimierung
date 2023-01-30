import numpy as np
from matplotlib import pyplot as plt

from trafficSimulator import *
from examples import mensa

def test_east_west():
    eva = []
    for _, eastwest in enumerate((0,25,50,74,100)):
        weights = spawning(eastwest / 100, 0.5, 0.5)
        sim = mensa.run(weights = weights)
        eva.append(sim)
    return eva
