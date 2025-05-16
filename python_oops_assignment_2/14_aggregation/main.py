# 14. Aggregation
# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a
#  Department object store a reference to an Employee object that exists independently of it.

class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def get_details(self):
        return f"Employee ID: {self.emp_id}, Name: {self.name}"

class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  # Aggregation: Department has an Employee

    def show_department_info(self):
        return f"Department: {self.dept_name}, {self.employee.get_details()}"

# Create an Employee object (exists independently)
emp1 = Employee("Muhammad Tariq Mahboob", 205)

# Create a Department object and associate it with the Employee
dept1 = Department("Air Engineering PAF", emp1)

# Display department info
print(dept1.show_department_info())


    