class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_name(self):
        return self.name

    def get_salary(self):
        return self.salary

employees = [
Employee("Коляха", 3123123),
Employee("Иван Александрович", 10000000),
Employee("Ярослав", 50)
]

for employee in employees:
    print(employee.get_name())
    print(employee.get_salary())
    print()
