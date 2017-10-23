"""
Number Guessing Game
number-guessing-game.py
23-10-2017
Boyke van Vugt
"""

# Library for random numbers 
import random

# Variables
number = random.randint(1, 20)
guess = 0
tries = 0

# Message on startup
print "Guess the number between 1 and 20."
print "You have 8 tries."

# As long as gues isn't the same as the random number
# and tries is less than 3
while guess != number and tries < 8:
	# Ask for answer and put it in variable guess
	guess = input("Your answer: ")
	# Output if guess is lower than the random number
	if guess < number:
		print "Too low!"
	# Output if guess is higher than the random number
	elif guess > number:
		print "Too high!"
	# Tries +1 after each answer
	tries = tries + 1

# If the answer is correct
if guess == number:
	print "Congratulations, thats the right answer!"
	print "You've guessed it in", tries, "tries!"
# If tries = 3
else:
	print "No more guesses! Better luck next time."
	print "The secret number was: ", number
