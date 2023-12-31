class User:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}")

class Employee(User):
    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id

    def get_employee_id(self):
        return self.employee_id

# Пример использования класса Employee
employee = Employee("Антоха", 15)
employee.greet()
print("Employee ID:", employee.get_employee_id())
