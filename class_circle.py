#class to compute area of a circle
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.142*(self.radius*self.radius)
    def perimeter(self):
        return 3.142*2*self.radius
    
C=Circle(5)
print(C.area())
print(C.perimeter())