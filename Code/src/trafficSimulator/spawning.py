import numpy as np

class spawning():
    
    def __init__(self,ostwest,essen3,essen4):
        assert 0 <= ostwest and ostwest <= 1
        self.ostwest = ostwest # np.array((ostwest,1-ostwest))
        self.essen3 = essen3
        self.essen4 = essen4
        
        self.weight_matrix = np.zeros((6,5))
        self.weight_matrix[0,:] = [19, 22, 22, 24, 0]
        self.weight_matrix[1,:] = [18, 22, 23, 39, 0]
        self.weight_matrix[2,:] = [32, 28, 32, 37, 0]
        self.weight_matrix[3,:] = [ 5,  6,  2,  0, 0]
        self.weight_matrix[4,:] = [13, 12, 14,  0, 0]
        self.weight_matrix[5,:] = [12, 10,  8,  0, 0]
        
        self.weights = np.zeros((4,5))
        self.weights[0,:] = [31, 32, 30, 24, 0] # Essen 1 und 6
        self.weights[1,:] = [31, 34, 37, 39, 0] # Essen 2 und 5
        self.weights[2,:] = [32, 28, 32, 37, 0] # Essen 3
        self.weights[3,:] = [ 5,  6,  2,  0, 0] # Essen 4
    
    def essen_1(self,time):
        if time > 9600: time = 10800
        val = self.weights[0, time//2700]
        return self.ostwest * val
    
    def essen_2(self,time):
        if time > 9600: time = 10800
        val = self.weights[1, time//2700]
        return self.ostwest * val
    
    def essen_3_ost(self,time):
        if time > 9600: time = 10800
        val = self.weights[2, time//2700]
        return self.ostwest * 4/3 * val * self.essen3
    
    def essen_3_west(self,time):
        if time > 9600: time = 10800
        val = self.weights[2, time//2700]
        return self.ostwest * 4/3 * val * (1 - self.essen3)
    
    def essen_4_ost(self,time):
        if time > 9600: time = 10800
        val = self.weights[3, time//2700]
        return (1 - self.ostwest) * 4 * val * self.essen4
    
    def essen_4_west(self,time):
        if time > 9600: time = 10800
        val = self.weights[3, time//2700]
        return (1 - self.ostwest) * 4 * val * (1 - self.essen4)
    
    def essen_5(self,time):
        if time > 9600: time = 10800
        val = self.weights[1, time//2700]
        return (1 - self.ostwest) * val
    
    def essen_6(self,time):
        if time > 9600: time = 10800
        val = self.weights[0, time//2700]
        return (1 - self.ostwest) * val
