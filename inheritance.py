class A:   #super class
    def __init__(self):
        print("In A init")
        
    def feature1(self):
        print("Feature 1 Working")

    def feature2(self):
        print("Feature 2 working")


class B(A):    # B inheriting from A #single level inheritance   #sub class
    def __init__(self):
        super().__init__()
        print("In B init")

    def feature3(self):
        print("Feature 3 Working")

    def feature4(self):
        print("Feature 4 working")


class C(B):   #multi level inheritance
    def feature5(self):
        print("Feature 5 Working")

class D:
    def __init__(self):
        print("In D init")

    def feature6(self):
        print("Feature 6 working")

class E(D,A):  #multiple inheritance

    def __init__(self):
        super().__init__()
        print("In E init")
    def feature6(self):
        print("Feature 6 working")

    def feat(self):
        super().feature1()


c = C()
c.feature1()

e = E()
e.feature2()

print("******************Below we learn constructor inheritance**********************")

b = B()    #at first it will check init of the class B.if it is not there it will go to the super class and go on  but if
           # it is present it will stop there


"""
If we want to call the both the both the init function we have to use super keyword
"""

"""  Method Resolution Order (MRO)
in multiple inheritance the order of precedenceof super class will be left to right.

"""
e = E()
e.feat()
