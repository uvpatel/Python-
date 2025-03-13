from random import randint

choices = ["rock", "paper", "scissors"]
# Create a dictionary to map choices to their corresponding values
choice_dict = {"rock": 0, "paper": 1, "scissors": -1}

# Generate a random choice for the computer
computer_choice = choices[randint(0, 2)]

# Get user input and convert it to the corresponding value
user_input = input("Enter your choice (rock, paper, scissors): ").lower()
if user_input in choice_dict:
    user_choice = choice_dict[user_input]
else:
    print("Invalid choice. Please choose rock, paper, or scissors.")
    exit()

# Compare choices
if user_choice == choice_dict[computer_choice]:
    print("It's a draw")
elif (user_choice == 0 and computer_choice == "paper") or (user_choice == -1 and computer_choice == "rock"):
    print("Computer wins")
else:
    print("You win")