class Employee:
    def __init__(self,eid,name,position,salary):
        self.eid=eid
        self.name=name
        self.position=position
        self.__salary=salary

zawad=Employee(101,'Zawad Islam Chowdhury','CEO',150000)
print(zawad.eid)
print(zawad.name)
print(zawad.position)
print(zawad.__salary)



