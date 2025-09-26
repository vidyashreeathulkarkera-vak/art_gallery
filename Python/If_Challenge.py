name=str(input("Enter your name: "))
age=int(input("Enter your age: "))
if name and age :
    if 18<age<=30:
        print("{}.format(name) Welcome to holiday")
    else:
        print("You are not eligible for current program")
else:
    print("{}.format(name) You have not entered name or age")
