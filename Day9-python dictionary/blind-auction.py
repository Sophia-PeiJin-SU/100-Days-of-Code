from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)

bid_dict = {}
keep_bidding = True

def find_winner(bid_dict):
  num = 0
  winner = ""

  for person in bid_dict:
    if int(bid_dict[person]) > num:
      num = int(bid_dict[person])
      winner = person
  print(f"Winner is {winner} with the highest bid of ${num}!")
  

while keep_bidding:
  name = input("What is your name? ")
  bid = input("What is your bid? $")
  bid_dict[name] = bid
  print(bid_dict)
  answer = input("Are there other bidders? Yes or No\n").lower()

  if answer == "yes":
    clear()
  elif answer == "no":
    find_winner(bid_dict)
    keep_bidding = False
