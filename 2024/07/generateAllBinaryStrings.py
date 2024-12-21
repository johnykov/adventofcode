# https://www.geeksforgeeks.org/generate-all-the-binary-strings-of-n-bits/

def generateAllBinaryStrings(n, arr, i):

  if i == n:
    print(arr)
    return

  # First assign "0" at ith position
  # and try for all other permutations
  # for remaining positions
  arr[i] = 0
  generateAllBinaryStrings(n, arr, i + 1)
  # And then assign "1" at ith position
  # and try for all other permutations
  # for remaining positions
  arr[i] = 1
  # print(i)
  generateAllBinaryStrings(n, arr, i + 1)

n = 2
arr = [None] * n
# Print all binary strings
generateAllBinaryStrings(n, arr, 0)