class Bike:
    def __init__(self,name,color):
        self.name=name
        self.color=color


    def __str__(self):
        return (f"{self.name}, {self.color}")


    def __eq__(self, other):
        return self.name==other.name and self.color==other.color


    def display(self):
        print(f"{self.name}, {self.color}")

bike1=Bike('Yamaha R15','Blue')
bike2=Bike('Yamaha R15','Blue')


print(bike1==bike2)

