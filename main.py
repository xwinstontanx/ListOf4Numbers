import random

ask = int(input("How many sets? "))
print()
for i in range(ask):
  listNum = []
  for x in range(4):
    rand = random.randint(0, 9)
    listNum.append(str(rand))  
  print(i+1, ">",''.join(listNum))
  print()
