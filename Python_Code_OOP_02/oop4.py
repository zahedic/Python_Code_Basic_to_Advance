import datetime
class Employee:
    def __init__(self,eid,name,join_in_date,position,salary):
        self.eid=eid
        self.name=name
        self.join_in_date=join_in_date
        self.position=position
        self.salary=salary

    def printing(self):
        print(f"Eid:{self.eid} Name:{self.name} Joining_date: {self.join_in_date} position{self.position} salary:{self.salary}")
x=datetime.datetime(2023,10,12)
emp=Employee(101,"awad",x,'oficer',12000)
emp.printing()