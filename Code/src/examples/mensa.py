
'''
This is a somewhat accurate replication of the canteen at FAU Erlangen Nürnberg
There are two sets of stairs from which the students get into the canteen, 6
counters where students can pick up their food and finally 5 check outs
(not implemented here, check mensa_with_checkouts).
'''

import numpy as np

import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from trafficSimulator import *

def run(steps = 100, v_max = 16.6, v_rate = 'variable', v_weight = 'variable', weights = spawning(ostwest = 0.5,essen3 = 0.5,essen4 = 0.5), fixed_cycle = True, speed_lim = 10):
    sim = Simulation()

    n = 15

    # Nodes
    STAIRS_WEST = (-84, 42)
    EDGE_WEST = (-84, 105)
    TRAY_RACK_WEST = (-70, 105)
    DIVERSION_WEST = (-70, 63)

    FOOD_ONE_WEST = (-56, 63)
    FOOD_TWO_WEST = (-42, 56)
    FOOD_THREE_WEST = (-14, 49)

    FIRST_INTERSECTION_WEST = (-52.5, 56)
    SECOND_INTERSECTION_WEST = (-49, 49)
    THIRD_INTERSECTION_WEST = (-35, 21)

    END_WEST = (-35, 0)

    STAIRS_EAST = (84, 42)
    EDGE_EAST = (84, 105)
    TRAY_RACK_EAST = (70, 105)
    DIVERSION_EAST = (70, 63)

    FOOD_ONE_EAST = (56, 63)
    FOOD_TWO_EAST = (42, 56)
    FOOD_THREE_EAST = (14, 49)

    FIRST_INTERSECTION_EAST = (52.5, 56)
    SECOND_INTERSECTION_EAST = (49, 49)
    THIRD_INTERSECTION_EAST = (35, 21)

    END_EAST = (35, 0)

    CROSS_INTERSECTION = (0, 41)

    # Roads
    STAIRS_TO_EDGE_WEST = (STAIRS_WEST, EDGE_WEST)
    EDGE_TO_RACK_WEST = (EDGE_WEST, TRAY_RACK_WEST, False, speed_lim)
    RACK_TO_DIVERSION_WEST = (TRAY_RACK_WEST, DIVERSION_WEST)
    # DIVERSION_TO_CURVE_END_WEST = (DIVERSION_WEST, CURVE_END_WEST)
    DIVERSION_TO_ONE_WEST = (DIVERSION_WEST, FOOD_ONE_WEST)
    DIVERSION_TO_INTERSECT_WEST = (DIVERSION_WEST, FIRST_INTERSECTION_WEST)
    ONE_TO_INTERSECT_WEST = (FOOD_ONE_WEST, FIRST_INTERSECTION_WEST)
    INTERSECT_TO_TWO_WEST = (FIRST_INTERSECTION_WEST, FOOD_TWO_WEST)
    FIRST_INTERSECT_TO_INTERSECT_WEST = (FIRST_INTERSECTION_WEST, SECOND_INTERSECTION_WEST, True)
    INTERSECT_TO_THREE_WEST = (SECOND_INTERSECTION_WEST, FOOD_THREE_WEST)
    TWO_TO_INTERSECT_WEST = (FOOD_TWO_WEST, SECOND_INTERSECTION_WEST)
    SECOND_INTERSECT_TO_INTERSECT_WEST = (SECOND_INTERSECTION_WEST, THIRD_INTERSECTION_WEST, True)
    THREE_TO_INTERSECT_WEST = curve_road(FOOD_THREE_WEST, THIRD_INTERSECTION_WEST, (THIRD_INTERSECTION_WEST[0], FOOD_THREE_WEST[1]), resolution=n)
    INTERSECT_TO_END_WEST = (THIRD_INTERSECTION_WEST, END_WEST, True)
    THREE_WEST_TO_CROSS_INTERSECT = (FOOD_THREE_WEST, CROSS_INTERSECTION)
    CROSS_INTERSECT_TO_ALL_EAST = (CROSS_INTERSECTION, THIRD_INTERSECTION_EAST)

    STAIRS_TO_EDGE_EAST = (STAIRS_EAST, EDGE_EAST)
    EDGE_TO_RACK_EAST = (EDGE_EAST, TRAY_RACK_EAST, False, speed_lim)
    RACK_TO_DIVERSION_EAST = (TRAY_RACK_EAST, DIVERSION_EAST)
    # DIVERSION_TO_CURVE_END_EAST = (DIVERSION_EAST, CURVE_END_EAST)
    DIVERSION_TO_ONE_EAST = (DIVERSION_EAST, FOOD_ONE_EAST)
    DIVERSION_TO_INTERSECT_EAST = (DIVERSION_EAST, FIRST_INTERSECTION_EAST)
    ONE_TO_INTERSECT_EAST = (FOOD_ONE_EAST, FIRST_INTERSECTION_EAST)
    INTERSECT_TO_TWO_EAST = (FIRST_INTERSECTION_EAST, FOOD_TWO_EAST)
    FIRST_INTERSECT_TO_INTERSECT_EAST = (FIRST_INTERSECTION_EAST, SECOND_INTERSECTION_EAST, True)
    INTERSECT_TO_THREE_EAST = (SECOND_INTERSECTION_EAST, FOOD_THREE_EAST)
    TWO_TO_INTERSECT_EAST = (FOOD_TWO_EAST, SECOND_INTERSECTION_EAST)
    SECOND_INTERSECT_TO_INTERSECT_EAST = (SECOND_INTERSECTION_EAST, THIRD_INTERSECTION_EAST, True)
    THREE_TO_INTERSECT_EAST = curve_road(FOOD_THREE_EAST, THIRD_INTERSECTION_EAST, (THIRD_INTERSECTION_EAST[0], FOOD_THREE_EAST[1]), resolution=n)
    INTERSECT_TO_END_EAST = (THIRD_INTERSECTION_EAST, END_EAST, True)
    THREE_EAST_TO_CROSS_INTERSECT = (FOOD_THREE_EAST, CROSS_INTERSECTION)
    CROSS_INTERSECT_TO_ALL_WEST = (CROSS_INTERSECTION, THIRD_INTERSECTION_WEST)


    sim.create_roads([
        STAIRS_TO_EDGE_WEST,
        EDGE_TO_RACK_WEST,
        RACK_TO_DIVERSION_WEST,
        DIVERSION_TO_ONE_WEST,
        DIVERSION_TO_INTERSECT_WEST,
        ONE_TO_INTERSECT_WEST,
        INTERSECT_TO_TWO_WEST,
        FIRST_INTERSECT_TO_INTERSECT_WEST,
        INTERSECT_TO_THREE_WEST,
        TWO_TO_INTERSECT_WEST,
        SECOND_INTERSECT_TO_INTERSECT_WEST,
        INTERSECT_TO_END_WEST,
        THREE_WEST_TO_CROSS_INTERSECT,
        CROSS_INTERSECT_TO_ALL_EAST,
        STAIRS_TO_EDGE_EAST,
        EDGE_TO_RACK_EAST,
        RACK_TO_DIVERSION_EAST,
        DIVERSION_TO_ONE_EAST,
        DIVERSION_TO_INTERSECT_EAST,
        ONE_TO_INTERSECT_EAST,
        INTERSECT_TO_TWO_EAST,
        FIRST_INTERSECT_TO_INTERSECT_EAST,
        INTERSECT_TO_THREE_EAST,
        TWO_TO_INTERSECT_EAST,
        SECOND_INTERSECT_TO_INTERSECT_EAST,
        INTERSECT_TO_END_EAST,
        THREE_EAST_TO_CROSS_INTERSECT,
        CROSS_INTERSECT_TO_ALL_WEST,
        *THREE_TO_INTERSECT_WEST,
        *THREE_TO_INTERSECT_EAST
    ])

    sim.create_signal([[3]], config={'fixed_cycle': fixed_cycle})
    sim.create_signal([[6]], config={'fixed_cycle': fixed_cycle})
    sim.create_signal([[8]], config={'fixed_cycle': fixed_cycle})
    sim.create_signal([[17]], config={'fixed_cycle': fixed_cycle})
    sim.create_signal([[20]], config={'fixed_cycle': fixed_cycle})
    sim.create_signal([[22]], config={'fixed_cycle': fixed_cycle})



    def road(a): return range(a, a+n)

    sim.create_gen({
        'vehicle_rate': v_rate,
        'vehicle_weight': v_weight, # can be set to variable. Weight needs to be callable
        'v_max': v_max,
        'vehicles': [
            [weights.essen_1, {'path': [0, 1, 2, 3, 5, 7, 10, 11]}],
            [weights.essen_2, {'path': [0, 1, 2, 4, 6, 9, 10, 11]}],
            [weights.essen_3_west, {'path': [0, 1, 2, 4, 7, 8, *road(28), 11]}],
            [weights.essen_3_ost, {'path': [0, 1, 2, 4, 7, 8, 12, 13, 25]}],
            [weights.essen_6, {'path': [14, 15, 16, 17, 19, 21, 24, 25]}],
            [weights.essen_5, {'path': [14, 15, 16, 18, 20, 23, 24, 25]}],
            [weights.essen_4_ost, {'path': [14, 15, 16, 18, 21, 22, *road(28+n), 25]}],
            [weights.essen_4_west, {'path': [14, 15, 16, 18, 21, 22, 26, 27, 11]}]
        ]
    })

    # Start simulation
    if steps == 'whole':
        sim.run('whole')
    else:
        win = Window(sim)
        win.zoom = 4
        win.run(steps_per_update=steps)
    return sim

if __name__ == "__main__":
    run(steps = 10, fixed_cycle=False)
