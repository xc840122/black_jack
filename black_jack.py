############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.


import random


# from art import logo


def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    # shuffle cards
    random.shuffle(cards)
    # return the first one
    return cards[0]


# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this.
def calculate_score(cards: list):
    """Take a list of cards and return the score calculated from the cards"""
    # Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10)
    # and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    if len(cards) == 1 and sum(cards) == 21:
        return 0
    # Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21,
    # remove the 11 and replace it with a 1. You might need to look up append() and remove().
    elif (11 in cards) and sum(cards) > 21:
        # replace ace(11) by (1)
        cards.remove(11)
        cards.append(1)
        return sum(cards)
    else:
        return sum(cards)

    # Hint 13: Create a function called compare() and pass in the user_score and computer_score.
    # If the computer and user both have the same score, then it's a draw.
    # If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0),
    # then the user wins. If the user_score is over 21, then the user loses.
    # If the computer_score is over 21, then the computer loses. If none of the above,
    # then the player with the highest score wins.


def compare(user_score, computer_score):
    # -1 means lose, 1 means win, 0 means draw, 22 user over, -22, computer over
    if computer_score == 0:
        return -1
    elif user_score == 0:
        return 1
    elif computer_score > 21:
        print("Computer score is over 21, boom! you win")
        return -22
    # if user_score > 21, lose
    elif user_score > 21:
        print("Your score is over 21, boom! you lose")
        return 22
    elif user_score < computer_score:
        return -1
    elif user_score > computer_score:
        return 1
    else:
        # draw
        return 0


def play_game():
    # Hint 5: Deal the user and computer 2 cards each using deal_card()
    user_cards = [deal_card(), deal_card()]
    print(f"your cards: {user_cards[0]}, {user_cards[1]}")
    computer_cards = [deal_card(), deal_card()]
    # Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0)
    # or if the user's score is over 21, then the game ends.
    if calculate_score(user_cards) == 0:
        print("Black jack, you win")
        return None
    elif calculate_score(computer_cards) == 0:
        print("Computer Got Black jack, you lose")
        return None
    # Hint 10: If the game has not ended, ask the user if they want to draw another card.
    while True:
        draw_card = input("do u want to draw another card? (y/n)")
        # If yes, then use the deal_card() function to add another card to the user_cards List.
        # If no, then the game has ended.
        if draw_card == "y":
            user_cards.append(deal_card())
            if calculate_score(user_cards) == 22:
                print("Your score is over 21, boom! you lose")
                break
        elif draw_card == "n":
            break
    # Hint 11: The score will need to be rechecked with every new card drawn
    # and the checks in Hint 9 need to be repeated until the game ends.
    # Hint 12: Once the user is done, it's time to let the computer play.
    # The computer should keep drawing cards as long as it has a score less than 17.
    if sum(computer_cards) < 17:
        computer_cards.append(deal_card())

    result = compare(sum(user_cards), sum(computer_cards))
    if result == -1:
        print("You Lose")
    elif result == 1:
        print("You Win")
    elif result == 0:
        print("Draw")
    elif result == -22:
        print("Computer score is over 21, boom! you win")
    elif result == 22:
        print("Computer score is over 21, boom! you win")
    else:
        print("Woo...problem")


# Hint 14: Ask the user if they want to restart the game. If they answer yes,
# clear the console and start a new game of blackjack and show the logo from art.
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()
