class Shape:
    def __init__(self, name="Shape"):
        self.name = name

    def area(self):
        raise NotImplementedError("Subclasses must implement area method")

    def perimeter(self):
        raise NotImplementedError("Subclasses must implement perimeter method")

    def __str__(self):
        return f"{self.name}"


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__(name="Rectangle")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.name = "Square"

rect = Rectangle(4, 6)
print(rect, "Area:", rect.area(), "Perimeter:", rect.perimeter())

sq = Square(5)
print(sq, "Area:", sq.area(), "Perimeter:", sq.perimeter())
