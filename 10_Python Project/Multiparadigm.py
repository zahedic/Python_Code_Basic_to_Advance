class Student:
    def __init__(self,roll,name,gpa):
        self.roll=roll
        self.name=name
        self.gpa=gpa

    def display(self):
        ''''
        print(f"Roll:{self.roll}")
        print(f"Name:{self.name}")
        print(f"GPA:{self.gpa}")
        '''
        print('Roll:', self.roll)
        print('Name:', self.name)
        print('GPA:', self.gpa)

s1=Student(101,'Zawad',5.00)
s1.display()