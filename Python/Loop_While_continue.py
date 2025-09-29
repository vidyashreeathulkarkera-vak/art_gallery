x = 0
while x < 21:
    if x % 3 == 0 or x % 5 == 0:  # use OR, same as your for-loop
        x += 1
        continue
    print(x)
    x += 1