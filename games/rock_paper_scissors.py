import random

# Choices
rock = 'r'
paper = 'p'
scissors = 's'

emojis = {
    rock: '🪨', 
    paper: '📃',
    scissors: '✂️'
}
valid_choices = tuple(emojis.keys()) # tuple = read only

def get_user_choice():
    while True:
        # User choice
        user_choice = input('Rock, paper, scissors? (r/p/s): ').lower()
        # Validity check
        if user_choice in valid_choices:
            return user_choice
        else:
            print('Not a valid choice')

def display_choices(user_choice,computer_choice):
    # print choices
    print(f'You chose {emojis[user_choice]}')
    print(f'Computer chose: {emojis[computer_choice]}')

def determine_win(user_choice,computer_choice):
    # Decision
    if user_choice == computer_choice:
        print('TIE')
    elif (
        (user_choice == rock and computer_choice == scissors) or 
        (user_choice == paper and computer_choice == rock) or 
        (user_choice == scissors and computer_choice == paper)):
        print('YOU WIN!')
    else:
        print('YOU LOST!')

def play_game():
    while True:
        # Get user choice
        user_choice = get_user_choice()

        # PC choice
        computer_choice = random.choice(valid_choices)

        display_choices(user_choice,computer_choice)
        determine_win(user_choice,computer_choice)

        con = input('Continue? (y/n): ')
        if con == 'n':
            break

if __name__ == '__main__':
    play_game()