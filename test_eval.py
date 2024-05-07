from lib.utils.player_evaluater import PlayerEvaluater
from players.breadth_first_search_player import BreadthFirstSearch


player = BreadthFirstSearch()
output = "test_output.json"
game_size = (5, 5)
num_trials = 5

player_evaluater = PlayerEvaluater(player)

player_evaluater.evaluate_player(num_trials=num_trials, board_size=game_size, output_file=output, verbose=True)
