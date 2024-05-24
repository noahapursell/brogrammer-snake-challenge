import numpy as np

from lib.models.point import Point

class GameState:
    """A class to store data about the current game state"""

    def __init__(self, board:np.ndarray, head_pos:Point, size:int, died:bool):
        if not isinstance(board, np.ndarray):
            raise TypeError("Board myst be a numpy.ndarray")
        if not isinstance(head_pos, Point):
            raise TypeError("head_pos must be a Point")
        self.board = board
        self.head_pos = head_pos
        self.size = size
        self.died = died

    def __str__(self):
        return f"Board: \n {self.board}\nHead Position: {self.head_pos}"

