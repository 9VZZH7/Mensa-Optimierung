import numpy as np

import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from trafficSimulator import *

sim = Simulation()

n = 15

# Nodes
STAIRS_WEST = (-195, 210)

FOOD_ONE_WEST = (-150, 165)
FOOD_TWO_WEST = (-120, 135)
FOOD_THREE_WEST = (-30, 105)

FIRST_INTERSECTION_WEST = (-135, 135)
SECOND_INTERSECTION_WEST = (-120, 105)
THIRD_INTERSECTION_WEST = (-90, 45)

END_WEST = (-90, 0)

STAIRS_EAST = (195, 210)

FOOD_ONE_EAST = (150, 165)
FOOD_TWO_EAST = (120, 135)
FOOD_THREE_EAST = (30, 105)

FIRST_INTERSECTION_EAST = (135, 135)
SECOND_INTERSECTION_EAST = (120, 105)
THIRD_INTERSECTION_EAST = (90, 45)

END_EAST = (90, 0)

CROSS_INTERSECTION = (0, 90)

# Roads
STAIRS_TO_ONE_WEST = (STAIRS_WEST, FOOD_ONE_WEST)
STAIRS_TO_INTERSECT_WEST = (STAIRS_WEST, FIRST_INTERSECTION_WEST)
ONE_TO_INTERSECT_WEST = (FOOD_ONE_WEST, FIRST_INTERSECTION_WEST)
INTERSECT_TO_TWO_WEST = (FIRST_INTERSECTION_WEST, FOOD_TWO_WEST)
FIRST_INTERSECT_TO_INTERSECT_WEST = (FIRST_INTERSECTION_WEST, SECOND_INTERSECTION_WEST, True)
INTERSECT_TO_THREE_WEST = (SECOND_INTERSECTION_WEST, FOOD_THREE_WEST)
TWO_TO_INTERSECT_WEST = (FOOD_TWO_WEST, SECOND_INTERSECTION_WEST)
SECOND_INTERSECT_TO_INTERSECT_WEST = (SECOND_INTERSECTION_WEST, THIRD_INTERSECTION_WEST, True)
THREE_TO_INTERSECT_WEST = (FOOD_THREE_WEST, THIRD_INTERSECTION_WEST)
INTERSECT_TO_END_WEST = (THIRD_INTERSECTION_WEST, END_WEST, True)
THREE_WEST_TO_CROSS_INTERSECT = (FOOD_THREE_WEST, CROSS_INTERSECTION)
CROSS_INTERSECT_TO_ALL_EAST = (CROSS_INTERSECTION, THIRD_INTERSECTION_EAST)

STAIRS_TO_ONE_EAST = (STAIRS_EAST, FOOD_ONE_EAST)
STAIRS_TO_INTERSECT_EAST = (STAIRS_EAST, FIRST_INTERSECTION_EAST)
ONE_TO_INTERSECT_EAST = (FOOD_ONE_EAST, FIRST_INTERSECTION_EAST)
INTERSECT_TO_TWO_EAST = (FIRST_INTERSECTION_EAST, FOOD_TWO_EAST)
FIRST_INTERSECT_TO_INTERSECT_EAST = (FIRST_INTERSECTION_EAST, SECOND_INTERSECTION_EAST, True)
INTERSECT_TO_THREE_EAST = (SECOND_INTERSECTION_EAST, FOOD_THREE_EAST)
TWO_TO_INTERSECT_EAST = (FOOD_TWO_EAST, SECOND_INTERSECTION_EAST)
SECOND_INTERSECT_TO_INTERSECT_EAST = (SECOND_INTERSECTION_EAST, THIRD_INTERSECTION_EAST, True)
THREE_TO_INTERSECT_EAST = (FOOD_THREE_EAST, THIRD_INTERSECTION_EAST)
INTERSECT_TO_END_EAST = (THIRD_INTERSECTION_EAST, END_EAST, True)
THREE_EAST_TO_CROSS_INTERSECT = (FOOD_THREE_EAST, CROSS_INTERSECTION)
CROSS_INTERSECT_TO_ALL_WEST = (CROSS_INTERSECTION, THIRD_INTERSECTION_WEST)


sim.create_roads([
    STAIRS_TO_ONE_WEST,
    STAIRS_TO_INTERSECT_WEST,
    ONE_TO_INTERSECT_WEST,
    INTERSECT_TO_TWO_WEST,
    FIRST_INTERSECT_TO_INTERSECT_WEST,
    INTERSECT_TO_THREE_WEST,
    TWO_TO_INTERSECT_WEST,
    SECOND_INTERSECT_TO_INTERSECT_WEST,
    THREE_TO_INTERSECT_WEST,
    INTERSECT_TO_END_WEST,
    THREE_WEST_TO_CROSS_INTERSECT,
    CROSS_INTERSECT_TO_ALL_EAST,
    STAIRS_TO_ONE_EAST,
    STAIRS_TO_INTERSECT_EAST,
    ONE_TO_INTERSECT_EAST,
    INTERSECT_TO_TWO_EAST,
    FIRST_INTERSECT_TO_INTERSECT_EAST,
    INTERSECT_TO_THREE_EAST,
    TWO_TO_INTERSECT_EAST,
    SECOND_INTERSECT_TO_INTERSECT_EAST,
    THREE_TO_INTERSECT_EAST,
    INTERSECT_TO_END_EAST,
    THREE_EAST_TO_CROSS_INTERSECT,
    CROSS_INTERSECT_TO_ALL_WEST
])

def road(a): return range(a, a+n)

sim.create_gen({
    'vehicle_rate': 'variable',
    'vehicle_weight': 'variable', # can be set to varibale. Weight needs to be callable 
    'vehicles': [
        [spawning.essen_1, {'path': [0, 2, 4, 7, 9]}],
        [spawning.essen_2, {'path': [1, 3, 6, 7, 9]}],
        [spawning.essen_3, {'path': [1, 4, 5, 8, 9]}],
        [spawning.essen_3, {'path': [1, 4, 5, 10, 11, 21]}],
        [spawning.essen_6, {'path': [12, 14, 16, 19, 21]}],
        [spawning.essen_5, {'path': [13, 15, 18, 19, 21]}],
        [spawning.essen_4, {'path': [13, 16, 17, 20, 21]}],
        [spawning.essen_4, {'path': [13, 16, 17, 22, 23, 9]}],
    ]
})

# Start simulation
win = Window(sim)
win.zoom = 2
win.run(steps_per_update=5)