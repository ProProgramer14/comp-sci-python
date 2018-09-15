from random import randint

def random_option():
    """return random option from ["Rock", "Paper", "Scissors", "Spock", "Lizard"]"""
    return ["Rock", "Paper", "Scissors", "Spock", "Lizard"][randint(0, 4)]

def rock_message(computer):
    """Returns the message to display when player enters Rock"""
    if computer == "Paper":
        return "You Lose! Paper covers Rock"
    elif computer == "Spock":
        return "You Lose! Spock vaporizes Rock"
    else:
        return "You Win! Rock smashes " + computer

def paper_message(computer):
    """Returns the message to display when player enters Paper"""
    if computer == "Scissors":
        return "You Lose! Scissors cuts Paper"
    elif computer == "Lizard":
        return "You Lose! Lizard eats Paper"
    else:
        return "You Win! Paper covers " + computer

def scissors_message(computer):
    """Returns the message to display when player enters Scissors"""
    if computer == "Rock":
        return "You Lose! Rock smashes Scissors"
    elif computer == "Spock":
        return "You Lose! Spock crushes Scissors"
    else:
        return "You Win! Scissors cuts " + computer
        
def lizard_message(computer):
    """Returns the message to display when player enters Lizard"""
    if computer == "Scissors":
        return "You Lose! Scissors decapitates Lizard"
    elif computer == "Rock":
        return "You Lose! Rock smashes Lizard"
    elif computer == "Paper":
        return "You Win! Lizard eats Paper"
    else:
        return "You Win! Lizard poisons " + computer

def spock_message(computer):
    """Returns the message to display when player enters Spock"""
    if computer == "Lizard":
        return "You Lose! Lizard poisons Spock"
    elif computer == "Paper":
        return "You Lose! Paper covers Spock"
    else:
        return "You Win! Spock vaporizes " + computer

