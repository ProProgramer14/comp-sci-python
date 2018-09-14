from random import randint

# create a list of computer options
computer_options = ["Rock", "Paper", "Scissors"]

# start player at empty string
player = ""
while player != "q":
    # assign random play option to computer
    computer = computer_options[randint(0, 2)]
    # prompt player for their option
    player = input("\nRock, Paper, Scissors? or 'q' to quit\n")
    if player == computer:
        print("Tie")
    elif player == "Rock":
        if computer == "Paper":
            print("You Lose!", computer, "covers", player)
        else:
            print("You Win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You Lose!", computer, "cuts", player)
        else:
            print("You Win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You Lose!", computer, "smashes", player)
        else:
            print("You Win!", player, "cuts", computer)
    elif player == "q":
        print("Goodbye")
    else:
        print("Invalid entry.  Check your spelling and caps!")

