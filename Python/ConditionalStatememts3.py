answeer=5
print("Please guess number between 1 and 10")
guess=int(input())
if(guess!=answeer):
    if(guess<answeer):
        print("Please guess higher")
    else:
        print("Please guess lower")
    guess=int(input())                  
    if guess==answeer:
        print("Welldone, you guessed it right")
    else:
         print("Sorry, you guessed it incorrect")
else:
    print("You got it right the first time")