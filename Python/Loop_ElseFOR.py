numbers=[1,45,31,12,60]
for number in numbers:
  if number%8==0:
   print("The number is unacceptable")
   break
else:
  print("All numbers are acceptable")