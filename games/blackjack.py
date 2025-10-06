from dataclasses import dataclass
import random
import time

# karty class
# def body
# def barvy
# vytvorit balicek
# rozdat karty (2) pro user a pro krupier, spocitat body
# raise bets
# ask user:
# -- HIT: pridat kartu update body
# -- STAND: hraje krupier (bodu>=17 nepridavat, body < 17 HIT)
# -- DOUBLE: Double bet, add card and end the game
# -- SPLIT (pouze pokud hrac ma 2 stejne karty, pak hraje hru zvast s kazdou casti, double the bet, kartu pridat ke kazdemu balicku)
# check winner (user == 21 - user wins 3:2 (1.5*bet),
#               user==krupier - tie,
#               user>krupier - user wins, 
#               user<=krupier - user lost,
#               user>21 - busted,
#               krupier>21 - user wins 1:1 if not busted)

@dataclass
class Card:
    name: str
    color: str
    points: int
    emoji: str

values = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
    "7": 7, "8": 8, "9": 9, "10": 10,
    "J": 10, "Q": 10, "K": 10, "A": 11  # eso = 11 (may be 1)
}

colors = {
    "srdce": "♥️",
    "káry": "♦️",
    "piky": "♠️",
    "kříže": "♣️"
}

deck = [
    Card(value, color, points, emoji)
    for value, points in values.items()
    for color, emoji in colors.items()
]

random.shuffle(deck)

def count_points(hand):
    points = sum(card.points for card in hand)

    aces = sum(1 for card in hand if card.name=='A')
    while points > 21 and aces:
        points-=10
        aces -=1
    return points

def reveal_hand(hand, who):
    cards_next = " ".join(f'{k.name}{k.emoji}' for k in hand)
    print(f'{who}: {cards_next}  (points: {count_points(hand)})')

def decide_winner(user_points, dealer_points,balance,user_bet):
    if user_points>21:
        print('💥BUSTED💥')
        print(f'Current balance ${balance}')
    elif dealer_points>21:
        print('❗Dealer busted❗')
        balance += user_bet*2
        print(f'You won ${user_bet*2}. Current balance: ${balance}')
    elif user_points>dealer_points:
        if user_points==21:
            print('💥💥💥BlackJack💥💥💥')
            balance += user_bet*2.5
            print(f'You won ${user_bet*2.5}. Current balance: ${balance}')
        else:
            print('⭐You win⭐')
            balance += user_bet*2
            print(f'You won ${user_bet*2}. Current balance: ${balance}')
    elif user_points==dealer_points:
        print('😮 Its\'s a tie 😮')
        balance += user_bet
        print(f'You won ${user_bet}. Current balance: ${balance}')
    elif dealer_points>user_points:
        print('☹️ You lost ☹️')
        print(f'Current balance ${balance}')

    return balance

def main(deck):
    balance = 100
    dealer_points = 0

    # Info string
    print('************************************')
    print('        WELCOME TO BLACKJACK        ')
    print('************************************')
    print()
    
    while balance>0:
        flag_end_game = False
        # User bet
        user_bet = input(f'What\'s your bet (available funds: {balance})? BET: $')
        # Bet input validity check
        if not user_bet.isdigit():
            print('Bet must be a number, try again...')
            continue
        # str -> int
        user_bet = int (user_bet)
        # Bet validity
        if user_bet>balance:
            print(f'Insufficient funds! Available funds: ${balance}')
            continue
        elif user_bet<=0:
            print('Bet must be more than $0')
            continue
        # Substract bet from balance
        balance -= user_bet        

        # GAME START
        user = [deck.pop(), deck.pop()]
        dealer = [deck.pop(), deck.pop()]

        user_turn = True

        reveal_hand(user, "User")
        print(f'Dealer: {dealer[0].name}{dealer[0].emoji} [Hidden card]')

        while user_turn:
            user_move = input('What is your next move? HIT (h) / STAND (s) / DOUBLE (d): ').lower()

            if user_move=='h':
                user.append(deck.pop())
                reveal_hand(user, "User")

                user_points = count_points(user)
                if user_points>=21:
                    balance = decide_winner(user_points,dealer_points,balance,user_bet)
                    flag_end_game = True
                    break

            elif user_move == 's':
                # dealer turn
                print('Dealer turn', end='', flush=True)
                for _ in range(6):
                    time.sleep(0.25)
                    print('.',end='',flush=True)
                print()
                user_turn = False
                break

            elif user_move=='d':
                # double bet
                balance -= user_bet
                user_bet = user_bet*2
                # add card
                user.append(deck.pop())
                reveal_hand(user,"User")

                # dealer turn
                user_turn = False
                print(f'Current bet: ${user_bet}')
                print('Dealer turn', end='', flush=True)
                for _ in range(6):
                    time.sleep(0.25)
                    print('.',end='',flush=True)
                print()

                break
        # Dealer turn
        while count_points(dealer) < 17:
            dealer.append(deck.pop())
        # Count points
        user_points = count_points(user)
        dealer_points = count_points(dealer)
        reveal_hand(dealer, "Dealer")
        if not flag_end_game:
            # Decide winner
            balance = decide_winner(user_points,dealer_points,balance,user_bet)

        if balance<=0:
            print('You are out of money! Bye :(')
            break

        round = input('Another round? (y/n): ')
        if round == 'y':
            continue
        if round == 'n':
            print('****************************************')
            print(f'Good game! Your final balance is ${balance}')
            print('****************************************')
            break


if __name__=='__main__':
    main(deck)