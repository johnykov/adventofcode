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
for line in lines: # O n
  x = line.strip().split(" ")
  y = [int(i) for i in line.strip().split(" ")]
  if is_safe(y): # O (m-1)
    count += 1
    print(y, is_safe(y))

print(count)

# line = lines[:2]
# y = [int(i) for i in line.strip().split(" ")]
# print(y, is_safe(y))

# print(arrayOfCodes)
