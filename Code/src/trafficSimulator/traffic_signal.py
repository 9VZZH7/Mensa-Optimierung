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
        self.slow_distance = 50
        self.slow_factor = 0.1
        self.stop_distance = 15

        self.current_cycle_index = 0

        self.last_t = 0
        self.passed_cars = 0
        self.fixed_cycle = True

    def init_properties(self):
        for i in range(len(self.roads)):
            for road in self.roads[i]:
                road.set_traffic_signal(self, i)

    @property
    def current_cycle(self):
        return self.cycle[self.current_cycle_index]
    
    def update(self, sim):
        if self.fixed_cycle:
            cycle_length = 30
            k = (sim.t // cycle_length) % 2
            self.current_cycle_index = int(k)
        else:
            self.passed_cars = max(0, self.passed_cars - 1)
            if self.passed_cars > 0:
                self.current_cycle_index = 0
            else:
                self.current_cycle_index = 1
            
        
    def increment(self):
        self.passed_cars += 41
