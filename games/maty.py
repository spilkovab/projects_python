import random

def spin_row():
    # Define symbols
    symbols = ['🍒', '🍉', '🍋', '🍓', '⭐']
    
    # Define row
    return [random.choice(symbols) for _ in range(3)] # for every iterarion (_) in range(3), pick a random symbol

def print_row(row):
    # Print row
    print('**********************')
    print("   |   ".join(row))
    print('**********************')

def get_payout(row, bet):  
    # Check if all symbols are the same
    if row[0] == row[1] == row[2]:
        # Get payout based on what symbols are in the row
        if row[0] == '🍒':
            return bet*3
        elif row[0] == '🍉':
            return bet*4
        elif row[0] == '🍋':
            return bet*5
        elif row[0] == '🍓':
            return bet*10
        elif row[0] == '⭐':
            return bet*20
    # If the symbols are not the same, return $0
    return 0    

def main():
    # Balance
    balance = 100

    # Print init message
    print('***************************')
    print('Welcome to the Slots (maty)')
    print('Symbols: 🍒 🍉 🍋 🍓 ⭐')
    print('***************************')

    # Check input validity
    while balance > 0:
        # Current balance and user bet input
        print(f'Current balance: ${balance}')
        bet = input('Place your bet amount: ')

        # Check if user input is digit
        if not bet.isdigit():
            print('Please enter a valid number')
            continue
        
        # str-> int
        bet = int(bet)

        # Check if bet < balance
        if bet > balance:
            print('Insufficient funds')
            continue
        # Check if bet > 0
        if bet <= 0:
            print('Bet must be grater than 0')
            continue

        # Substract bet from balance
        balance -= bet
        # Spin row
        row = spin_row()
        print('Spinning...\n')
        # Print row
        print_row(row)
        # Get payout
        payout = get_payout(row,bet)
        # Info message
        if payout > 0:
            print(f'You won ${payout}')
        else:
            print('Sorry you lost this round')

        # Add payout to balance
        balance += payout
        # Check if user wants to play again
        play_again = input('Do you want to spin again? (y/n): ').lower()

        # if 'n', stop the game, everything else, continue game >:)
        if play_again == 'n':
            break

    # End of the game info message
    print('**********************************************')
    print(f'Game over! Your current balance is: {balance}')
    print('**********************************************')

if __name__ == '__main__':
    main()