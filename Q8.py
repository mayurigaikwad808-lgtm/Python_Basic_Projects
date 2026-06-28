# Program: Employee Class with Dictionary

class Employee:
    # constructor to initialize employee details
    def __init__(self, emp_id, name, details):
        self.emp_id = emp_id
        self.name = name
        self.details = details   # tuple (department, salary)
    
    # method to show details
    def show_details(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Department:", self.details[0])
        print("Salary:", self.details[1])
        print()   # blank line for neat output

# --- main program ---
# dictionary to store employees (emp_id as key)
employees = {}

# add 3 employees
employees["E101"] = Employee("E101", "Gaikwad Mayuri", ("HR", 30000))
employees["E102"] = Employee("E102", "Sneha Jadhav", ("IT", 45000))
employees["E103"] = Employee("E103", "Mohini Sharma", ("Finance", 40000))

# display all employees using loop
print("\n--- Employee Records ---")
for emp_id, emp_obj in employees.items():
    emp_obj.show_details()
