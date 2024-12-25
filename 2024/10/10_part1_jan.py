from collections import deque
from pprint import pprint

# wzorowałem się na MATRIX BFS z neetcode: https://neetcode.io/courses/dsa-for-beginners/30

# print(list('1234'.strip()))
# print(list(map(int,list('1234'))))
file = './easy'
file = './example'
file = './input'
# st_grid = list(map(list, open(file).read().splitlines()))
# grid = [[int(num) for num in lstt[:]] for lstt in st_grid]
grid = [list(map(int, list(num.strip()))) for num in open(file).readlines()]

pprint(grid)

n = len(grid)
m = len(grid[0])
start_point = []
for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            start_point.append((i, j))

print('start_point', start_point)


def score(grid, start_point):
    # queue = [start_point]
    queue = deque([start_point])
    seen = set()
    seen.add(start_point)
    summits = 0
    while queue:
        # r, c = queue.pop(0)
        r, c = queue.popleft()
        # print(len(queue), 'quue', (r,c))
        # if r == n-1 and c == m-1:
        #     return expected_val
        for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            if r + dr < 0 or r + dr >= n or c + dc < 0 or c + dc >= m:# or (r + dr, c + dc) in seen:
                continue
            if grid[r + dr][c + dc] != grid[r][c]+1:
                continue
            if (r + dr, c + dc) in seen:
                continue
            seen.add((r + dr, c + dc))
            if grid[r + dr][c + dc] == 9:
                summits += 1
            else:
                queue.append((r + dr, c + dc))
                # print((r + dr, c + dc), grid[r + dr][c + dc], (r, c))
                # continue
            # seen.add((r + dr, c + dc))
    return summits


# print(score(grid, start_point[0]))
print(sum(score(grid, point) for point in start_point))
# print(follow(grid, (0,0)))


# Shortest path from top left to bottom right
def bfs(grid):
    ROWS, COLS = len(grid), len(grid[0])
    visit = set()
    queue = deque()
    queue.append((0, 0))
    visit.add((0, 0))

    length = 0
    while queue:
        for i in range(len(queue)):
            r, c = queue.popleft()
            if r == ROWS - 1 and c == COLS - 1:
                return length

            neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in neighbors:
                if (min(r + dr, c + dc) < 0 or
                        r + dr == ROWS or c + dc == COLS or
                        (r + dr, c + dc) in visit or grid[r + dr][c + dc] == 1):
                    continue
                queue.append((r + dr, c + dc))
                visit.add((r + dr, c + dc))
        length += 1
