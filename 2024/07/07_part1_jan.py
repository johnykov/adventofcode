def generate_combinations_iterative(n):
  combinations = ['']

  for _ in range(n):
    new_combinations = []
    for combo in combinations:
      new_combinations.append(combo + '+')
      new_combinations.append(combo + '*')
      # new_combinations.append(combo + '|')
    combinations = new_combinations

  return combinations

def test1(combos, nums):
  target = nums[0]
  nums = nums[1:]
  # print(nums,range(1, len(nums)))
  for combo in combos:
    val = nums[0]
    # print(val)
    for i in range(1, len(nums)):
      if combo[i - 1] == "+":
        val += nums[i]
      # elif combo[i - 1] == "|":
      #   val = int(f"{val}{nums[i]}")
      else:
        val *= nums[i]
    if val == target:
      return True
      # print(i, nums[i],combo[i-1], val)
  return False
# CORRECT 3245122495150

total = 0
# with open("./example") as fin:
with open("./input") as fin:
  lines = fin.read().strip().split("\n")

  parsed = []
  for line in lines:
    split = list(map(int, line.replace(': ', ' ').split(' ')))
    parsed.append(split)

  for p in parsed:
    operations = len(p) - 2
    combinations = generate_combinations_iterative(operations)
    print(p, operations, combinations, test1(combinations, p))
    if test1(combinations, p):
      total += p[0]
print(total)

# print(test1(['+', '*'], [190, 10, 19]))
# print(generate_combinations_iterative(3))