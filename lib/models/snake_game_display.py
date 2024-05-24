from abc import ABC, abstractmethod
import numpy as np
from lib.models.game_state import GameState

class SnakeGameDisplay(ABC):
    """A class to manage the displaying of a snakegame"""

    @abstractmethod
    def render(self, game_state: GameState):
        pass

    @abstractmethod
    def render_end_of_game(self, game_state: GameState):
        pass
