from random import randint

# create a list of computer options
computer_options = ["Rock", "Paper", "Scissors", "Spock", "Lizard"]

# start player at empty string
player = ""
while player != "q":
    # assign random play option to computer
    computer = computer_options[randint(0, 4)]
    # prompt player for their option
    player = input("\nRock, Paper, Scissors, Lizard, Spock? or 'q' to quit\n")
    if player == computer:
        print("Tie")
    elif player == "Rock":
        if computer == "Paper":
            print("You Lose!", computer, "covers", player)
        elif computer == "Spock":
            print("You Lose!", computer, "vaporizes", player)
        else:
            print("You Win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You Lose!", computer, "cuts", player)
        elif computer == "Lizard":
            print("You Lose!", computer, "eats", player)
        else:
            print("You Win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You Lose!", computer, "smashes", player)
        elif computer == "Spock":
            print("You Lose!", computer, "crushes", player)
        else:
            print("You Win!", player, "cuts", computer)
    elif player == "Lizard":
        if computer == "Scissors":
            print("You Lose!", computer, "decapitates", player)
        elif computer == "Rock":
            print("You Lose!", computer, "smashes", player)
        elif computer == "Paper":
            print("You Win!", player, "eats", computer)
        else:
            print("You Win!", player, "poisons", computer)
    elif player == "Spock":
        if computer == "Lizard":
            print("You Lose!", computer, "poisons", player)
        elif computer == "Paper":
            print("You Lose!", computer, "covers", player)
        else:
            print("You Win!", player, "vaporizes", computer)
    elif player == "q":
        print("Goodbye")
    else:
        print("Invalid entry.  Check your spelling and caps")


