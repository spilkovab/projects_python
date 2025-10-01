import random

num = random.randint(1,100)
win = False

for i in range(5):
    guess = int(input(f'Guess the number between 1-100, you have {5-i} guesses: '))
    if guess is int:
        ('Not a number!!!')
        break
    elif guess == num:
        print('Congrats! You won!')
        win = True
        break
    elif guess > num:
        print('Lower...')
    elif guess < num:
        print('Higher...')

if win != True:
    print(f'You lost! The number was {num}.')