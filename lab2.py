from lab2_helper import random_option, rock_message, paper_message, scissors_message, lizard_message, spock_message

# start player at empty string
player = ""
while player != "q":
    # assign random play option to computer
    computer = random_option()
    # prompt player for their option
    player = input("\nRock, Paper, Scissors, Lizard, Spock? or 'q' to quit\n")
    if player == computer:
        print("Tie")
    elif player == "Rock":
        print(rock_message(computer))
    elif player == "Paper":
        print(paper_message(computer))
    elif player == "Scissors":
        print(scissors_message(computer))
    elif player == "Lizard":
        print(lizard_message(computer))
    elif player == "Spock":
        print(spock_message(computer))
    elif player == "q":
        print("Goodbye")
    else:
        print("Invalid entry.  Check your spelling and caps")
