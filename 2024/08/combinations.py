
list = [1,2,3, 4]

comb =[]
for i in range(len(list)):
  for j in range(i+1, len(list)):
    comb.append((list[i], list[j]))
print(comb)