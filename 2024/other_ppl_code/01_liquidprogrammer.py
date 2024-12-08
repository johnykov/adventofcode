# n = [int(a) for a in open(0).read().split()]
n = [int(a) for a in open('input').read().split()]

s1 = s2 = 0
print(n)
print(n[::2])
print(n[1::2])
print(sorted(n[::2]))
print(sorted(n[1::2]))
for a, b in zip(sorted(n[::2]), sorted(n[1::2])):
  s1 += abs(a - b)
  s2 += a * n[1::2].count(a)
print(s1, s2, sep="\n")