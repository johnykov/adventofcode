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


def trail(grid, r, c):
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
  return seen


def loops(grid, r, c):
  dr = -1
  dc = 0

  seen = set()

  while True:
    seen.add((r, c, dr, dc))
    if r + dr < 0 or r + dr >= rows or 0 > dc + c or dc + c >= cols:
      return False
    if grid[r + dr][c + dc] == "#":
      dc, dr = -dr, dc
    else:
      r += dr
      c += dc
    if (r, c, dr, dc) in seen:
      return True

count = 0
# applied first comment from the YT, check loops only for the visited cells
paths = trail(grid, r, c)
# print(paths)
# for cr in range(rows):
#   for cc in range(cols):
for cr, cc in paths:
  if grid[cr][cc] != ".": continue
  grid[cr][cc] = "#"
  if loops(grid, r, c):
    count += 1
  grid[cr][cc] = "."

# 6
# 1784
print(count)