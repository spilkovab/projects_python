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
        "rps": "rock_paper_scissors.py",
        "maty": "maty.py",
        "bj": "blackjack.py"
    }
    # List available games
    game = input('Available games:\n'
                'Dice rolling (dice)\n'
                'Number guessing (number)\n'
                'Trivia game (trivia)\n'
                'Rock, paper, scissors (rps)\n'
                'Casino slots (maty)\n'
                'Black Jack (bj)\n'
                'Please select a game: ').lower()

    # If user chooses an available game run it, otherwise try again
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
        # Run main function
        main()
        # After the end of the game, let user choose if user wants to play again
        con = input('Choose another game? (y/n): ').lower()

        # User doesn't want to play, disp a goodbye message
        if con == 'n':
            print('Goodbye :(')
            break