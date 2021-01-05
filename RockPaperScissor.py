import random
print("Welcome to the Game.\nLet's play!!!")
player=int(input("What do u choose?\nType 0 for Rock, 1 for Paper, 2 for Scissor.\n"))
comp=random.randint(0,2)
l=["Rock", "Paper", "Scissor"]
h=["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""", """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""", """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]
print(f'You choose: {l[player]}.\n{h[player]}')
print(f'Computer choose: {l[comp]}.\n{h[comp]}')
if 0 <= player < 3:
    if player==comp:
        print("Tie")
    elif player==0 and comp==1 or player==1 and comp==2 or player==2 and comp==0:
        print(f"You Lose.\n{l[comp]} beats {l[player]}")
    elif comp==0 and player==1 or comp==1 and player==2 or comp==2 and player==0:
        print(f"You win.\n{l[player]} beats {l[comp]}")
else:
    print("Please enter a valid choice")


