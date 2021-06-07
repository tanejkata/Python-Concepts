#dunder means  __ __

class Employee:
   
    raiseAmmount = 1.04
    
    #constructor
    def __init__(self, first, last, pay):
        #self -> current instance
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'
        
    
    def getName(self):
        return '{} {}'.format(self.first , self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raiseAmmount)
        
    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first,self.last,self.pay)
    
    def __str__(self):
        return '{} - {}'.format(self.getName(),self.email)
    
    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        pass
    
    
emp_1 = Employee('Tanej','Kata',2000)
emp_2 = Employee('Niha','Kata',2000)

print(emp_1.getName())
print(emp_2.getName())


print(repr(emp_1))
print(str(emp_1))

print(emp_1 + emp_2)
