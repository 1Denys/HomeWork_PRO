class Rectangle:
    def __init__(self, length, width):
        if length <= 0 or width <= 0:
            raise ValueError
        self.length = length
        self.width = width

    def square(self):
        return self.length * self.width

    def __equal__(self, rect):
        return self.square() == rect.square()

    def __add__(self, rect):
        return Rectangle(1, self.square() + rect.square())

    def __prod__(self, num):
        self.length = self.square() * num
        self.width = 1
        return self

    def __str__(self):
        return 'Rectangle: length = {}, width = {}'. format(self.length, self.width)

i1 = Rectangle(3, 5)
i2 = Rectangle(3, 5)
i3 = i1 + i2
print(i1)
print(i2)
print(i3)
