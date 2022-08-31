userfirstline = input()
usersplit = userfirstline.split()
orders = int(usersplit[0])
watertank = int(usersplit[1])
orders_fufiled = 1
waterRefilCounter = 0
waterRefil = watertank
while int(orders_fufiled) <= int(orders):
  orders_fufiled += 1
  userOrder = input("")
  userOrder += " "
  waterUsed = 0
  if userOrder[1] == "L":
    waterUsed = int(userOrder[0]) + 1
  else:
    waterUsed = int(userOrder[0])
  if watertank < waterUsed:
    waterRefilCounter = waterRefilCounter + 1
    watertank = waterRefil  
  watertank -= int(waterUsed)

print(waterRefilCounter)