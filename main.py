import random

# Mapping user input and computer choices to corresponding values
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "snake", -1: "water", 0: "gun"}

# Generating computer's choice
computer = random.choice([1, -1, 0])

# Getting user's choice
youstr = input("Enter your choice (s for snake, w for water, g for gun): ").lower()

# Validating user's input
if youstr not in youDict:
    print("Invalid choice! Please enter 's', 'w', or 'g'.")
else:
    you = youDict[youstr]

    # Displaying choices
    print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

    # Determining the result
    if computer == you:
        print("It's a draw")
    elif (computer == -1 and you == 1) or (computer == 0 and you == -1) or (computer == 1 and you == 0):
        print("You win")
    else:
        print("You lose!!")
