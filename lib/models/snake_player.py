from abc import ABC, abstractmethod
from lib.models.game_state import GameState
from lib.models.game_action import GameAction

class SnakePlayer(ABC):
    """
        Abstract class / interface to represent a player for
        the snake game
    """

    @abstractmethod
    def get_action(self, game_state: GameState) -> GameAction:
        """Based on the game state, perform an action. The action should be returned"""
        pass

    @abstractmethod
    def notify_end_of_game(self, game_state: GameState) -> None:
        """Notify the player that the game is over"""
        pass

    @abstractmethod
    def notify_win(self):
        """Notify the player that they won"""
        pass
