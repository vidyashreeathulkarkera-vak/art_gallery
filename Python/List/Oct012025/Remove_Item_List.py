available_parts=["computer",
                 "monitor",
                 "keyboard",
                 "mouse",
                 "HDMI cable",
                 "DVD drive"
                 ]
#valid_choices=[str(i) for i in range(1,len(available_parts)+1)]
valid_choices=[]
for i in range(1,len(available_parts)+1):
  valid_choices.append(str(i))  

current_choice="-"
computer_parts=[]
while current_choice!="0":
  if current_choice in  valid_choices:
  
    index=int(current_choice)-1
    chosen_part=available_parts[index]
    if chosen_part in computer_parts:
      print("Removing {}".format(current_choice))
      computer_parts.remove(chosen_part)
    else:
      print("Adding {}".format(current_choice))
      computer_parts.append(chosen_part)
    print("Your List now contais {}".format(computer_parts))
   
  else:
    print("Please Add options from the list below:")
    for number,part in enumerate(available_parts):
      print("{}.{}".format(number+1,part))
  current_choice=input()

print(computer_parts)