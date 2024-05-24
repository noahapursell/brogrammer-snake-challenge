from lib.models.snake_game_display import SnakeGameDisplay
from lib.models.game_state import GameState
class CLIDisplay(SnakeGameDisplay):

    def __init__(self):
        pass

    def render(self, game_state: GameState):
        print(game_state.board)
        return

    def render_end_of_game(self, game_state: GameState):
        print(game_state.board)
        print("Game OVER")
        return
