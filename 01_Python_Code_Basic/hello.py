class Student:
    def name(self):
        print('I am a Student.')

zawad=Student()
awad="Awad"
zawad.name()
print(type(zawad))
print(isinstance(zawad,Student))
print(isinstance(awad,Student))
print(id(zawad))


def name(self):
    print('I am a Student.')
