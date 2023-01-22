import numpy as np
from trafficSimulator import *

sim = Simulation()

UPPER_START = (-60,30)
LOWER_START = (-60,-30)

JUNCTION = (0,0)

END = (60,0)

UPPER_STREET = (UPPER_START, JUNCTION)
LOWER_STREET = (LOWER_START, JUNCTION)
MERGED = (JUNCTION, END, True)

sim.create_roads([
    UPPER_STREET,
    LOWER_STREET,
    MERGED
    ])

sim.create_gen({
    'vehicle_rate': 20,
    'vehicle_weight': 'variable',
    'vehicles': [
        [spawning.essen_1, {'path': [0, 2]}],
        [spawning.essen_4, {'path': [1, 2]}]
        ]
    })

# Start simulation
win = Window(sim)
win.zoom = 10
win.run(steps_per_update=1)
