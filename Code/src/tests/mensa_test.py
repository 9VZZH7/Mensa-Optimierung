import numpy as np
from matplotlib import pyplot as plt

from trafficSimulator import *
from examples import mensa

sim = mensa.run()
print(sim.total_vehicles)
print(sim.waiting_times[0])
print(np.average(sim.waiting_times))
