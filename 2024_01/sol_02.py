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


# https://www.algotree.org/algorithms/binary_search/duplicates/
def first(array, n):
  beg = 0  # begging
  end = len(array) - 1
  while beg <= end:
    mid = int(beg + (end - beg) / 2)
    if array[mid] == n:
      if mid - 1 >= 0 and array[mid - 1] == n:
        end = mid - 1
        continue
      return mid
    elif array[mid] < n:
      beg = mid + 1
    else:
      end = mid - 1
  return -1


def last(array, n):
  beg = 0
  end = len(array) - 1
  while beg <= end:
    mid = int(beg + (end - beg) / 2)
    if array[mid] == n:
      if mid + 1 < len(array) and array[mid + 1] == n:
        beg = mid + 1
        continue
      return mid
    elif array[mid] < n:
      beg = mid + 1
    else:
      end = mid - 1
  return -1


print(list2)
occurrence_product = []
for el in list1: # O n
  fi = first(list2, el) # O log m
  la = last(list2, el) # O log m
  if fi > 0:
    # print(el, " ", fi," ", la, la-fi+1)
    occurrence_product.append((la - fi + 1) * el)

# O (n * log m)

# similarity_score
print(sum(occurrence_product))

