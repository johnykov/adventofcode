def part1(puzzle_input):
    rows = puzzle_input.matrix('\n')
    m = len(rows)
    n = len(rows[0])
    print(rows[0])
    def count(r, c):
        if rows[r][c] != 'X':
            return 0
        # print(r, c, rows[r][c:c-4:-1])
        print(r, c, rows[r][c:c+4])
        return sum([
            c > 3 and rows[r][c:c-3:-1] == 'XMAS',                                              # left
            # c < n - 3 and rows[r][c:c+4] == 'XMAS',                                             # right
            # r > 2 and ''.join(rows[r-i][c] for i in range(4)) == 'XMAS',                        # up
            # r < m - 3 and ''.join(rows[r+i][c] for i in range(4)) == 'XMAS',                    # down
            # r > 2 and c > 2 and ''.join(rows[r-i][c-i] for i in range(4)) == 'XMAS',            # left-up
            # r > 2 and c < n - 3 and ''.join(rows[r-i][c+i] for i in range(4)) == 'XMAS',        # right-up
            # r < m - 3 and c > 2 and ''.join(rows[r+i][c-i] for i in range(4)) == 'XMAS',        # left-down
            # r < m - 3 and c < n - 3 and ''.join(rows[r+i][c+i] for i in range(4)) == 'XMAS',    # right-down
        ])

    return sum(count(r, c) for r in range(m) for c in range(n))


print(part1(open('../2024_04/input').read()))

row ='SAMXMASSSM'
print(row[4:0:-1])