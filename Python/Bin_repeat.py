low=1
high=1000

print("Think of a number between {} and {} (inclusive). I will try to guess it.".format(low, high))
input("Press enter to start....")
guess=1
while low!=high:
  guess=low+(high-low)//2
  high_low=input("My guess is {}. Should I guess higher or lower? Enter h or l, or c if my guess was correct ".format(guess)).casefold()
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
else:
  print("Your number{} was guessed in {} tries".format(low,guess))

