from random import randrange
from math import ceil

def roulette(wallet = 100, random = 50):
    """ Function of the roulette game, that ask the bet amount and number, draw the number result,
    and return the draw number, the result, and the total wallet money and ask if you want to play again
    """
    play = "yes"
    while play.lower() == "yes":
        bet_amount = input("How much do you want to bet?")
        bet_nbr = input("Which number, between 0 and %s do you want to bet on?" %(random-1))
        bet_amount = int(bet_amount)
        bet_nbr = int(bet_nbr)
        draw = randrange(5)
        print("And the draw number is the ", draw)
        if bet_nbr == draw:  # Good number in the draw, you win 3 times your bet
            wallet += ceil(3*bet_amount)
            print("Good number choice, you won ", ceil(3*bet_amount), " $")
            print("You still have %s $ in your wallet" %(wallet))
        elif bet_nbr % 2 == draw % 2:
            wallet += ceil(bet_amount/2)
            print("Good color choice, you won ", ceil(bet_amount/2), " $")
            print("You still have %s $ in your wallet" %(wallet))
        else:
            wallet -= ceil(bet_amount)
            print("Wrong number, try again !!")
            print("You still have %s $ in your wallet" %(wallet))
        play = input("Do you want to play again? Type 'Yes' or 'No'")

if __name__ == '__main__':
    roulette(100,50)