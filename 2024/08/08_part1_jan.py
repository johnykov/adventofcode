from collections import defaultdict
from itertools import combinations

# solution take from william
def in_bounds(cx, cy):
  return 0 <= cx < n and 0 <= cy < n


def get_antinodes(a, b):
  ax, ay = a
  bx, by = b

  cx, cy = ax - (bx - ax), ay - (by - ay)
  dx, dy = bx + (bx - ax), by + (by - ay)

  if in_bounds(cx, cy):
    yield (cx, cy)
  if in_bounds(dx, dy):
    yield (dx, dy)

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

  print(all_locs)

  antinodes = set()
  for item in all_locs:
    for a, b in combinations(all_locs[item], r=2):
      # print(a,b)
      for antinode in get_antinodes(a, b):
        antinodes.add(antinode)


print(len(antinodes))