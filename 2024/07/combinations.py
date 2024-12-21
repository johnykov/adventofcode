# no
def get_combinations(input_list):
  combinations = [[]]
  for n in input_list:
    combinations += [combination + [n] for combination in combinations]
  return combinations

comb = []

# nice
def binlist(n, s):
  # print(n, s)
  if n == 0:
    comb.append(s)
    return
  else:
    binlist(n - 1, s + '0')
    binlist(n - 1, s + '1')
    binlist(n - 1, s + '2')

print(binlist(3, ''), comb)

# wtf
n = 3
binlist1 = [f"{i:0{n}b}" for i in range(2 ** n)]
print(binlist1)

def generate_combinations_iterative(n):
  combinations = ['']

  for _ in range(n):
    new_combinations = []
    for combo in combinations:
      new_combinations.append(combo + '0')
      new_combinations.append(combo + '1')
    combinations = new_combinations

  return combinations

# Użycie
# result = generate_combinations_iterative(3)
# print(result)

# print(range(2 ** n))
# print(binlist1)
comb1 = ''
for i in range(8):
  # for el in comb1:
    for j in range(2):
      comb1+=f"{j}"
      # print(comb1)
    #   comb1.append(f"{el}{j}")
  # comb1 +=j
  #     print(i, j)
# print(comb1)

parts = "1941: 5 39 7 808 931".split()

value = int(parts[0][:-1])
nums = list(map(int, parts[1:]))

print(parts, value, nums)

print("12321,a"[:-2])