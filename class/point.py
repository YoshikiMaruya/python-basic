from math import sqrt

class Point:
  def __init__(self, x: float = 0.0, y: float = 0.0) -> float:
    self.x = x
    self.y = y
  def difference(self, point: float = None) -> float:
    if not point:
      point = Point()
    return sqrt((self.x - point.x) **2 + (self.y - point.y) **2)

point = Point(1.0, 1.0)
print(point.difference())
print(dir(point))
