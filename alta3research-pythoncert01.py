#!/usr/bin/env python3
"""Dana Kaempen | Northern Trust

   My hi/lo number guessing game.
   To start, ask for the upper bound of the number,
   then have the user guess at the number.  Pgm responds
   Higher or Lower, helping the user hone in on the answer.

   A program to certify that I know something about Python."""

import crayons, numbers, random

def main():

    # Prompt user for upper bound of number, or q to quit
    input_text = input("Lower bound is 1. Enter upper bound (10-1000, q to quit):  ").lower()
    if input_text == "q" or input_text == "":
        return
    elif isinstance(int(input_text), numbers.Integral):
        upper_bound = int(input_text)
        if upper_bound < 10 or upper_bound > 1000:
            print(f"Your input ({upper_bound}) is out of bounds - exiting")
            return 1
    else:
        print(f"Your input ({input_text}) is not a number - exiting")
        return 1

    # Use the number to generate a random Target
    Target = random.randint(0,upper_bound)

    # Loop to prompt user for a guess, or 0 to quit
    while True:
        guess_num = int(input("Enter your guess (0 to quit):  "))
        # If user quits, print a red, Too bad, so sad
        if guess_num == 0:
            print(f'{crayons.red("Too bad, so sad")} - you quit')
            break
        # If user guesses it, print a green YOU WIN
        elif guess_num == Target:
            print(f'You guessed it - {crayons.green("YOU WIN!!!")}')
            break
        elif guess_num > Target:
            print(f"Lower")
        else:
            print(f"Higher")


if __name__ == "__main__":
    main()

