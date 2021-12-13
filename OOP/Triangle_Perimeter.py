class Triangle:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C 
        
    def Per(self):
        self.Perimeter = self.A + self.B + self.C
        return self.Perimeter
        

t1 = Triangle(7,40.2,5) 
P  = t1.Per()
print("Triangle perimeter is", P)      
