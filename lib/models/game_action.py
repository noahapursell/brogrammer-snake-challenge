from enum import Enum
from lib.models.point import Point

class GameAction(Enum):
    """A class to store a game action"""

    LEFT = Point(-1, 0)
    RIGHT = Point(1, 0)
    UP = Point(0, -1)
    DOWN = Point(0, 1)
