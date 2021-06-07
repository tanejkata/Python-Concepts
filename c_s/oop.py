#Blue print to create instance of class
class Employee:
    #class variable shared among all the instances
    #cannot directly use. only user instance.num_of_emps or Employee.num_of_emps
    #will not be added into instance dictionary
    #there will be added to Classname.__dict__()
    num_of_emps = 0
    raiseAmmount = 1.04
    
    #constructor
    def __init__(self, first, last, pay):
        #self -> current instance
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'
        
        Employee.num_of_emps += 1
    
    #class methods
    #first argument is instance
    def getName(self):
        return '{} {}'.format(self.first , self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raiseAmmount)
    
    #first argument is the Class
    @classmethod
    def set_raise_amt(cls , amount):
        cls.raiseAmmount = amount
        
    #alternate constructor
    @classmethod
    def from_string(cls , emp_str):
        first,last,pay = emp_str.split("-")
        return cls(first,last,pay)
    
    #don't operate on the instance or the class
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True
    
#instance of class
emp_1 = Employee('Tanej','Kata',2000)
emp_2 = Employee('Niha','Kata',2000)

# print(emp_2.pay)
# emp_2.apply_raise()
# print(emp_2.pay)
# Employee.set_raise_amt(1.05)
# emp_1.apply_raise()
# print(emp_1.pay)

#executing the methods for instance
# print(Employee.getName(emp_2))
# print(emp_1.getName())

# print(emp_2.email)
# emp_2.apply_raise()
# print(emp_2.pay)
# print(Employee)

#get the complete instance in dictionary format
# print(emp_2.__dict__)