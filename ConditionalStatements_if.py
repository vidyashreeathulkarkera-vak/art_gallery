name=input("Enter your name: ")
age=int(input("How Old are you,{0}?".format(name)))
print(age)

if age>=18:
    print("You can cast your vote")
else:
    print("You are not eligible to vote")