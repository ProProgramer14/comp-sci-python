from random import choice

# Array of available options
letters = ["A","B","C","D","E","F"]

# Function: that generates a secret
def generateSecret():
    str = ""
    for _i in range(0,4):
        str = str + choice(letters)
    return str

# Function: Gets the users guess
def usersGuess():
    player = input("Your guess: ")
    return player.upper()
    

# Function: Make sure that the guess is valid (always return true)
def isusersGuessValid():
    return True

# Score the user’s guess (in order to score the guess, it will also need the secret).  
# For now, return True if the guess and the secret are equal, otherwise return False.
def scoreusersGuess(guess, secret):
    if guess == secret:
        return True
    else:
        return False

# Write a program that uses those functions as follows:

# First, generate a secret.
secret = generateSecret()

# Print the secret to the screen
print(secret)

# Then, ask the user for a guess
guess = usersGuess()

# Keep asking for guesses until the routine that scores the user’s guess returns True.

while scoreusersGuess(guess, secret) != True:
    guess = usersGuess()
    
