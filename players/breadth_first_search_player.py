import numpy as np
from queue import Queue
import copy
from typing import Tuple

from lib.models.snake_player import SnakePlayer
from lib.models.game_state import GameState
from lib.models.game_action import GameAction
from lib.models.snake_game import SnakeGame
from lib.models.point import Point

class BreadthFirstSearch(SnakePlayer):
    """A class that plays snake via a bfs algorithm"""

    def __init__(self):
        pass

    def get_action(self, game_state: GameState) -> GameAction:
        board_state = game_state.board
        target_position = np.where(board_state == SnakeGame.APPLE_SQUARE)
        # States will be storeed as tuples: (board state, head_pos) where head pos is (x, y)
        head_pos = (game_state.head_pos.x, game_state.head_pos.y)
        state_queue = Queue()
        state_queue.put((copy.deepcopy(board_state), head_pos, None))

        found_solution = False
        while not found_solution:
            if state_queue.empty():
                break

            current_state = state_queue.get()
            head_pos = current_state[1]
            board_state = current_state[0]

            # For all possible moves, see if the move is legal. If it is, make the move and add the new state to the queue
            possible_moves = [(1, 0, GameAction.RIGHT), (-1, 0, GameAction.LEFT), (0, 1, GameAction.DOWN), (0, -1, GameAction.UP)]

            for move in possible_moves:
                new_head_pos = (head_pos[0] + move[0], head_pos[1] + move[1])
                if not self.is_legal_move(board_state, new_head_pos):
                    continue
                if self.found_apple(board_state, new_head_pos): 
                    if self.is_safe_move(board_state, new_head_pos):
                            
                        if current_state[2] is not None:
                            return current_state[2]
                        else:
                            return move[2]
                    else:
                        print("NOT SAFE")
                        continue
                
                next_state = self.get_next_state(board_state, new_head_pos, current_state[2], move[2])
                state_queue.put(next_state)
        return GameAction.UP

    def get_next_state(self, board_state, new_head_pos, prev_first_action, current_action):
        head_value = np.max(board_state)
        new_board_state = copy.deepcopy(board_state)
        new_board_state[new_board_state > 1] -= 1
        new_board_state[new_head_pos[1], new_head_pos[0]] = head_value
        if prev_first_action is None:
            #print("First action is none!!")
            #print(f"Current Action: {current_action}")
            prev_first_action = current_action
        return (new_board_state, new_head_pos, prev_first_action) 

    def found_apple(self, board, head_pos):
        """Return true if the apple is in the same spot as the head pos"""
        apple_square = np.where(board == SnakeGame.APPLE_SQUARE)
        #print(f"AS: {apple_square}, HP: {head_pos}")
        # print(f"apple square: {apple_square}")
        # print(board)
        apple_x = apple_square[0][0]
        apple_y = apple_square[1][0]
        if head_pos[1] == apple_x and head_pos[0] == apple_y:
            #print(f"FOUND ONE!!!!!! - head: {head_pos}, apple: {apple_square}")
            pass 
        return board[head_pos[1], head_pos[0]] == SnakeGame.APPLE_SQUARE 

    def is_safe_move(self, board, head_pos):
        """Return true if the board is fully connected"""
        # TODO
        number_of_empty_nodes = np.count_nonzero(board == 0)
        x, y = self.find_random_starting_node(board)
        
        to_see_queue = Queue()
        is_head_found = False
        visited = []
        to_see_queue.put(Point(x, y))
        while not to_see_queue.empty():
            current_node = to_see_queue.get()

            if current_node == Point(head_pos[0], head_pos[1]):
                is_head_found = True
                continue
            if current_node in visited:
                continue
            if board[current_node.y, current_node.x] != 0:
                continue
            visited.append(current_node)
            to_search = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            for place in to_search:
                next_node = current_node + Point(place[0], place[1])
                if next_node.x < 0 or  next_node.y < 0:
                    continue
                if next_node.x >= board.shape[1] or next_node.y >= board.shape[0]:
                    continue
                to_see_queue.put(next_node)

        if len(visited) == number_of_empty_nodes and is_head_found:
            return True
        else:

            print(f"Visited: {len(visited)}, To see: {number_of_empty_nodes}")
            return False
            
        
        print(board)
        return True

    def find_random_starting_node(self, board) -> Tuple[int, int]:
        max_x = board.shape[1]
        max_y = board.shape[0]

        for x in range(max_x):
            for y in range(max_y):
                if board[y, x] == 0:
                    return (x, y)
        return (-1, -1)

    def is_legal_move(self, board_state, new_head_pos):
        """board state should be 2d numpy array. new_head_pos is tuple (x, y)"""
        # Ensure new head is not out of bounds
        width = board_state.shape[1]
        height = board_state.shape[0]
        if new_head_pos[0] < 0 or new_head_pos[0] > width - 1 or new_head_pos[1] < 0 or new_head_pos[1] > height - 1:
            return False
        # Ensure new head does not collid with self
        if board_state[new_head_pos[1], new_head_pos[0]] > 1:
            return False

        return True # Return true if all tests pass

        
        return GameAction.UP
    def notify_end_of_game(self, game_state: GameState) -> None:
        #print("Game Over")
        print('l')
    def notify_win(self):
        print("You win")
