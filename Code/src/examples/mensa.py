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
    STAIRS_WEST = (-105, 41)
    EDGE_WEST = (-105, 105)
    TRAY_RACK_WEST = (-97.5, 105)
    
    FOOD_ONE_WEST = (-75, 82.5)
    FOOD_TWO_WEST = (-60, 67.5)
    FOOD_THREE_WEST = (-15, 52.5)
    
    FIRST_INTERSECTION_WEST = (-67.5, 67.5)
    SECOND_INTERSECTION_WEST = (-60, 52.5)
    THIRD_INTERSECTION_WEST = (-45, 22.5)
    
    END_WEST = (-45, 0)
    
    STAIRS_EAST = (105, 41)
    EDGE_EAST = (105, 105)
    TRAY_RACK_EAST = (97.5, 105)
    
    FOOD_ONE_EAST = (75, 82.5)
    FOOD_TWO_EAST = (60, 67.5)
    FOOD_THREE_EAST = (15, 52.5)
    
    FIRST_INTERSECTION_EAST = (67.5, 67.5)
    SECOND_INTERSECTION_EAST = (60, 52.5)
    THIRD_INTERSECTION_EAST = (45, 22.5)
    
    END_EAST = (45, 0)
    
    CROSS_INTERSECTION = (0, 45)
    
    # Roads
    STAIRS_TO_EDGE_WEST = (STAIRS_WEST, EDGE_WEST)
    STAIRS_TO_RACK_WEST = (EDGE_WEST, TRAY_RACK_WEST, False, 10)
    RACK_TO_ONE_WEST = curve_road(TRAY_RACK_WEST, FOOD_ONE_WEST, (TRAY_RACK_WEST[0], FOOD_ONE_WEST[1]), resolution=n)
    RACK_TO_INTERSECT_WEST = curve_road(TRAY_RACK_WEST, FIRST_INTERSECTION_WEST, (TRAY_RACK_WEST[0], FIRST_INTERSECTION_WEST[1]), resolution=n)
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
    STAIRS_TO_RACK_EAST = (EDGE_EAST, TRAY_RACK_EAST, False, 10)
    RACK_TO_ONE_EAST = curve_road(TRAY_RACK_EAST, FOOD_ONE_EAST, (TRAY_RACK_EAST[0], FOOD_ONE_EAST[1]), resolution=n)
    RACK_TO_INTERSECT_EAST = curve_road(TRAY_RACK_EAST, FIRST_INTERSECTION_EAST, (TRAY_RACK_EAST[0], FIRST_INTERSECTION_EAST[1]), resolution=n)
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
        STAIRS_TO_RACK_WEST,
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
        STAIRS_TO_RACK_EAST,
        ONE_TO_INTERSECT_EAST,
        INTERSECT_TO_TWO_EAST,
        FIRST_INTERSECT_TO_INTERSECT_EAST,
        INTERSECT_TO_THREE_EAST,
        TWO_TO_INTERSECT_EAST,
        SECOND_INTERSECT_TO_INTERSECT_EAST,
        INTERSECT_TO_END_EAST,
        THREE_EAST_TO_CROSS_INTERSECT,
        CROSS_INTERSECT_TO_ALL_WEST,
        *RACK_TO_ONE_WEST,
        *RACK_TO_INTERSECT_WEST,
        *THREE_TO_INTERSECT_WEST,
        *RACK_TO_ONE_EAST,
        *RACK_TO_INTERSECT_EAST,
        *THREE_TO_INTERSECT_EAST
    ])
    
    def road(a): return range(a, a+n)
    
    sim.create_gen({
        'vehicle_rate': v_rate,
        'vehicle_weight': v_weight, # can be set to variable. Weight needs to be callable
        'v_max': v_max,
        'vehicles': [
            [weights.essen_1, {'path': [0, 1, *road(22), 2, 4, 7, 8]}],
            [weights.essen_2, {'path': [0, 1, *road(22+n), 3, 6, 7, 8]}],
            [weights.essen_3_west, {'path': [0, 1, *road(22+n), 4, 5, *road(22+2*n), 8]}],
            [weights.essen_3_ost, {'path': [0, 1, *road(22+n), 4, 5, 9, 10, 19]}],
            [weights.essen_6, {'path': [11, 12, *road(22+3*n), 13, 15, 18, 19]}],
            [weights.essen_5, {'path': [11, 12, *road(22+4*n), 14, 17, 18, 19]}],
            [weights.essen_4_ost, {'path': [11, 12, *road(22+4*n), 15, 16, *road(22+5*n), 19]}],
            [weights.essen_4_west, {'path': [11, 12, *road(22+4*n), 15, 16, 20, 21, 8]}],
        ]
    })
    
    # Start simulation
    
    win = Window(sim)
    win.zoom = 4
    win.run(steps_per_update=100)
    return sim
