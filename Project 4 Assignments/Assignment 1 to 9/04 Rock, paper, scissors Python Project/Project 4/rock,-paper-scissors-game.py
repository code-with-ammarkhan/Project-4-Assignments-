import random

def play():
    print("Rock, Paper, Scissors Game!")
    user = input("Choose rock, paper or scissors: ").lower()
    options = ["rock", "paper", "scissors"]
    
    if user not in options:
        return "Invalid input. Please choose rock, paper, or scissors."
    
    computer = random.choice(options)
    print(f"Computer chose: {computer}")

    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

# Run the game
result = play()
print(result)
