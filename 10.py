class Employee:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
    def show_info(self):
        print(f"Имя: {self.name}")
        print(f"Фамилия: {self.surname}")
        print(f"Возраст: {self.age}")
emp = Employee("Иван", "Бобчик", 17)
emp.show_info()
