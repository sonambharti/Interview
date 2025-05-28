"""
#   Calculate(4, 3).add(3).sub(2).div(4).mul(5).get()
"""

class Calculate:
    def __init__(self, a, b):
        self.value = a + b 
    
    def add(self, x):
        self.value += x 
        return self    # returning self here to allow chainig (as self is obj
        
    def sub(self, x):
        self.value -= x 
        return self
        
    def mul(self, x):
        self.value *= x 
        return self
        
    def div(self, x):
        if x==0:
            raise ValuError("Cannot divided by 0.")
        self.value /= x 
        return self
    def get(self):
        return self.value 
        
if __name__ == "__main__":
    res = Calculate(4, 3).add(3).sub(2).div(4).mul(5).get()
    print(f"res = {res}")
    
