from trafficSimulator import *
from examples import mensa, mensa_with_checkouts

mensa.run(steps = 200, v_weight = 'variable', weights = spawning(0.5,0.5,0.5), fixed_cycle = False)
pygame.quit()
