class User:
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

class Employee(User):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

employee = Employee("Иван", 343221)
employee.setName("Bobchik")
print(employee.getName())
