class Triangle:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C 

    def add(self, number):
        A = self.A + number.A 
        B = self.B + number.B
        C = self.C + number.C 
        return A+B+C
        

t1 = Triangle(7,40.2,5) 
perimeter = (t1.add(t1))/2 
print("Triangle perimeter is", perimeter)      
