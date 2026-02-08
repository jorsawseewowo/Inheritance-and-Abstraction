from abc import ABC, abstractmethod
class Animal(ABC):
    def move(self):
        pass
class Human(Animal):
    def move(self):
        print("Humans are the strongest beings")
class Snake(Animal):
    def move(self):
        print("Snakes can slither around")
class Dog(Animal):
    def move(self):
        print("Dogs bark and chase their own tail")
class Cat(Animal):
    def move(self):
        print("Cats are either very affectionate or aggressive")
class Dinosaur(Animal):
    def move(self):
        print("Dinosaurs are extinct")
R=Human()
R.move()
K=Snake()
K.move()
P=Dog()
P.move()
M=Cat()
M.move()
H=Dinosaur()
H.move()