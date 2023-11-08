class Employee:
    name = None
    salary = None
    def show(self):
        print(self.name)
employee = Employee()
employee.name = "Ванек"
employee.salary = 10000
employee.show()
