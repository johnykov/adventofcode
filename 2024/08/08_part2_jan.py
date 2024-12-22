from collections import defaultdict
from itertools import combinations

def in_bounds(cx, cy):
  return 0 <= cx < n and 0 <= cy < n


def get_antinodes(a, b):
  ax, ay = a
  bx, by = b

  dx, dy = bx - ax, by - ay

  i = 0
  while True:
    if in_bounds(ax - dx * i, ay - dy * i):
      yield (ax - dx * i, ay - dy * i)
    else:
      break
    i += 1

  i = 0
  while True:
    if in_bounds(bx + dx * i, by + dy * i):
      yield (bx + dx * i, by + dy * i)
    else:
      break
    i += 1

# with open('./example') as file:
with open('./input') as file:
  grid = file.read().strip().split('\n')

  # print(grid)
  n = len(grid)

  all_locs = defaultdict(list)
  for i in range(n):
    for j in range(n):
      if grid[i][j] != ".":
        all_locs[grid[i][j]].append((i, j))

  # print(all_locs)

  antinodes = set()
  for item in all_locs:
    for a, b in combinations(all_locs[item], r=2):
      # print(a,b)
      for antinode in get_antinodes(a, b):
        antinodes.add(antinode)


print(len(antinodes))