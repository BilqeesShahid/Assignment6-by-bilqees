#CLASS_PROJECTS-06_Build_Compose_and_Decorate_A_Complete_Traditional_OOP_Practice_Series.md
#Assignment-15-Method Resolution Order (MRO) and Diamond Inheritance
#Create four classes:

# 1-A with a method show(),
# 2-B and C that inherit from A and override show(),
# 3-D that inherits from both B and C.
# 4-Create an object of D and call show() to observe MRO.

# Class A
class A:
    def show(self):
        print("Method from class A")

# Class B inherits from A
class B(A):
    def show(self):
        print("Method from class B")

# Class C inherits from A
class C(A):
    def show(self):
        print("Method from class C")

# Class D inherits from both B and C (diamond inheritance)
class D(B, C):
    pass

# Create object of D and call show() method
d = D()
d.show() #Output : Method from class B
