class User:
    def setName(self, name):
        self._name = name

    def getName(self):
        return self._name
user = User()
user.setName("Ярик")
print(user.getName())



class Employee(User):
    def setEmployeeId(self, employee_id):
        self._employee_id = employee_id

    def getEmployeeId(self):
        return self._employee_id
employee = Employee()
employee.setName("Ярик")
employee.setEmployeeId(300)
print(employee.getName())
print(employee.getEmployeeId())


class Programmer(Employee):
    def setSkill(self, skill):
        self._skill = skill

    def getSkill(self):
        return self._skill
programmer = Programmer()
programmer.setName("Ваня")
programmer.setEmployeeId(840)
programmer.setSkill("Python")
print(programmer.getName())
print(programmer.getEmployeeId())
print(programmer.getSkill())




class Designer(Employee):
    def setExperience(self, experience):
        self._experience = experience

    def getExperience(self):
        return self._experience
designer = Designer()
designer.setName("ДАниил")
designer.setEmployeeId(1000)
designer.setExperience("2 года")
print(designer.getName())
print(designer.getEmployeeId())
print(designer.getExperience())
