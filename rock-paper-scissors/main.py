import random

choices = ["rock", "paper", "scissors"]
user = input("Choose rock, paper, or scissors: ").lower()

while user not in choices:
    user = input(f"You input {user} is not valid. Please enter rock, paper, or scissors: ").lower()

computer = random.choice(choices)

print(f"user: {user}")
print(f"comp: {computer}")

# if user == comp ==> it's a tie

if computer == user: 
    print("it's a tie!")
elif ((user == "paper" and computer == "scissors") or (user == "rock" and user == "paper") or (user == "scissors" and computer == "rock")):
    print("you lose!")
elif ((user == "paper" and computer == "rock") or (user == "rock" and computer == "scissors") or (user == "scissors" and computer == "paper")):
    print("you win!")
else:
    print("Error!")