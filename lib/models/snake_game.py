from typing import Tuple
import pandas as pd
import numpy as np
from lib.models.snake_player import SnakePlayer
from lib.models.game_state import GameState
from lib.models.point import Point
import time


class SnakeGame:
    """
        A class to manage a snake game
    """

    EMPTY_SQUARE = 0
    APPLE_SQUARE = -1

    def __init__(self, player: SnakePlayer, size: Tuple[int, int] = (12, 12), display=None, time_delay=0):
        self.map_width = size[0]
        self.map_height = size[1]
        self.game_board = np.full(
            (self.map_width, self.map_height), SnakeGame.EMPTY_SQUARE, dtype=int)
        self.snake_size = 5  # Initialize snake size
        self.snake_pos = Point(x=self.map_width // 2, y=self.map_height // 2)
        self.game_board[self.snake_pos.y, self.snake_pos.x] = self.snake_size
        self.player = player
        self.died = False  # Set to true when the player dies
        self.won = False
        apple_pos = self.get_random_apple_location()
        self.game_board[apple_pos.y, apple_pos.x] = SnakeGame.APPLE_SQUARE
        self.display = display
        self.time_delay = time_delay

    def step(self):
        game_state = GameState(
            self.game_board, self.snake_pos, self.snake_size, self.died)
        if self.died:  # If the game is over, notify player, but then do nothing
            if self.display:
                self.display.render_end_of_game(game_state)
            return
        if self.display:
            self.display.render(game_state)
        time.sleep(self.time_delay)

        player_action = self.player.get_action(game_state)
        self.snake_pos += player_action.value

        if self.is_out_of_bounds():
            self.died = True
        elif self.is_crashing_into_self():
            self.died = True
        elif self.is_eating_apple():
            self.snake_size += 1
            self.game_board[self.snake_pos.y,
                            self.snake_pos.x] = self.snake_size
            apple_pos = self.get_random_apple_location()
            if apple_pos.x == -1 and apple_pos.y == -1:
                self.player.notify_win()
                self.won = True
                self.died = True
                return
            self.game_board[apple_pos.y, apple_pos.x] = SnakeGame.APPLE_SQUARE
            return

        if self.died:  # If the game is over, notify player, but then do nothing
            if self.display:
                self.display.render_end_of_game(game_state)
            game_state = GameState(
                self.game_board, self.snake_pos, self.snake_size, self.died)
            self.player.notify_end_of_game(game_state)
            return

        self.game_board[self.snake_pos.y,
                        self.snake_pos.x] = self.snake_size + 1
        self.game_board[self.game_board > 0] -= 1

    def is_out_of_bounds(self):
        if self.snake_pos.x < 0 or self.snake_pos.y < 0:
            return True
        if self.snake_pos.x >= self.map_width or self.snake_pos.y >= self.map_height:
            return True
        return False

    def is_crashing_into_self(self):
        if self.game_board[self.snake_pos.y, self.snake_pos.x] > 1:
            return True
        return False

    def is_eating_apple(self):
        if self.game_board[self.snake_pos.y, self.snake_pos.x] == SnakeGame.APPLE_SQUARE:
            return True
        return False

    def get_random_apple_location(self):
        zero_indicies = np.where(self.game_board == 0)
        zero_positions = list(zip(zero_indicies[0], zero_indicies[1]))
        if zero_positions:
            selected_position = zero_positions[np.random.choice(
                len(zero_positions))]
            return Point(x=selected_position[1], y=selected_position[0])
        else:
            return Point(-1, -1)
