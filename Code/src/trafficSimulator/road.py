from scipy.spatial import distance
from collections import deque

class Road:
    def __init__(self, start, end, merging, sim, speed_lim = float('Inf')):
        self.start = start
        self.end = end
        self.sim = sim

        self.is_merging = merging
        self.merging_queue = deque()
        self.removed_queue = deque()
        self.speed_lim = speed_lim

        self.vehicles = deque()

        self.init_properties()

    def init_properties(self):
        self.length = distance.euclidean(self.start, self.end)
        self.angle_sin = (self.end[1]-self.start[1]) / self.length
        self.angle_cos = (self.end[0]-self.start[0]) / self.length
        # self.angle = np.arctan2(self.end[1]-self.start[1], self.end[0]-self.start[0])
        self.has_traffic_signal = False
        self.intersection_slow_factor = 0.4
        self.intersection_stop_distance = 4
        self.intersection_slow_distance = 12

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
            first = self.vehicles[0]
            if first.current_road_index < len(first.path) - 1:
                next_road = self.sim.roads[first.path[first.current_road_index + 1]]
                if len(next_road.vehicles) >= 1:
                    lead = next_road.vehicles[-1]
                    first.update(lead,dt,isFirst = True,remaining = self.length - first.x)
                else:
                    self.vehicles[0].update(None, dt)
            else:
                first.update(None,dt)

            # Update other vehicles
            for i in range(1, n):
                lead = self.vehicles[i-1]
                self.vehicles[i].update(lead, dt)

            if self.is_merging and self.vehicles[-1].x >= 2 and\
                self.removed_queue.count(self.vehicles[n - 1]) == 0:
                self.removed_queue.append(self.vehicles[n-1])
                self.merging_queue.popleft()

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

            # Check merging road
            if first.current_road_index < len(first.path) - 1:
                next_road = self.sim.roads[first.path[first.current_road_index + 1]]
                if next_road.is_merging and (first.x >= self.length - self.intersection_slow_distance):

                    # add to waiting queue
                    if next_road.merging_queue.count(first) == 0:
                        next_road.merging_queue.append(first)

                    # slow down if not first
                    if next_road.merging_queue.index(first) != 0:
                        factor = (self.length - first.x)/(self.intersection_slow_distance) \
                                    * self.intersection_slow_factor
                        first.slow(factor * first._v_max)
                        # Stop vehicles in the stop zone
                        if first.x >= self.length - self.intersection_stop_distance and\
                            first.x <= self.length - self.intersection_stop_distance / 2:
                            first.stop()
                   # if first is at index 0 of waiting queue it can pass
                    else:
                        first.unstop()
                        for vehicle in self.vehicles:
                            vehicle.unslow()
