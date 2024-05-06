import numpy as np
import pygame as pg

from lib.models.snake_player import SnakePlayer
from lib.models.game_action import GameAction
from lib.models.game_state import GameState


class WASDPlayer(SnakePlayer):
    """Play with wasd keys"""

    def __init__(self):
        pg.init()
        self.prev_move = GameAction.UP

    def get_action(self, state: GameState) -> GameAction:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_w:
                    self.prev_move = GameAction.UP
                elif event.key == pg.K_a:
                    self.prev_move = GameAction.LEFT
                elif event.key == pg.K_s:
                    self.prev_move = GameAction.DOWN
                elif event.key == pg.K_d:
                    self.prev_move = GameAction.RIGHT
        return self.prev_move

    def notify_end_of_game(self, game_state: GameState) -> None:
        print("Game over")
        return

    def notify_win(self):
        print("Game beat!")
        return
