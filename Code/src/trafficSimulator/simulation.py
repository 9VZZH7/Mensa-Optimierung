from .road import Road
from copy import deepcopy
from .vehicle_generator import VehicleGenerator
from .traffic_signal import TrafficSignal
import numpy as np

class Simulation:
    def __init__(self, config={}):
        # Set default configuration
        self.set_default_config()

        # Update configuration
        for attr, val in config.items():
            setattr(self, attr, val)

    def set_default_config(self):
        self.t = 0.0            # Time keeping
        self.frame_count = 0    # Frame count keeping
        self.real_time = 0      # Keep track of the real time
        self.dt = 1/60          # Simulation time step
        self.num_vehicles = 0
        self.total_vehicles = 0
        self.dropped = 0
        self.roads = []         # Array to store roads
        self.generators = []
        self.traffic_signals = []
        self.vehicle_dist = []
        self.waiting_times = []

    def create_road(self, start, end, merging = False, speed_lim = float('inf')):
        road = Road(start, end, merging, self, speed_lim = speed_lim)
        self.roads.append(road)
        return road

    def create_roads(self, road_list):
        for road in road_list:
            self.create_road(*road)

    def create_gen(self, config={}):
        gen = VehicleGenerator(self, config)
        self.generators.append(gen)
        return gen

    def create_signal(self, roads, config={}):
        roads = [[self.roads[i] for i in road_group] for road_group in roads]
        sig = TrafficSignal(roads, config)
        self.traffic_signals.append(sig)
        return sig

    def update(self):
        # Update every road
        for road in self.roads:
            road.update(self.dt)

        # Add vehicles
        for gen in self.generators:
            gen.update()

        for signal in self.traffic_signals:
            signal.update(self)

        # Check roads for out of bounds vehicle
        for road in self.roads:
            # If road has no vehicles, continue
            if len(road.vehicles) == 0: continue
            # If not
            vehicle = road.vehicles[0]
            # If first vehicle is out of road bounds
            if vehicle.x >= road.length:
                # If vehicle has a next road
                if vehicle.current_road_index + 1 < len(vehicle.path):
                    # Update current road to next road
                    vehicle.current_road_index += 1
                    # Create a copy and reset some vehicle properties
                    new_vehicle = vehicle # deepcopy(vehicle)
                    new_vehicle.x = 0
                    # Add it to the next road
                    next_road_index = vehicle.path[vehicle.current_road_index]
                    self.roads[next_road_index].vehicles.append(new_vehicle)
                    # Check if next road has speed limit
                    if self.roads[next_road_index].speed_lim != float('inf'):
                        new_vehicle._v_max = min(new_vehicle._v_max,self.roads[next_road_index].speed_lim)
                    else:
                        new_vehicle._v_max = 16.6
                    # Check for traffic lights
                    if self.roads[next_road_index].has_traffic_signal:
                        self.roads[next_road_index].traffic_signal.increment()
                else:
                    self.num_vehicles -= 1
                    self.waiting_times.append(self.real_time - vehicle.die())
                # In all cases, remove it from its road
                road.vehicles.popleft()
        # Increment time
        self.t += self.dt
        self.frame_count += 1
        if self.frame_count % 41 ==0:
            self.real_time += 1
        self.vehicle_dist.append(self.num_vehicles)


    def run(self, steps):
        if steps == 'whole':
            while self.real_time < 10200:
                self.update()
            self.evaluate()
        else:
            for _ in range(steps):
                self.update()
                
    def evaluate(self):
        self.norm = np.linalg.norm(self.waiting_times) / np.sqrt(len(self.waiting_times))
                