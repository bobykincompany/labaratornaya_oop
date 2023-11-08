class Employee:
    __age = None
    __salary = None

    def getAge(self):
        return self.__age

    def getSalary(self):
        return str(self.__salary) + "$"

    def setAge(self, age):
        if age >= 0 and age <= 120:
            self.__age = age
        else:
            raise Exception("age is incorrect!")

    def setSalary(self, salary):
        self.__salary = salary

employee = Employee()
employee.setAge(22)
employee.setSalary(10080)
print(employee.getAge())
print(employee.getSalary())
