comb = []

# nice
def binlist(n, s):
  if n == 0:
    comb.append(list(map(int,s)))
    return
  binlist(n - 1, s + '0')
  binlist(n - 1, s + '1')
  binlist(n - 1, s + '2')

binlist(3, '')
print(comb)