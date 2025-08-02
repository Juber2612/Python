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
import random
game_choice=[rock,paper,scissors]

user_choice=int(input("what do you choose? Type 0 for Rock,1 for paper,2 for Scissors : "))
if user_choice>=0 and user_choice<=2:
    print(game_choice[user_choice])
choice=random.randint(0,2)
print("computer choice: ")
print(game_choice[choice])
if user_choice>=3 or user_choice<0:
    print("You typed invalid number")
elif user_choice==0 and choice==2:
    print("You win")
elif choice==0 and choice==2:
    print("You lose!")
elif choice > user_choice:
    print("You lose!")
elif user_choice > choice:
    print("You win")
elif choice == user_choice:
    print("it is draw")
else:
    print("you typed invalid number")