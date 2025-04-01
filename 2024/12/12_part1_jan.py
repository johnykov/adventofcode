from collections import defaultdict, deque
from pprint import pprint

file = './example'
# file = './input'
grid = [[char for char in line.strip()] for line in open(file)]
pprint(grid)

# 1. regions, outside limits, not seen, same as current
regions = []

rows = len(grid)
cols = len(grid[0])
seen = set()

for r in range(rows):
    for c in range(cols):
        if (r,c) in seen: continue
        seen.add((r,c))
        q = deque([(r,c)])
        region = set()
        region.add((r,c))
        crop = grid[r][c]
        while q:
            cr, cc = q.popleft()
            for nr, nc in [(cr - 1, cc), (cr + 1, cc), (cr, cc - 1), (cr, cc + 1)]:
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue
                if grid[nr][nc] != crop:
                    continue
                if (nr, nc) in region:
                    continue
                region.add((nr, nc))
                q.append((nr, nc))
        seen |= region
        regions.append(region)
pprint(regions)

def perimeter(region):
    return sum(1 for r, c in region if any((nr, nc) not in region for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]))
    output = 0
    for r, c in region:
        output +=4
        for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if (nr, nc) in region:
                output -= 1
    return output

print( [perimeter(region) for region in regions])
# print(sum(len(region) * perimeter(region) for region in regions))
