# with open("./example") as fin:
with open("./input") as fin:
  grid = fin.read().strip().split("\n")
  print(grid)
  m = len(grid)
  n = len(grid[0])
  # todo, scan for obstacles and starting point
  # put that in memory
  # move, up until obstacle, then 90degree right until obstacle
  # save trail
  # obstacles = set()
  start_pos = (0, 0)
  # trail = []

found = False
for i, line in enumerate(grid):
  for j, el in enumerate(grid[i]):
    # if el == '#':
    #   obstacles.add((i, j))
    if el == '^':
      start_pos = (i, j)
      found = True
      break
  if found:
    break

# pointers on the start location
print(i, j, el)

direction = 0
dd = [[-1, 0], [0, 1], [1, 0], [0, -1]]

seen = set()
while True:
  next_i = i + dd[direction][0]
  next_j = j + dd[direction][1]

  if not (0 <= next_i < m and 0 <= next_j < n):
    break
  # print(next_i,next_j)

  if grid[next_i][next_j] == "#":
    direction = (direction + 1) % 4
  else:
    i, j = next_i, next_j
    seen.add((next_i, next_j))

print(len(seen))
# obstacle are not needed
# print(obstacles, start_pos)