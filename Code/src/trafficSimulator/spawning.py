class spawning():
    
    def __init__(self,ostwest,essen3,essen4):
        self.ostwest = ostwest
        self.essen3 = essen3
        self.essen4 = essen4
        
    def essen_1(self,time):
        if time < 2700:
            return 19
        if time < 5400:
            return 22
        if time< 8100:
            return 22
        if time < 9600: 
            return 24
        return 1
    
    def essen_2(self,time):
        if time < 2700:
            return 18
        if time < 5400:
            return 22
        if time< 8100:
            return 23
        if time < 9600: 
            return 39
        return 1
    
    def essen_3_ost(self,time):
        if time < 2700:
            return self.essen3 * 32
        if time < 5400:
            return self.essen3 * 28
        if time< 8100:
            return self.essen3 * 32
        if time < 9600: 
            return self.essen3 * 37
        return 1
    
    def essen_3_west(self,time):
        if time < 2700:
            return (1-self.essen3) * 32
        if time < 5400:
            return (1-self.essen3) * 28
        if time< 8100:
            return (1-self.essen3) * 32
        if time < 9600: 
            return (1-self.essen3) * 37
        return 1
    
    def essen_4_ost(self,time):
        if time < 2700:
            return self.essen4 * 5
        if time < 5400:
            return self.essen4 * 6
        if time< 8100:
            return self.essen4 * 2
        if time < 9600: 
            return self.essen4 * 0
        return 0
    
    def essen_4_west(self,time):
        if time < 2700:
            return (1-self.essen4) * 5
        if time < 5400:
            return (1-self.essen4) * 6
        if time< 8100:
            return (1-self.essen4) * 2
        if time < 9600: 
            return (1-self.essen4) * 0
        return 0
    
    def essen_5(self,time):
        if time < 2700:
            return 13
        if time < 5400:
            return 12
        if time< 8100:
            return 14
        if time < 9600: 
            return 0
        return 0
    
    def essen_6(self,time):
        if time < 2700:
            return 12
        if time < 5400:
            return 10
        if time< 8100:
            return 8
        if time < 9600: 
            return 0
        return 0
