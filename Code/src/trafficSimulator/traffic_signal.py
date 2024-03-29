import numpy as np

class TrafficSignal:
    def __init__(self, roads, config={}):
        # Initialize roads
        self.roads = roads
        # Set default configuration
        self.set_default_config()
        # Update configuration
        for attr, val in config.items():
            setattr(self, attr, val)
        # Calculate properties
        self.init_properties()

    def set_default_config(self):
        self.cycle = [(False, True), (True, False)]
        self.slow_distance = 12
        self.slow_factor = 0.1
        self.stop_distance = 4

        self.current_cycle_index = 0

        self.last_t = 0
        self.passed_cars = 0
        self.fixed_cycle = True
        self.cycle_delay = 150
        self.delay = np.random.randint(200,400)

    def init_properties(self):
        if not isinstance(self.fixed_cycle,bool):
            self.cycle_delay = self.fixed_cycle
            self.fixed_cycle = False
        for i in range(len(self.roads)):
            for road in self.roads[i]:
                road.set_traffic_signal(self, i)

    @property
    def current_cycle(self):
        return self.cycle[self.current_cycle_index]

    def update(self, sim):
        # switches state every 30 ticks
        if self.fixed_cycle:
            cycle_length = 30
            k = (sim.t // cycle_length) % 2
            self.current_cycle_index = int(k)
        # switches state based on the given delay, this is used to simulate a
        # more realistic canteen
        else:
            self.delay = max(0, self.delay - 1)
            if self.delay > 0:
                self.current_cycle_index = 0
            else:
                self.current_cycle_index = 1

    def increment(self):
        '''
            increment runs whenever a vehicle passes this traffic light.
            It simulates a little delay after every person. Additionally there
            is an longer delay after every 6th car to simulate the times it
            takes to prepare more dishes.
        '''
        self.passed_cars += 1
        self.delay += self.cycle_delay # self.cycle_delay = 150
        if self.passed_cars % 6 == 0:
            self.delay += 2 * self.cycle_delay
