disk = []
fid = 0  # file id
# HyperNeutrino
# https://www.youtube.com/watch?v=5_GstsPDI-Q

# t = open('./example').read()
t = open('./input').read()
for i, char in enumerate(t):
  x = int(char)
  if i % 2 == 0:
    disk += [fid] * x
    fid += 1
  else:
    disk += [-1] * x

# print(disk)
blanks = [i for i, x in enumerate(disk) if x == -1]
# print(blanks)

for i in blanks:
  while disk[-1] == -1: disk.pop()
  if len(disk) <= i: break
  disk[i] = disk.pop()

# print(disk)
print(sum(i * x for i, x in enumerate(disk)))