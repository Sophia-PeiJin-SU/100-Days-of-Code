import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

image = [rock, paper, scissors]
choice = int(input("What do you choose? 0 for rock, 1 for paper, 2 for scissors.\n"))
if choice < 3:
  print(image[choice])
else:
  print("Invalid input, you lose!")
# if choice == 0:
#   print(rock)
# elif choice == 1:
#   print(paper)
# elif choice == 2:
#   print(scissors)
# else:
#   print("Invalid number, you lose!")

choice_computer = random.randint(0,2)
# if choice < 3:
#   print("Computer chose: ")
#   if choice_computer == 0:
#     print(rock)
#   elif choice_computer == 1:
#     print(paper)
#   else:
#     print(scissors)

if choice < 3:
  print(image[choice_computer])
  if choice == choice_computer:
    print("It's a tie.")
  elif (choice == 0 and choice_computer == 1) or (choice == 1 and choice_computer == 2) or (choice == 2 and choice_computer == 0):
    print("You lose!")
  else:
    print("You win!")
