class triangle:
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def calculate_Area(self):
        Area=0.5*self.base*self.height
        print(Area)

t1=triangle(20,30)
t1.calculate_Area()