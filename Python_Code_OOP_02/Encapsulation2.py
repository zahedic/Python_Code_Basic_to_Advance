class Person:
    def __init__(self, name, age):
        self.__name = name  # Private variable
        self.__age = age    # Private variable

    # Public method to get the name
    def get_name(self):
        return self.__name

    # Public method to set the name
    def set_name(self, new_name):
        if isinstance(new_name, str) and len(new_name) > 0:
            self.__name = new_name
        else:
            print('Invalid name')

    # Public method to get the age
    def get_age(self):
        return self.__age

    # Public method to set the age
    def set_age(self, new_age):
        if isinstance(new_age, int) and new_age > 0:
            self.__age = new_age
        else:
            print('Invalid age')

# Creating an instance of the Person class
person1 = Person('John', 30)

# Accessing and modifying the properties using public methods
print(person1.get_name())  # Output: John
print(person1.get_age())   # Output: 30

person1.set_name('Doe')
person1.set_age(35)

print(person1.get_name())  # Output: Doe
print(person1.get_age())   # Output: 35

# Trying to set invalid values
person1.set_name('')
person1.set_age(-5)
