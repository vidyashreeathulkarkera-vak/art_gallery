number="9,223;372:036;854:775;807"
seperators=""
for char in number:
  if not char.isnumeric():
    seperators+=char
print(seperators)