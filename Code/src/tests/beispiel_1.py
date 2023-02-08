from trafficSimulator import *
from examples import mensa, mensa_with_checkouts

mensa.run(steps = 60, v_weight = 'variable', weights = spawning(0.85,0.5,0.5), fixed_cycle = False, speed_lim = 7, v_max = 11)
pygame.quit()
