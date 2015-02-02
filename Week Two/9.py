# Create a program that guesses a secret number
max_number = 100
min_number = 0
# User thinks of an integer between 0 and 100 (to 99, not including 100)
print("Please think of a number between 0 and 100!")

# Program makes guesses and you tell it if it is too high or too low
guess = int(max_number/ 2)
print "Is your secret number %s?" % guess

print "Enter 'h' to indicate the guess is too high. ",
print "Enter 'l' to indicate the guess is too low. ",
print "Enter 'c' to indicate I guessed correctly.",
guess_accuracy = raw_input("")

# Use bisection search to narrow down guesses
while True:
    if guess_accuracy == "c":
        print "Game over. Your secret number was: %s" % guess
        break
    elif guess_accuracy == "h":
        max_number = guess
    elif guess_accuracy == "l":
        min_number = guess
    else:
        print "Sorry I did not understand your input."

    guess = guess = int((max_number + min_number) / 2)
    print "Is your secret number %s?" % guess
    print "Enter 'h' to indicate the guess is too high. ",
    print "Enter 'l' to indicate the guess is too low. ",
    print "Enter 'c' to indicate I guessed correctly.",
    guess_accuracy = raw_input("")
