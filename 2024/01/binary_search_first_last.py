def first(array, n):
  return n

def last(array, n):
  return 0


array = [ 1, 2, 3, 9, 9, 9, 9, 10, 10, 12, 13 ]
n = int (input("Enter the number : "))

first_index = first(array, n)
last_index  = last(array, n)

if (first_index == -1 or last_index == - 1) :
  print("Element does not exist")
else :
  print("First occurrence of " + str(n) + " is at index : " + str(first_index))
  print("Last occurrence of " + str(n) + " is at index : " + str(last_index))
  print("Total count : "+ str(last_index - first_index + 1))
