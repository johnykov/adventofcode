from collections import deque
from pprint import pprint

# https://www.youtube.com/watch?v=layyhtQQuM0&t=436s
file = './easy'
file = './example'
grid = [[int(char) for char in line.strip()] for line in open(file)]
pprint(grid)

rows = len(grid)
cols = len(grid[0])
start_point = [(r,c) for r in range(rows) for c in range(cols) if grid[r][c] == 0]
# for i in range(n):
#     for j in range(m):
#         if grid[i][j] == 0:
#             start_point.append((i, j))

print('start_point', start_point)

def score(grid, r,c):
    q = deque([(r,c)])
    seen = {(r,c)}
    summits=0
    while q:
        cr, cc = q.popleft()
        for nr, nc in [(cr-1,cc),(cr+1,cc),(cr,cc-1),(cr,cc+1)]:
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                continue
            if grid[nr][nc] != grid[cr][cc]+1:
                continue
            # jan: tutaj sie pomylil i william i hyperneutrino, potrzebny jest ten warunek
            if (nr,nc) in seen:
                continue
            seen.add((nr,nc))
            if grid[nr][nc] == 9:
                summits += 1
            else:
                print((nr,nc), grid[nr][nc])
                q.append((nr,nc))
    return summits

# print(score(grid, start_point[0][0], start_point[0][1]))
print(sum(score(grid, r,c) for r,c in start_point))
# print(follow(grid, (0,0)))
