class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def show_info(self):
        print(f"Имя: {self.name}")
        print(f"Зарплата: {self.salary}")
emp = Employee("Иванн", 500000)
emp.show_info()
