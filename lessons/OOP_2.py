# Create a class called Cordinate

"""
It should have two attributes:
  - x: float and y: float

Write a constructor that takes three parameters
  - self, x(float), and y(float)

Write a method called get_dist that takes as parameters self and other (another coordinate object).
The method should return the distance between the two coordinate objects

"""


class Cordinate:
    x: float
    y: float

    def __init__(self, x, y):
        self.x = xn
        self.y = y

    def get_dist(self, other) -> float:
        """get the distance from this coord to other coord"""
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) ** 2
        return x_diff_sq + y_diff_sq
