class car:
    def __init__(self,name,color):
        self.name=name
        self.color=color

    def __str__(self):
        return (f'{self.name}, {self.color}')

    def __eq__(self, other):
        return self.name==other.name and self.color==other.color

    def view(self):
        print(self.name,self.color)



c1=car('BMW','red')
c2=car('BMW','green')

print(c1==c2)


