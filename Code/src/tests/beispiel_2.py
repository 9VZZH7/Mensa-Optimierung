'''
Imporved version with adjusted spawning of the students. If possible, all
students should equally use both sets of stairs. This fixes some problems
during peaks and is responsible for shorter waiting times.
'''
from trafficSimulator import *
from examples import mensa, mensa_with_checkouts

mensa.run(steps = 200, v_weight = 'variable', weights = spawning(0.5,0.5,0.5), fixed_cycle = False)
pygame.quit()
