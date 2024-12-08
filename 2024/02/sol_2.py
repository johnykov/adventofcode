from typing import List

f = open("input2", "r")
lines = f.readlines()


# https://neetcode.io/solutions/monotonic-array
# check if array is monotonic and consecutive pair of elements is in distance less than <4
def is_safe(y: List[int]) -> bool:
  decrease_count = 0
  increase_count = 0
  count_bad_level = 0
  for i in range(len(y) - 1):
    # print(0 < abs(y[i + 1] - y[i]) < 4, abs(y[i + 1] - y[i]))
    if not (y[i] < y[i + 1]):
      increase_count += 1
    if not (y[i] > y[i + 1]):
      decrease_count += 1
    if not (0 < abs(y[i + 1] - y[i]) < 4):
      count_bad_level += 1

  # return (decrease or increase) and distanced
  # return increase_count + count_bad_level < 2 or decrease_count + count_bad_level < 2
  return [increase_count, decrease_count, count_bad_level]


count = 0
for line in lines:
  x = line.strip().split(" ")
  y = [int(i) for i in line.strip().split(" ")]
  if is_safe(y):
    count += 1
    print(y, is_safe(y))

print(count)

# line = lines[:2]
# y = [int(i) for i in line.strip().split(" ")]
# print(y, is_safe(y))

# print(arrayOfCodes)
