from lib.models.snake_game import SnakeGame
from players.cli_player import CLIPlayer
from lib.models.displays.cli_display import CLIDisplay

if __name__ == "__main__":
    print("Main program starting")
    snake_player = CLIPlayer()
    snake_display = CLIDisplay()
    snake_game = SnakeGame(snake_player, display=snake_display, size=(3, 3))

    while not snake_game.died:
        snake_game.step()
