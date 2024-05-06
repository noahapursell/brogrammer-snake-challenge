# brogrammer-snake-challenge
This is a repo to host the snake challenge for the brogrammers


## Installation
It is recommended you fork this repository so you can make custom changes. 

### Installing Libraries
This project was made with *python=3.10*. A `requirements.txt` file has been added to this project. 
To install dependencies, run `pip install -r requirements.txt`. Make sure to do this from 
within your conda environment if you are using one. 

## Project Structure
The primary class is the *SnakeGame* class located in `lib/models/snake_game.py`. This class is responsible for managing 
a game of Snake. It takes in a *player* parameter of type *SnakePlayer* (note - this is an abstract class). *SnakePlayer*s are classes designed to play a game of snake. There is a sample player called *CLIPlayer* which is located in `players/cli_player`. This player allows a user to control the snake via the command-line-interface (cli). However, you could easily make a new *SnakePlayer* that is controlled via some algorithm. 


*SnakeGame* can also take in a optional parameter called display, which should be of type *SnakeGameDisplay* (note - this is an abstract class). An example of a *SnakeGameDisplay* class is *cli_display* located in `lib/models/displays/cli_display`. Feel free to make additional display classes.


