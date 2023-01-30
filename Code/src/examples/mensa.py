import numpy as np

import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from trafficSimulator import *

def run(v_max = 16.6, v_rate = 'variable', v_weight = 'variable', weights = spawning(ostwest = 0.5,essen3 = 0.5,essen4 = 0.5)):
    sim = Simulation()
    
    n = 15
    
    # Nodes
    STAIRS_WEST = (-98, 42)
    EDGE_WEST = (-98, 105)
    TRAY_RACK_WEST = (-86, 105)
    DIVERSION_WEST = (-86, 84)
    
    FOOD_ONE_WEST = (-70, 63)
    FOOD_TWO_WEST = (-56, 56)
    FOOD_THREE_WEST = (-28, 49)
    
    FIRST_INTERSECTION_WEST = (-70, 56)
    SECOND_INTERSECTION_WEST = (-66.5, 49)
    THIRD_INTERSECTION_WEST = (-49, 21)
    
    END_WEST = (-49, 0)
    
    STAIRS_EAST = (98, 42)
    EDGE_EAST = (98, 105)
    TRAY_RACK_EAST = (86, 105)
    DIVERSION_EAST = (86, 84)
    
    FOOD_ONE_EAST = (70, 63)
    FOOD_TWO_EAST = (56, 56)
    FOOD_THREE_EAST = (28, 49)
    
    FIRST_INTERSECTION_EAST = (70, 56)
    SECOND_INTERSECTION_EAST = (66.5, 49)
    THIRD_INTERSECTION_EAST = (49, 21)
    
    END_EAST = (49, 0)
    
    CROSS_INTERSECTION = (0, 38.5)
    
    # Roads
    STAIRS_TO_EDGE_WEST = (STAIRS_WEST, EDGE_WEST)
    EDGE_TO_RACK_WEST = (EDGE_WEST, TRAY_RACK_WEST, False, 10)
    RACK_TO_DIVERSION_WEST = (TRAY_RACK_WEST, DIVERSION_WEST)
    DIVERSION_TO_ONE_WEST = curve_road(DIVERSION_WEST, FOOD_ONE_WEST, (TRAY_RACK_WEST[0], FOOD_ONE_WEST[1]), resolution=n)
    DIVERSION_TO_INTERSECT_WEST = curve_road(DIVERSION_WEST, FIRST_INTERSECTION_WEST, (TRAY_RACK_WEST[0], FIRST_INTERSECTION_WEST[1]), resolution=n)
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
    DIVERSION_TO_ONE_EAST = curve_road(DIVERSION_EAST, FOOD_ONE_EAST, (TRAY_RACK_EAST[0], FOOD_ONE_EAST[1]), resolution=n)
    DIVERSION_TO_INTERSECT_EAST = curve_road(DIVERSION_EAST, FIRST_INTERSECTION_EAST, (TRAY_RACK_EAST[0], FIRST_INTERSECTION_EAST[1]), resolution=n)
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
        ONE_TO_INTERSECT_EAST,
        INTERSECT_TO_TWO_EAST,
        FIRST_INTERSECT_TO_INTERSECT_EAST,
        INTERSECT_TO_THREE_EAST,
        TWO_TO_INTERSECT_EAST,
        SECOND_INTERSECT_TO_INTERSECT_EAST,
        INTERSECT_TO_END_EAST,
        THREE_EAST_TO_CROSS_INTERSECT,
        CROSS_INTERSECT_TO_ALL_WEST,
        *DIVERSION_TO_ONE_WEST,
        *DIVERSION_TO_INTERSECT_WEST,
        *THREE_TO_INTERSECT_WEST,
        *DIVERSION_TO_ONE_EAST,
        *DIVERSION_TO_INTERSECT_EAST,
        *THREE_TO_INTERSECT_EAST
    ])

    sim.create_signal([[4, 6, 16, 18, 24+n-1, 24+4*n-1]])
    # sim.create_signal([[5]])
    # sim.create_signal([[14]])
    # sim.create_signal([[16]])

    def road(a): return range(a, a+n)
    
    sim.create_gen({
        'vehicle_rate': v_rate,
        'vehicle_weight': v_weight, # can be set to variable. Weight needs to be callable
        'v_max': v_max,
        'vehicles': [
            [weights.essen_1, {'path': [0, 1, 2, *road(24), 3, 5, 8, 9]}],
            [weights.essen_2, {'path': [0, 1, 2, *road(24+n), 4, 7, 8, 9]}],
            [weights.essen_3_west, {'path': [0, 1, 2, *road(24+n), 5, 6, *road(24+2*n), 9]}],
            [weights.essen_3_ost, {'path': [0, 1, 2, *road(24+n), 5, 6, 10, 11, 20]}],
            [weights.essen_6, {'path': [12, 13, 14, *road(24+3*n), 15, 17, 20, 21]}],
            [weights.essen_5, {'path': [12, 13, 14, *road(24+4*n), 16, 19, 20, 21]}],
            [weights.essen_4_ost, {'path': [12, 13, 14, *road(24+4*n), 17, 18, *road(24+5*n), 21]}],
            [weights.essen_4_west, {'path': [12, 13, 14, *road(24+4*n), 17, 18, 22, 23, 9]}],
        ]
    })
    
    # Start simulation
    
    win = Window(sim)
    win.zoom = 4
    win.run(steps_per_update=100)
    return sim

if __name__ == "__main__":
    run()
