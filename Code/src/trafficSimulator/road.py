from scipy.spatial import distance
from collections import deque

class Road:
    def __init__(self, start, end, merging, sim):
        self.start = start
        self.end = end
        self.sim = sim
        
        self.is_merging = merging
        self.merging_queue = deque()

        self.vehicles = deque()

        self.init_properties()

    def init_properties(self):
        self.length = distance.euclidean(self.start, self.end)
        self.angle_sin = (self.end[1]-self.start[1]) / self.length
        self.angle_cos = (self.end[0]-self.start[0]) / self.length
        # self.angle = np.arctan2(self.end[1]-self.start[1], self.end[0]-self.start[0])
        self.has_traffic_signal = False

    def set_traffic_signal(self, signal, group):
        self.traffic_signal = signal
        self.traffic_signal_group = group
        self.has_traffic_signal = True

    @property
    def traffic_signal_state(self):
        if self.has_traffic_signal:
            i = self.traffic_signal_group
            return self.traffic_signal.current_cycle[i]
        return True

    def update(self, dt):
        n = len(self.vehicles)

        if n > 0:
            # Update first vehicle
            self.vehicles[0].update(None, dt)
            # Update other vehicles
            for i in range(1, n):
                lead = self.vehicles[i-1]
                self.vehicles[i].update(lead, dt)

            # Check merging road
            first = self.vehicles[0] 
            if first.current_road_index < len(first.path) - 1:
                next_road = self.sim.roads[first.path[first.current_road_index + 1]]
                if next_road.is_merging:
                    next_road.merging_queue.append(first)
                    if next_road.merging_queue.index(first) == 0:
                        print('Vehicle can pass')
            
            # Check for traffic signal
            if self.traffic_signal_state:
                # If traffic signal is green or doesn't exist
                # Then let vehicles pass
                self.vehicles[0].unstop()
                for vehicle in self.vehicles:
                    vehicle.unslow()
            else:
                # If traffic signal is red
                if self.vehicles[0].x >= self.length - self.traffic_signal.slow_distance:
                    # Slow vehicles in slowing zone
                    self.vehicles[0].slow(self.traffic_signal.slow_factor*self.vehicles[0]._v_max)
                if self.vehicles[0].x >= self.length - self.traffic_signal.stop_distance and\
                   self.vehicles[0].x <= self.length - self.traffic_signal.stop_distance / 2:
                    # Stop vehicles in the stop zone
                    self.vehicles[0].stop()
