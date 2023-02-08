'''
Unoptimized (realistic) day at the canteen. As one can see there are some
problems during peak periods. A lot of students have to wait long times to get
their food.
'''

from trafficSimulator import *
from examples import mensa, mensa_with_checkouts

mensa.run(steps = 60, v_weight = 'variable', weights = spawning(0.85,0.5,0.5), fixed_cycle = False, speed_lim = 7, v_max = 11)
pygame.quit()
