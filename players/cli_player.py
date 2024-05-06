import numpy as np
from lib.models.snake_player import SnakePlayer

class CLIPlayer(SnakePlayer):
    """Command-line-interface player for the snake game"""

    def __init__(self):
        pass

    def get_action(self, state):
        user_input = input("Please enter a move (l, r, u, d): ")

        input_to_output = {
                "u": np.array([1, 0, 0, 0]),
                "r": np.array([0, 1, 0, 0]),
                "d": np.array([0, 0, 1, 0]),
                "l": np.array([0, 0, 0, 1])
        }

        output = input_to_output[user_input]
        print(f"User entered: {output}")
        return output
