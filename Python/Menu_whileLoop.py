print("Please choose your options from below:")
print("1.\tLearn Python")
print("2.\tLearn Java")
print("3.\tGo Swimming")
print("4.\tHave Dinner")
print("5.\Goto Bed")
print("0\tExit")

while True:
  choice=(input("Enter your choice:"))
  if choice==0:
    print("Exiting the menu")
    break
  elif choice in "12345":
    print("You have chosen option:",choice)
  else:
    print("Please choose your options from list below:")
    print("1.\tLearn Python")
    print("2.\tLearn Java")
    print("3.\tGo Swimming")
    print("4.\tHave Dinner")
    print("5.\Goto Bed")

    