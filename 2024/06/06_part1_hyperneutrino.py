# https://www.youtube.com/watch?v=UPS2jl3JmCs

# file = 'example'
file = 'input'
grid = list(map(list, open(file).read().splitlines()))
# print(grid)
rows = len(grid)
cols = len(grid[0])

for r in range(rows):
  for c in range(cols):
    if grid[r][c] == "^":
      break
  else:
    continue
  break

dr = -1
dc = 0

seen = set()

while True:
  seen.add((r, c))
  if r + dr < 0 or r + dr >= rows or 0 > dc + c or dc + c >= cols:
    break
  if grid[r + dr][c + dc] == "#":
    dc, dr = -dr, dc
  else:
    r += dr
    c += dc

print(len(seen))