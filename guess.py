#I want to have the program choose a number between x and y.  I want the user to have to guess the number.
#If the guess is too high, they will be told that it's too high
#If it's too low.  They will be told that it's too low


import random

number = random.randint(1,1000000)

print("Number Guessing Game")
print("Guess a number between 1 and 1000000")

def input():
    return int(raw_input("What is your guess? "))

guess = input()

while guess != number:
    if guess < number:
        print("Nope.  It's higher than that")
        guess = input()
    else:
        print("Nope.  Pick something lower")
        guess = input()

print("You got it")

