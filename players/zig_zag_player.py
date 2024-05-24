from lib.models.snake_player import SnakePlayer
from lib.models.game_state import GameState
from lib.models.game_action import GameAction

class ZigZagPlayer(SnakePlayer):
    def __init__(self):
        self.needs_to_go_to_top_left = True
        pass

    def get_action(self, game_state: GameState) -> GameAction:
        #TODO


        board = game_state.board
        board_dimensions = board.shape
        if board_dimensions[0] != board_dimensions[1]:
            print(board_dimensions)
            print("Dimensions not equal")
            return NotImplemented
        if board_dimensions[0] % 2 != 0:
            print(board_dimensions)
            print("Dimensions not even")
            return NotImplemented

        if game_state.head_pos.x == 0 and game_state.head_pos.y == 0:
            self.needs_to_go_to_top_left = False
        if self.needs_to_go_to_top_left:
            return self.move_needed_to_get_to_top_left(game_state)
        
        # If the head is at the bottom row, but not the bottom left, go left
        if game_state.head_pos.y == board_dimensions[0] - 1 and game_state.head_pos.x > 0:
            return GameAction.LEFT
        # If the head is on the left most col, and not the top row, go up
        if game_state.head_pos.x == 0 and game_state.head_pos.y > 0:
            return GameAction.UP
        # If the head is in the top left, go right
        if game_state.head_pos.x == 0 and game_state.head_pos.y == 0:
            return GameAction.RIGHT
        # If the head is at the far right column on an even row, go down
        if game_state.head_pos.x == board_dimensions[1] - 1 and game_state.head_pos.y % 2 == 0:
            return GameAction.DOWN
        # If the head is at the second from left column, and on odd row, go down
        if game_state.head_pos.x == 1 and game_state.head_pos.y % 2 == 1:
            return GameAction.DOWN
        # Otherwise, if head is on even row, go right
        if game_state.head_pos.y % 2 == 0:
            return GameAction.RIGHT
        # If head is on odd row, go left
        if game_state.head_pos.y % 2 != 0:
            return GameAction.LEFT
        
        return GameAction.DOWN

    def move_needed_to_get_to_top_left(self, game_state: GameState) -> GameAction:
        head_pos = game_state.head_pos
        if head_pos.x > 0:
            return GameAction.LEFT
        else:
            return GameAction.UP

        

    def notify_end_of_game(self, game_state: GameState) -> None:
        print("Game over! ZigZagL")

    def notify_win(self):
        print("Thats too easy")
