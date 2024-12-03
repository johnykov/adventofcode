f = open("input", "r")
lines = f.readlines()

list1 = []
list2 = []
for line in lines:
  x = line.split("   ")
  list1.append(int(x[0].strip()))
  list2.append(int(x[1].strip()))

list1.sort()
list2.sort()
dist =[]
# print(list1)
# print(list2)

for i, item1 in enumerate(list1):
  dist.append(abs(item1 - list2[i]))
  # print(item1, "  ", list2[i])
print(sum(dist))
