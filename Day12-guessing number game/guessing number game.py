import random
import art
print(art.logo)

def guess(number):
  if number > answer:
    return "Too high, try again"
  elif number < answer:
    return "Too low, try again"
  else:
    return "You win"

def difficulity(level):
  if level == "hard":
    return 5
  else:
    return 10

answer = random.randint(1,100)
level = input("Choose a level, hard or easy? ").lower()
life = difficulity(level)
game = True

while game:
  guess_num = int(input("Select a number "))
  result = guess(guess_num)
  life -= 1
  print(f"{result}, you still have {life} life")

  if life == 0:
    print("You lose...")
    game = False
  elif result == "You win":
    game = False



