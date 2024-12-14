with open("./example") as fin:
# with open("./input") as fin:
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
newobst = []
while True:
  next_i = i + dd[direction][0]
  next_j = j + dd[direction][1]

  if not (0 <= next_i < m and 0 <= next_j < n):
    break
  # print(next_i,next_j)
  right_hand_dir = (direction + 1) % 4
  ri, rj = i,j
  if grid[next_i][next_j] == ".":
    while True:
      ri += dd[right_hand_dir][0]
      rj += dd[right_hand_dir][1]
      if (ri, rj, right_hand_dir) in seen:
        newobst.append((next_i,next_j))
        break
      # print(f" ri rj {ri} {rj}")
      if not (0 <= ri < m and 0 <= rj < n):
        break
      if grid[ri][rj] == "#":
        newobst.append((next_i,next_j))
        break

    # if (ri+ dd[right_hand_dir][0], rj + dd[right_hand_dir][1], right_hand_dir) in seen:
    #   newobst.append((next_i,next_j))

  if grid[next_i][next_j] == "#":
    direction = (direction + 1) % 4
  else:
    i, j = next_i, next_j
    seen.add((next_i, next_j, direction))


print(len(seen))

print(newobst)
print(len(newobst))
# obstacle are not needed
# print(obstacles, start_pos)