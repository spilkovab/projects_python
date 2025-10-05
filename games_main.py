from games import *
import os
import subprocess

# Folder where the game scripts are stored
GAMES_DIR = os.path.join(os.path.dirname(__file__), "games")

def main():
    # Map short names to actual filenames
    games = {
        "dice": "dice_rolling.py",
        "number": "number_guessing.py",
        "trivia": "trivia_game.py",
        "rps": "rock_paper_scissors.py"
    }

    game = input('Available games:\n'
                'Dice rolling (dice)\n'
                'Number guessing (number)\n'
                'Trivia game (trivia)\n'
                'Rock, paper, scissors (rps)\n'
                'Please select a game: ').lower()

    if game in games:
        game_path = os.path.join(GAMES_DIR,games[game])
        if os.path.exists(game_path):
            # run game
            subprocess.run(["python", game_path])
        else:
            print(f'Game not found: {game_path}')
    else:
        print('Invalid selection, please try again.')

if __name__ == '__main__':
    while True:
        main()
        con = input('Choose another game? (y/n): ').lower()

        if con == 'n':
            break