class Triangle:
    def __init__(self,base,height):
        self.base=base
        self.height=height

    def area(self):
        area=0.5*self.base*self.height
        print('The Triangle Area=',area)

t1=Triangle(20,30)
t1.area()

t2=Triangle(30,40)
t2.area()

        