current_choice="-"
computer_parts=["computer","monitor","keyboard","mouse","mouse mat"]
while current_choice!="0":
  if current_choice in computer_parts:
    print("Adding{}".format(current_choice))
  else:
    print("Please add options from the list below:")
    print("""
    1.Computer
    2.Monitor
    3.Keyboard
    4.Mouse
    5.Mouse mat
    0.Finish
    """)
  current_choice+=input()
else:
  print("You have purchased the following items:")
  print(current_choice)
