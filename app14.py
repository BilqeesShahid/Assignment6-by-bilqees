#CLASS_PROJECTS-06_Build_Compose_and_Decorate_A_Complete_Traditional_OOP_Practice_Series.md
#Assignment-14-Aggregation
#Create a class Department and a class Employee. Use aggregation by having a Department object 
#store a reference to an Employee object that exists independently of it.

# Class Employee
class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Employee Name: {self.name}")

# Class Department using aggregation
class Department:
    def __init__(self, dept_name, employee: Employee):
        self.dept_name = dept_name
        self.employee = employee  # Aggregation: Department has a reference to an Employee

    def show_details(self):
        print(f"Department: {self.dept_name}")
        self.employee.show()  # Access method of Employee
        

# Create an Employee object (exists independently)
emp1 = Employee("Ahmed")

# Pass it to Department (aggregation)
dept1 = Department("HR", emp1)

# Show details
dept1.show_details()

#Output
# Department: HR
# Employee Name: Ahmed
