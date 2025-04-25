#CLASS_PROJECTS-06_Build_Compose_and_Decorate_A_Complete_Traditional_OOP_Practice_Series.md
#Assignment-7-Access Modifiers: Public, Private, and Protected
#Create a class Employee with:

# 1-a public variable name,
# 2-a protected variable _salary, and
# 3-a private variable __ssn.
# 4-Try accessing all three variables from an object of the class and document what happens.

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # public variable
        self._salary = salary     # protected variable
        self.__ssn = ssn          # private variable  (ssn stands for Social Security Number.)

    def display_info(self):
        print("Name:", self.name)
        print("Salary:", self._salary)
        print("SSN:", self.__ssn)
        
        
emp = Employee("Alice", 50000, "123-45-6789")

# Access public variable
print("Public:", emp.name)           # ✅ Works fine

# Access protected variable
print("Protected:", emp._salary)     # ⚠️ Works, but not recommended (intended for internal use)

# Access private variable
try:
    print("Private:", emp.__ssn)     # ❌ Error: private attribute
except AttributeError as e:
    print("Private access error:", e)

# But you can access private like this (name mangling)
# Mangling discourages direct access, but does not make it truly private.:
print("Private (via name mangling):", emp._Employee__ssn)

