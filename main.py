# This is a sample Python script.
import random
to_guess = str(random.randint(100, 1000))

print("Hey code breaker, can you guess this 3 digit number I have in mind")

tries = 0

def Checknot(guess, toguess):
    for i in guess:
        if i in toguess:
            return False
    return True


while True:
    guess = input("Now try to make a guess \n")
    if len(guess) > 3:
        print("Enter a 3 digit number you idiot!")
        continue
    if guess == to_guess:
        print("Wow you guessed the number in {tries} tries".format(tries=tries))
        break
    if Checknot(guess, to_guess):
        print("Nope")
    else:
        for i in guess:
            if i in to_guess:
                if guess.index(i) == to_guess.index(i):
                    print("Match")
                else:
                    print("Close")
            else:
                print("Nope")
    tries += 1

"""
a thing to remmbr the hasan please put thr things in place pleae do mp keep the toothpaste with the ccap on. flush the toilew3t after using
"""