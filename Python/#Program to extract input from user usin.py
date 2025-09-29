#Program to extract input from user using Loops

number=input("Enter a number with seperators: ")
seperators=""
for char in number:
  if not char.isnumeric():
    seperators+=char
print(seperators)