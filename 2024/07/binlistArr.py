comb = []

def binlist(n, s):
  # print(n, s)
  if n == 0:
    comb.append(s)
    return
  s[n - 1] = '0'
  binlist(n - 1, s)
  s[n - 1] = '1'
  binlist(n - 1, s)
  # s.append('2')
  # binlist(n - 1, s)


arr = [None] * 3
print(binlist(3, arr), comb)