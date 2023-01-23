import numpy as np

class Vehicle:
    def __init__(self, config={}, override_vmax = None):
        # Set default configuration
        self.set_default_config()
        #self.sim = sim

        # Update configuration
        for attr, val in config.items():
            setattr(self, attr, val)

        if override_vmax is not None:
            self.v_max = override_vmax
            
        # Calculate properties
        self.init_properties()
        

    def set_default_config(self):    
        self.l = 4
        self.s0 = 2
        self.T = 1
        self.v_max = 16.6
        self.a_max = 10 # 1.44
        self.b_max = 4.61

        self.path = []
        self.current_road_index = 0

        self.x = 0
        self.v = self.v_max
        self.a = 0
        self.stopped = False

    def init_properties(self):
        self.sqrt_ab = 2*np.sqrt(self.a_max*self.b_max)
        self._v_max = self.v_max

    def update(self, lead, dt, isFirst = False, remaining = 0):
        # Update position and velocity
        if self.v + self.a*dt < 0:
            self.x -= 1/2*self.v*self.v/self.a
            self.v = 0
        else:
            self.v += self.a*dt
            self.x += self.v*dt + self.a*dt*dt/2
        
        # Update acceleration
        alpha = 0
        if lead and not isFirst:
            delta_x = lead.x - self.x - lead.l
            delta_v = self.v - lead.v

            alpha = (self.s0 + max(0, self.T*self.v + delta_v*self.v/self.sqrt_ab)) / delta_x
        elif lead and isFirst:
            delta_x = lead.x - lead.l + remaining
            delta_v = self.v - lead.v

            alpha = (self.s0 + max(0, self.T*self.v + delta_v*self.v/self.sqrt_ab)) / delta_x

        self.a = self.a_max * (1-(self.v/self.v_max)**4 - alpha**2)

        if self.stopped: 
            self.a = -self.b_max*self.v/self.v_max
        
    def stop(self):
        self.stopped = True

    def unstop(self):
        self.stopped = False

    def slow(self, v):
        self.v_max = v

    def unslow(self):
        self.v_max = self._v_max
        

