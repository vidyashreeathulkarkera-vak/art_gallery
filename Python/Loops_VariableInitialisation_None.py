shopping_List=["milk","pasta","eggs","spam","bread","rice"]

item_To_Find="eggs"
foundAt=None
#for index in range(len(shopping_List)):
#  if shopping_List[index]==item_To_Find:
#    foundAt=index
#    break;

if item_To_Find in shopping_List:
  foundAt=shopping_List.index(item_To_Find)
if foundAt is not None:
  print("Item found at {}".format(foundAt))#prints 3
else:
  print("{} not found".format(item_To_Find))