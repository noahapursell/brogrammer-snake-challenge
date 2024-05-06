import numpy as np
from lib.models.snake_player import SnakePlayer
from lib.models.game_action import GameAction
from lib.models.game_state import GameState
class CLIPlayer(SnakePlayer):
    """Command-line-interface player for the snake game"""

    def __init__(self):
        pass

    def get_action(self, state):
        if state.died:
            print("Game Over")
            return
        user_input = input("Please enter a move (l, r, u, d): ")

        input_to_output = {
            "l": GameAction.LEFT,
            "r": GameAction.RIGHT,
            "u": GameAction.UP,
            "d": GameAction.DOWN
        }

        output = input_to_output[user_input]
        print(f"User entered: {output}")
        return output

    def notify_end_of_game(self, game_state: GameState) -> None:
        print("Game over")
        return

    def notify_win(self):
        print("Game beat!")
        return
