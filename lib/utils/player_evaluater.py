import time
import json
from typing import Tuple

from lib.models.snake_game import SnakeGame
from lib.models.snake_player import SnakePlayer

class PlayerEvaluater:
    """A class to evaluate the performance of a snake player"""

    def __init__(self, player: SnakePlayer):
        """
        params:
            player: Snake Player
                the player to be evaluated
        """

        self.player = player
        self.player_name = player.__class__
        self.game_size = (12, 12)
        self.time_history = {}

    
    def evaluate_player(self, num_trials:int = 5, board_size=(12, 12), output_file:str | None =None, verbose:bool = False):
        """Perform various tests on the player to evaluate it"""
        if verbose: 
            print(f"Starting evaluation of {self.player_name}")

        trial_data = []

        for trial_number in range(num_trials):
            if verbose:
                print(f"Starting trial {trial_number}")
            trial_statistics = self.run_trial(board_size)
            trial_data.append(trial_statistics)
            if verbose:
                print(f"Trial {trial_number} finished.")

        if output_file is not None:
            with open(output_file, 'w') as file:
                json.dump(trial_data, file)

    def run_trial(self, board_size: Tuple[int, int]):
        """Run a trial on the model, record the following statistics:
            time for each frame,
            number of frames,
            total time
            wether it was a win or not
        """
        num_frames = 0
        frame_times = []
        total_time = 0
        is_win = False

        snake_game = SnakeGame(self.player, board_size)
        while not snake_game.died:
            initial_time = time.time()
            snake_game.step()
            final_time = time.time()

            frame_time = final_time - initial_time
            frame_times.append(frame_time)
            total_time += frame_time
            num_frames += 1

        if snake_game.won:
            is_win = True

        return {
                "num_frames": num_frames,
                "frame_times": frame_times,
                "total_time": total_time,
                "is_win": is_win
        }
