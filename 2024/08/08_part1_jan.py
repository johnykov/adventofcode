from collections import defaultdict

with open('./example') as file:
    grid = file.read().strip().split('\n')

    # print(grid)
    n = len(grid)

    all_locs = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if grid[i][j] != ".":
                all_locs[grid[i][j]].append((i,j))

    print(all_locs)
