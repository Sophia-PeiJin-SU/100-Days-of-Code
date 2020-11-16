import random
from replit import clear
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
  random_card = random.choice(cards)
  return random_card

def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  elif sum(cards) > 21:
    if 11 in cards:
      cards.remove(11)
      cards.append(1)
    return sum(cards)    
  else:
    return sum(cards)

def compare(user_score, computer_score):
  if user_score == computer_score:
    return "It's a draw."
  elif user_score == 0:
    return "You have Blackjack! YOU WIN!!!"
  elif computer_score == 0:
    return "Computer has Blackjack! You lose..."    
  elif user_score > 21:
    return "You went too far, you lose!"
  elif computer_score > 21:
    return "Computer went too far, you win!"
  elif user_score < computer_score:
    return "You lose..."
  elif user_score > computer_score:
    return "You win!"

def new_game():
  print(logo)
  user_cards = []
  computer_cards = []
  game = True

  for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while game:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"  Your cards: {user_cards}, current score: {user_score}")
    print(f"  Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      game = False
    else:
      draw_card = input("Do you wnat another card? 'Y' or 'N'? ").lower()
      if draw_card == "y":
        user_cards.append(deal_card())
      else:      
        game = False

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"  Your final result: {user_cards}, final score: {user_score}")
  print(f"  Computer's final result: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))
  
while input("Do you want to play Blackjack game? 'Y' or 'N'? ").lower() == "y":
  clear()
  new_game()


