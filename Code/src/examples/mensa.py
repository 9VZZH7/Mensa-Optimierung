import numpy as np

import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from trafficSimulator import *

def run(steps = 100, v_max = 16.6, v_rate = 'variable', v_weight = 'variable', weights = spawning(ostwest = 0.5,essen3 = 0.5,essen4 = 0.5), fixed_cycle = True):
    sim = Simulation()
    
    n = 15
    
    # Nodes
    STAIRS_WEST = (-84, 42)
    EDGE_WEST = (-84, 105)
    TRAY_RACK_WEST = (-70, 105)
    DIVERSION_WEST = (-70, 84)
    CURVE_END_WEST = (-63, 63)
    
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
    DIVERSION_EAST = (70, 84)
    CURVE_END_EAST = (63, 63)
    
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
    EDGE_TO_RACK_WEST = (EDGE_WEST, TRAY_RACK_WEST, False, 10)
    RACK_TO_DIVERSION_WEST = (TRAY_RACK_WEST, DIVERSION_WEST)
    DIVERSION_TO_CURVE_END_WEST = curve_road(DIVERSION_WEST, CURVE_END_WEST, (DIVERSION_WEST[0], CURVE_END_WEST[1]), resolution=n)
    CURVE_END_TO_ONE_WEST = (CURVE_END_WEST, FOOD_ONE_WEST)
    DIVERSION_TO_INTERSECT_WEST = curve_road(CURVE_END_WEST, FIRST_INTERSECTION_WEST, (DIVERSION_WEST[0], CURVE_END_WEST[1]), resolution=n)
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
    EDGE_TO_RACK_EAST = (EDGE_EAST, TRAY_RACK_EAST, False, 10)
    RACK_TO_DIVERSION_EAST = (TRAY_RACK_EAST, DIVERSION_EAST)
    DIVERSION_TO_CURVE_END_EAST = curve_road(DIVERSION_EAST, CURVE_END_EAST, (DIVERSION_EAST[0], CURVE_END_EAST[1]), resolution=n)
    CURVE_END_TO_ONE_EAST = (CURVE_END_EAST, FOOD_ONE_EAST)
    DIVERSION_TO_INTERSECT_EAST = curve_road(CURVE_END_EAST, FIRST_INTERSECTION_EAST, (DIVERSION_EAST[0], CURVE_END_EAST[1]), resolution=n)
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
        CURVE_END_TO_ONE_WEST,
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
        CURVE_END_TO_ONE_EAST,
        ONE_TO_INTERSECT_EAST,
        INTERSECT_TO_TWO_EAST,
        FIRST_INTERSECT_TO_INTERSECT_EAST,
        INTERSECT_TO_THREE_EAST,
        TWO_TO_INTERSECT_EAST,
        SECOND_INTERSECT_TO_INTERSECT_EAST,
        INTERSECT_TO_END_EAST,
        THREE_EAST_TO_CROSS_INTERSECT,
        CROSS_INTERSECT_TO_ALL_WEST,
        *DIVERSION_TO_CURVE_END_WEST,
        *DIVERSION_TO_INTERSECT_WEST,
        *THREE_TO_INTERSECT_WEST,
        *DIVERSION_TO_CURVE_END_EAST,
        *DIVERSION_TO_INTERSECT_EAST,
        *THREE_TO_INTERSECT_EAST
    ])

    sim.create_signal([[3]],config={'fixed_cycle':False})
    sim.create_signal([[5]])
    sim.create_signal([[7]])
    sim.create_signal([[16]])
    sim.create_signal([[18]])
    sim.create_signal([[20]])


    def road(a): return range(a, a+n)
    
    sim.create_gen({
        'vehicle_rate': v_rate,
        'vehicle_weight': v_weight, # can be set to variable. Weight needs to be callable
        'v_max': v_max,
        'vehicles': [
            [weights.essen_1, {'path': [0, 1, 2, *road(26), 3, 4, 6, 9, 10]}],
            [weights.essen_2, {'path': [0, 1, 2, *road(26+n), 3, 5, 8, 9, 10]}],
            [weights.essen_3_west, {'path': [0, 1, 2, *road(26+n), 6, 7, *road(26+2*n), 10]}],
            [weights.essen_3_ost, {'path': [0, 1, 2, *road(26+n), 5, 7, 11, 12, 22]}],
            [weights.essen_6, {'path': [13, 14, 15, *road(26+3*n), 16, 17, 19, 22, 23]}],
            [weights.essen_5, {'path': [13, 14, 15, *road(26+4*n), 16, 18, 21, 22, 23]}],
            [weights.essen_4_ost, {'path': [13, 14, 15, *road(26+4*n), 19, 20, *road(26+5*n), 23]}],
            [weights.essen_4_west, {'path': [13, 14, 15, *road(26+4*n), 19, 20, 24, 25, 10]}],
        ]
    })
    
    # Start simulation
    if steps == 'whole':
        sim.run('whole')
    else:
        win = Window(sim)
        # win.box((0, 52.5), (28, 3.5), (125, 125, 125))
        win.zoom = 4
        win.run(steps_per_update=steps)
    return sim

if __name__ == "__main__":
    run(steps = 10, fixed_cycle=False)
