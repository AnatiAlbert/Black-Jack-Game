# black jack game

############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt
import random
from art_blackjack import logo
#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    '''Return a random card from the deck.'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(list_cards):
    '''Take a list of cards and return the score calculated from the cards'''
    score = sum(list_cards)
    if score == 21 and len(list_cards) == 2:
        return 0
    if 11 in list_cards and score > 21:
        list_cards.remove(11)
        list_cards.append(1)
    return score

def compare(user_score, computer_score):
    if computer_score == user_score:
        return 'Draw!'
    elif computer_score == 0:
        return 'Lost, opponent has Blackjack!'
    elif user_score == 0:
        return 'Won, with a Blackjack!'
    elif user_score > 21:
        return 'You went over, you lost!'
    elif computer_score > 21:
        return 'Opponent went over, You win!'
    elif user_score > computer_score:
        return 'You win!'
    else:
        return 'You lose'

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
def playgame():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())


    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f' Your cards: {user_cards}, current score: {user_score}')
        print(f" Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            draw_card = input('Type "y" to get another card or "n" to pass? ')
            if draw_card == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

        while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)

        print(f' Your final hand: {user_cards} and final score {user_score}')
        print(f" Computer's final hand: {computer_cards} and final score {computer_score}")
        print(compare(user_score, computer_score))


while input('Do you want to play a game of Blackjack? Type "y" or "n": ') == "y":
    playgame()

