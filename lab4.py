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
    guess = player.upper()

    # Validate guess
    while not isusersGuessValid(guess):
        print("Invalid guess.")
        player = input("Your guess: ")
        guess = player.upper()

    return guess
    
# Function: Make sure that the guess is valid
# Length is 4 and all characters are in letters array
def isusersGuessValid(guess):
    # Is the length 4?
    if len(guess) != 4:
        return False

    # Are all the letters valid?
    for c in guess:
        if c not in letters:
            return False
    
    # If we get here then we are valid
    return True

# Function: Score the user’s guess 
# (in order to score the guess, it will also need the secret).  
# For now, return True if the guess and the secret are equal, otherwise return False.

def scoreUsersGuess(guess, secret):
    # create variables to hold number of black pins, white pins, and unmatched letters from secret
    black = 0
    white = 0
    leftovers = ''
    
    # loop through each of the 4 letters and check how many are in the correct position
    for i in range(4):
        # is it a match? 
        if guess[i] == secret[i]:
            # yep, give it a black peg 
            black += 1
            # replace that letter with a blank
            guess = guess[0:i] + ' ' + guess[i+1:]
        else:
            # nope, put that secret in leftovers to check in loop below
            leftovers += secret[i]

    # loop leftover secret letters
    for l in leftovers:
        # is the letter somewhere in the users' guess? 
        if l in guess:
            # yep, give it a white peg
            white += 1
            # find the exact letter and replace with blank (could be duplicates)
            pos = guess.find(l)
            guess = guess[0:pos] + ' ' + guess[pos+1:] 

    print("You have %s black pins and %s white pins" % (black, white)) 
       
    # return number of black and white pegs
    return black, white          

#
# Write a program that uses those functions as follows:
#

# First, generate a secret.
secret = generateSecret()


# Print the secret to the screen
print(secret)

# Then, ask the user for a guess
guess = usersGuess()

# Keep asking for guesses until the routine that scores the user’s guess returns True.
while scoreUsersGuess(guess, secret)[0] != 4:
    guess = usersGuess()