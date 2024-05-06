class Point:
    """A class to represent a point"""

    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return NotImplemented
