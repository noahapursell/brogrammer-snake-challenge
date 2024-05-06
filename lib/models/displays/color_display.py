from lib.models.snake_game_display import SnakeGameDisplay
from lib.models.game_state import GameState

import numpy as np
import pygame as pg
import time


class ColorDisplay(SnakeGameDisplay):

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((800, 800))

    def render(self, game_state: GameState):
        # Fill the screen with black before redrawing
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return
        self.screen.fill(pg.Color('black'))
        self.draw_array(game_state.board)
        pg.display.flip()

    def render_end_of_game(self, game_state: GameState):

        font = pg.font.Font(None, 36)
        text = font.render("Game Over", True, pg.Color('white'))
        text_rect = text.get_rect(center=(400, 400))
        self.screen.blit(text, text_rect)
        pg.display.flip()
        time.sleep(5)
        pg.quit()

    def map_color(self, value, max_value):
        if value == 0:
            return pg.Color('black')
        elif value == -1:
            return pg.Color('red')
        else:
            intensity = int(255 * value / max_value)
            return pg.Color(0, intensity, 0)

    def draw_array(self, arr):
        cell_width = 800 // arr.shape[0]
        cell_height = 800 // arr.shape[1]
        for y in range(arr.shape[0]):
            for x in range(arr.shape[1]):
                color = self.map_color(arr[y, x], arr.max())
                pg.draw.rect(self.screen, color, pg.Rect(
                    x * cell_width, y * cell_height, cell_width, cell_height))
                if 1 <= arr[y, x] <= arr.max():
                    pg.draw.rect(self.screen, pg.Color('green'), pg.Rect(
                        x * cell_width, y * cell_height, cell_width, cell_height), 1)
                else:
                    pg.draw.rect(self.screen, pg.Color('gray'), pg.Rect(
                        x * cell_width, y * cell_height, cell_width, cell_height), 1)
