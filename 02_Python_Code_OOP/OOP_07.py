class Student:
    def __init__(self, roll, name,marks):
        self.roll = roll
        self.name = name
        self.marks=marks

    def update_roll(self, new_roll):
        self.roll = new_roll

    def update_name(self, new_name):
        self.name = new_name

    def update_marks(self, new_marks):
        self.marks = new_marks


s = Student(101,"Zahed", 90)
s.update_roll(201)
s.update_name("Zahedul Islam Chowdhury")
s.update_marks(95)



print(s.roll,s.name,s.marks )  # Zahedul 201
