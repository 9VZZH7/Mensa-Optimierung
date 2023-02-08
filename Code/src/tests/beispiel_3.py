'''
Improved concept like beispiel_2, but this time with checkouts.
'''
from trafficSimulator import *
from examples import mensa, mensa_with_checkouts

mensa_with_checkouts.run(steps = 300, v_weight = 'variable', weights = spawning(0.5,0.5,0.5), fixed_cycle = False, v_rate = 35)
pygame.quit()
