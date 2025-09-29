shopping_List=["milk","pasta","eggs","spam","bread","rice"]
for item in shopping_List:
  if item=="spam":
    break;
  print("Buy "+item)#prints till eggs


item_To_Find="spam"
foundAt=None
for index in range(len(shopping_List)):
  if shopping_List[index]==item_To_Find:
    foundAt=index
    break;
print("Item found at {}".format(foundAt))#prints 3