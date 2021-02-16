class Employee:
    first_name = ""
    last_name = ""
    salary = 0
    
    def __init__(self, firstName, lastName, initialSalary):
        self.first_name = firstName
        self.last_name = lastName
        self.salary = initialSalary

    def get_salary(self):
        return self.salary
    
    def set_salary(self, newSalary):
        self.salary = newSalary

    def give_raise(self, payIncrease = 5000):
        self.salary += payIncrease

# I set these up for manual testing to verify my results. Figured I'd leave them here to show process.
"""
employee = Employee("Marty", "McFly", 64920)
print(f"Woah! {employee.first_name} {employee.last_name}, your salary is: ${employee.get_salary()}?! RADICAL!")

employee.give_raise()
print(f"You just got a dank nasty raise: ${employee.get_salary()}")

employee.give_raise(4500)
print(f"Bruh, all you do is win: ${employee.get_salary()}")
"""