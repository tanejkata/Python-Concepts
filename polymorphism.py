"""
polymorphism object or method having multiple forms
we can achieve by 4 types:
  1.Duck typing
  2.operator overloading
  3.method overloading
  4.method overridding 
"""
class Students:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):  # operator overload
        m1 = self.m1+ other.m1
        m2 = self.m2+ other.m2

        s3 = Students(m1,m2)

        return s3
    
    def __gt__(self,other):
        s1 = self.m1 + self.m2
        s2 = other.m1 + other.m2

        if s1 > s2:
            return True
        else:
            return False
    
    def __str__(self):    
        return '{} {}'.format(self.m1 , self.m2)


s1 = Students(12,15)
s2 = Students(87,98)

s3 = s1 + s2

print(s3.m1 , s3.m2)

print(s1 > s2)

print(s1)

#in python we dont have method overloading but we can achieve using None given in parmaterers

print("**************************************************************************************")


#method overriding


class A:
    def show(self):
        print("In A Show")

class B(A):
    def show(self):
        print("In B Show")

a1 = B()
a1.show()

