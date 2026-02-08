class Person:
    def __init__(self, name, idnumber):
        self.name=name
        self.idnumber=idnumber
    def display(self):
        print(f"Name: {self.name}")
        print(f"ID Number: {self.idnumber}")
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary=salary
        self.post=post
        super().__init__(name, idnumber)
emp1=Employee("Nathan", 12345, 25000, "Manager")
emp1.display()