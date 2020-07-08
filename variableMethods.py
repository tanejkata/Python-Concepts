class Computer:

    def __init__(self,cpu,ram):  # It is like Constructor ,call itself and used for initializing variables
        self.cpu = cpu
        self.ram = ram


    def config(self):
        print(self.cpu , self.ram)

com1 = Computer('i5',16)
com2 = Computer('Ryzen', 8)

com1.config()   # Computer.config(com1)  <-- internally it will modify like this
com2.config()





class Computer2:
    color = "white"    # class variable

    def __init__(self):
        self.name = 'tanej'  #both are instance variables
        self.age = 22        #both are instance variables

    def compare(self, other):
        return self.age == other.age

c1 = Computer2()
c2 = Computer2()

print(c1.color)
print(c2.color)
Computer2.color = "black"  ## we can cange using this for all objects
print(c1.color)
print(c2.color)



class Student:

    school = 'Tanej University'  #class variable

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    
    def avg(self):    # instance method if we are working with instance variables 
        return (self.m1+self.m2+self.m3)/3

    @classmethod      # we have to use this decorator to use class methods
    def getSchool(cls):   # class method if we are working with class variables .  we have to use cls keyword
        return cls.school

    @staticmethod
    def info():       #static methods
        print("This is student Class. In ABC Module")



s1 = Student(10,54,53)
s2 = Student(78,84,48)



