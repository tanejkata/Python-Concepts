class Employee:
       
    #constructor
    def __init__(self, first, last):
        #self -> current instance
        self.first = first
        self.last = last
    
    #this can be used as normal variable
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first , self.last)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first , self.last)
    
    @fullname.setter
    def fullname(self,name):
        first,last = name.split(" ")
        self.first = first
        self.last = last
    
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first  = None
        self.last = None
    
emp_1 = Employee("Tanej","Kata")

print(emp_1.fullname)
emp_1.fullname = "Sobha Talari"
print(emp_1.email)

del emp_1.fullname