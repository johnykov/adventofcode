from typing import List

f = open("input", "r")
lines = f.readlines()

# https://neetcode.io/solutions/monotonic-array
# check if array is monotonic and consecutive pair of elements is in distance less than <4
def is_safe(y: List[int]) -> bool:
  decrease = True
  increase = True
  distanced = True
  for i in range(len(y) - 1):
    # print(0 < abs(y[i + 1] - y[i]) < 4, abs(y[i + 1] - y[i]))
    if not (y[i] < y[i + 1]):
      increase = False
    if not (y[i] > y[i + 1]):
      decrease = False
    if not (0 < abs(y[i + 1] - y[i]) < 4):
      distanced = False

  return (decrease or increase) and distanced

count = 0
data =[]
for line in lines: # O n
  x = line.strip().split(" ")
  y = [int(i) for i in line.strip().split(" ")]
  data.append(y)
  if is_safe(y): # O (m-1)
    count += 1
    # print(y, is_safe(y))

print(count)


print(any([is_safe(row[:i] + row[i + 1:]) for i in range(len(row))]) for row in data)
safe_count = sum([any([is_safe(row[:i] + row[i + 1:]) for i in range(len(row))]) for row in data])
print(safe_count)

# line = lines[:2]
# y = [int(i) for i in line.strip().split(" ")]
# print(y, is_safe(y))

# print(arrayOfCodes)