age=24
print("My age is "+str(age)+" years")


print("My age is {0} years".format(age))

print("there are  {0} days in {1},{2},{3},{4},{5},{6} & {7}".format(31,"Jan","March","May","July","Aug","Oct","Dec"))

print("There are {0} days in Jan,Marc,May,July,Aug,Oct,Dec".format(31))

print("Jan:{2},Feb:{0}, Mar:{2}, April:{1},May:{2},Jun:{1},July:{2},sep:{1},Oct:{2},Nov:{1},Dec:{2}".format(28,30,31))

print()

print("""Jan:{2}
      Feb:{0}
      Mar:{2}
       April:{1}
      May:{2}
      Jun:{1}
      July:{2}
      sep:{1}
      Oct:{2}
      Nov:{1}
      Dec:{2}""".format(28,30,31))