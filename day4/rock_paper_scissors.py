import random

rock = {
    'value': 0,
    'text': """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    """
}

paper = {
    'value': 1,
    'text': """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
    """
}

scissors = {
    'value': 2,
    'text': """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    """
}

choices = [rock, paper, scissors]

def get_winner(choice1, choice2):
    if choice1['value'] == choice2['value']:
        return -1
    elif choice1['value'] == 0:
        if choice2['value'] == 1:
            return 1
        elif choice2['value'] == 2:
            return 0
    elif choice1['value'] == 1:
        if choice2['value'] == 0:
            return 0
        elif choice2['value'] == 2:
            return 1
    elif choice1['value'] == 2:
        if choice2['value'] == 0:
            return 1
        elif choice2['value'] == 1:
            return 0
    else:
        print("There was an invalid choice, no winner")
        return -1

input = input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: ")
player_1_choice = list(filter(lambda choice: choice['value'] == int(input), choices))[0]
player_2_choice = random.choice(choices)

print(player_1_choice['text'] + "\n")
print("Computer chose:\n")
print(player_2_choice['text'] + "\n")

outcome = get_winner(player_1_choice, player_2_choice)

if outcome == 0:
    print("Player 1 wins!")
elif outcome == -1:
    print("It's a tie!")
elif outcome == 1:
    print("Player 2 wins!")
else:
    print("Something horrible has happened")
