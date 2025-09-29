import random
low=1
high=1000
print("Please guess a number between {} and {}".format(low,high))
input("Press ENTER to start")
guess=1
while True:
  guess=low+(high-low)//2
  high_low=input("My guess is {}. Should I guess higher or lower? " 
  "Enter h or l, or c if my guess was correct ".format(guess)).casefold()
  if high_low=="h":
    low=guess+1
  elif high_low=="l":
    high=guess-1
  elif high_low=="c":
    print("Yay! I guessed your number, {}".format(guess))
    break
  else:
    print("Please enter h, l or c")
  guess+=1
  

 
 