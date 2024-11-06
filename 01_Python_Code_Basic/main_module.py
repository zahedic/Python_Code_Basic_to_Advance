class Employee:
    def __init__(self,eid,name,address,phone):
        self.eid=eid
        self.name=name
        self.address=address
        self.phone=phone
        print(self.eid,self.name,self.address,self.phone)


    def salary_info(self,position,salary):
        self.position = position
        self.salary = salary
        print(self.position,self.salary)

emp = Employee(101, 'Zawad Islam Chowdhury', 'ctg', 1975625504)
if __name__=='__main__':
    emp.salary_info('CEO', 505000)
else:
    print('Information is not avaiable')





