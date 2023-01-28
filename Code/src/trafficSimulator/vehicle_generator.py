from .vehicle import Vehicle
from numpy.random import randint
import numpy as np
from scipy import interpolate as ip

class VehicleGenerator:
    def __init__(self, sim, config={}):
        self.sim = sim
        
        # Set default configurations
        self.set_default_config()

        # Update configurations
        for attr, val in config.items():
            setattr(self, attr, val)

        # Calculate properties
        self.init_properties()

    def set_default_config(self):
        """Set default configuration"""
        self.vehicles = [
            (1, {})
        ]
        self.last_added_time = 0
        self.vehicle_weight = 'const'
        self.v_max = 16.6
    
    def variable_vehicle_rate(self,time):
        if self.vehicle_rate == 'variable': 
            if(time>=9300): return 0.01
            t = np.array([0, 0, 0, 0, 45, 70, 80, 100, 115, 155, 155, 155, 155] )
            c = [96, 197.66604206, -87.57521343, 145.25315264, -30.11543723, 180.5093985, -124.12274568, 265.26061658, 3, 0, 0, 0, 0] 
            k = 3
            return (ip.BSpline(t,c,k)(time/60) / 100 ) * 16.4
        else: 
            return self.vehicle_rate

    def init_properties(self):
        self.upcoming_vehicle = self.generate_vehicle(0)

    def generate_vehicle(self, time):
        """Returns a random vehicle from self.vehicles with random proportions"""
        if self.vehicle_weight == 'const':
            total = sum(pair[0] for pair in self.vehicles)
        elif self.vehicle_weight == 'variable':
            total = sum(pair[0](time) for pair in self.vehicles)
        else:
            assert False
        r = randint(1, total+1)
        for (weight, config) in self.vehicles:
            if self.vehicle_weight == 'const':
                r -= weight
            elif self.vehicle_weight == 'variable':
                r -= weight(time)
            if r <= 0:
                return Vehicle(config,self.v_max,time)

    def update(self):
        """Add vehicles"""
        if self.sim.t - self.last_added_time >= 60 / self.variable_vehicle_rate(self.sim.real_time):
            # If time elasped after last added vehicle is
            # greater than vehicle_period; generate a vehicle
            road = self.sim.roads[self.upcoming_vehicle.path[0]]      
            if len(road.vehicles) == 0\
               or road.vehicles[-1].x > self.upcoming_vehicle.s0 + self.upcoming_vehicle.l:
                # If there is space for the generated vehicle; add it
                self.upcoming_vehicle.time_added = self.sim.t
                road.vehicles.append(self.upcoming_vehicle)
                self.sim.num_vehicles += 1
                self.sim.total_vehicles += 1
                # Reset last_added_time and upcoming_vehicle
                self.last_added_time = self.sim.t
            elif not road.vehicles[-1].x > self.upcoming_vehicle.s0 + self.upcoming_vehicle.l: 
                self.sim.dropped += 1
            self.upcoming_vehicle = self.generate_vehicle(self.sim.real_time)

