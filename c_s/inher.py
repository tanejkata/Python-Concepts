class Employee:
    raiseAmmount = 1.04
    
    #constructor
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'
            
    #class methods
    def getName(self):
        return '{} {}'.format(self.first , self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raiseAmmount)

class Developer(Employee):
    raiseAmmount = 1.10
    
    def __init__(self, first, last, pay,prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    
    def __init__(self, first, last, pay,employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emp(self):
        for emp in self.employees:
            print('-->',emp.getName())
   
#instance of class
emp_1 = Employee('Tanej','Kata',2000)
emp_2 = Employee('Niha','Kata',2000)

dev_1 = Developer('Tanej','Kata',2000,'python')
dev_2 = Developer('Niha','Kata',2000,'Javascript')
mgr_1 = Manager("Sobha","T",9000,[dev_1,dev_2])

print(isinstance(mgr_1, Developer))

print(issubclass(Manager, Developer))

#print(help(Developer))

# print(dev_1.email)
# print(dev_1.prog_lang)

# print(dev_1.pay)
# dev_1.apply_raise()

# print(dev_1.pay)