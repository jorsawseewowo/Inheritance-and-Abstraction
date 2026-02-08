class Person:
    def __init__(self, fname, lname):
        self.fname=fname
        self.lname=lname
    def printname(self):
        print(f"Name: {self.fname, self.lname, self.year}")
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.year=year
child=Student("Nathan", "Yusuf", 2032)
child.printname()