# importing art, random, and clear function
from art import logo
from os import system, name
import random


# clear function to clear the console.
def clear():
    # for windows.
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix').
    else:
        _ = system('clear')
# end of clear function.


# start of the game.
print(logo)
print("Welcome to BlackJack")
start_game = input("Start the game Y or N: ").lower()


# function to calculate the score
def score_counter(cards):
    score = 0
    for card in cards:
        if card == "J" or card == "Q" or card == "K":
            score += 10
        elif card == "A":
            score += 11
        else:
            score += card

    for i in cards:
        if score > 21 and i == "A":
            score -= 10

    return score
# end of score_counter function


# BlackJack game function
def black_jack():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    user_cards = []
    dealer_cards = []

    # drawing the first deck of cards, 2 to the user, 1 for the dealer
    user_cards.append(random.choice(cards))
    user_cards.append(random.choice(cards))
    dealer_cards.append(random.choice(cards))

    print(f"Your cards: {user_cards}, your score: {score_counter(user_cards)}")
    print(f"Dealer's first card: {dealer_cards}")

    draw_card = input("Another card Y or N: ").lower()

    is_pass = False
    while not is_pass:
        if draw_card == "y":
            user_cards.append(random.choice(cards))
            print("-------------------------------------")
            print(f"Your cards: {user_cards}, your score: {score_counter(user_cards)}")
            print(f"Dealer's first card: {dealer_cards}")
            print("-------------------------------------")
            if score_counter(user_cards) > 21:
                is_pass = True
                while score_counter(dealer_cards) < 17:
                    dealer_cards.append(random.choice(cards))
            else:
                draw_card = input("Another card Y or N: ").lower()
        else:
            is_pass = True
            while score_counter(dealer_cards) < 17:
                dealer_cards.append(random.choice(cards))

    print(f"Your hand: {user_cards}, score: {score_counter(user_cards)}")
    print(f"dealer hand: {dealer_cards}, score: {score_counter(dealer_cards)}")

    if score_counter(user_cards) > 21:
        print("You went over, You lost.")
    elif score_counter(user_cards) <= 21 and score_counter(dealer_cards) > 21:
        print("Dealer went over, You won.")
    elif score_counter(user_cards) <= 21 and score_counter(user_cards) > score_counter(dealer_cards):
        print("You WON!!!")
    elif score_counter(user_cards) <= 21 and score_counter(user_cards) < score_counter(dealer_cards):
        print("You LOST!!!")
    elif score_counter(user_cards) == score_counter(dealer_cards):
        print("You draw.")

    start_game = input("Start the game Y or N: ").lower()
    if start_game == "y":
        clear()
        print(logo)
        black_jack()
    else:
        clear()
        print("You exit the game, GoodBye.")


# Checking the if the user want to play or not
if start_game == "y":
    black_jack()
else:
    print("You exit the game, GoodBye.")