age=int(input("How Old are you?"))
#if 16<=age<=65:
if age in range(16,66):
  print("Have a great day at work") 
else:
  print("Enjoy your free time")

print("-"*100)

if age not in range(16,66):
  print("Enjoy your free time")
else:
  print("Have a great day at work")