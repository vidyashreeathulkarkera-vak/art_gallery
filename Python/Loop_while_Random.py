import random
random_number=random.randint(1,10)
print("Please enter number between 1 and 10")
guess=0

while guess!=random_number:
  guess=int(input())
  if guess==random_number:
    print("You got it the first time")
    break
  else:
    if guess<random_number:
      print("Please guess higher")
    else:
      print("Please guess lower")
    