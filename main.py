from lib.models.snake_game import SnakeGame
from players.cli_player import CLIPlayer

if __name__ == "__main__":
    print("Main program starting")
    snake_player = CLIPlayer()
    snake_game = SnakeGame(snake_player)
    print(snake_game.game_board)

    for _ in range(10):
        snake_game.step()
        print(snake_game.game_board)
