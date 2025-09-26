name=input("Enter your name")
age=int(input("How old are you,{0}?".format(name)))
print(age)

if(age<18):
    print("You arent od  enough to vote")
    print("Please come back after{0} years".format(18-age))
   
elif age==900:
    print("Sorry,Yoda, you die in return of Jedi")
else:
    print("You are old enough to Vote")
    print("Please put your X in box")