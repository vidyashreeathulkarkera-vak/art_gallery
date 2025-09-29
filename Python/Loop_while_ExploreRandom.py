import random
highest=10
answer=random.randint(1,highest)
print("Please enter number between 1 and {}".format6(highest))
guess=int(input())
if guess==answer:
  print("You got it first time")
else:
  if guess<answer:
    print("Please guess higher")
  else:
    print("Please guess lower")
  guess=int(input())
  if guess==answer:
    print("Well done you guessed it")
  else:
    print("Sorry you have not guessed it, the answer was {}".format(answer))


