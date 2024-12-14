def part1(puzzle_input):
  rows = puzzle_input.split('\n')
  # print(len(rows))
  m = len(rows)
  n = len(rows[0])

  def count(r, c):
    if rows[r][c] != 'X':
      return 0
    # print(c,max(c-4,0), rows[r][c:max(c-4,0):-1])
    # print(c, rows[r][c:c-4:-1])
    # 0 1 2 3
    # S A M X
    # if c > 2 and rows[r][c:c-3:-1] == 'XMA':
    #   print(r, c, rows[0][4:0:-1], rows[0][3:0:-1])
    # if c < n - 3 and rows[r][c:c+4] == 'XMAS':
      # file1.write(f"{r} {c}\n")
    return sum([
      c > 2 and rows[r][c:(None if c-4 <0 else c-4):-1] == 'XMAS',                                              # left 198 (missing one) 82 3
      # c > 2 and ''.join(rows[r][c-i] for i in range(4)) == 'XMAS',                                              # left 198 OK
      # c > 2 and rows[r][c-3:c+1] == 'SAMX' mgtezak solution
      c < n - 3 and rows[r][c:c+4] == 'XMAS',                                             # right 198
      r > 2 and ''.join(rows[r-i][c] for i in range(4)) == 'XMAS',                        # up 222
      r < m - 3 and ''.join(rows[r+i][c] for i in range(4)) == 'XMAS',                    # down 196
      r > 2 and c > 2 and ''.join(rows[r-i][c-i] for i in range(4)) == 'XMAS',            # left-up 385
      r > 2 and c < n - 3 and ''.join(rows[r-i][c+i] for i in range(4)) == 'XMAS',        # right-up 406
      r < m - 3 and c > 2 and ''.join(rows[r+i][c-i] for i in range(4)) == 'XMAS',        # left-down 391
      r < m - 3 and c < n - 3 and ''.join(rows[r+i][c+i] for i in range(4)) == 'XMAS',    # right-down 347
    ])

  return sum(count(r, c) for r in range(m) for c in range(n))

# file1 = open('mgtezak.txt', 'w')
# readlines = open('inputMissing', 'r').read()
# readlines = open('input', 'r').read()
readlines = open(0).read()

# readlines1 ='SAMXAXMASAMMSMXAAAXMXMAMAMASAASAMMMAMXAMXMAMAXXAAXAMXXXAASXSMSASMAXXSMMMAMAMASMXSAASMSMMMSSMMAMAMXXAMXAXMSSMMSSMXXMMMAMXMMMMMSMSAMXSAMXXXAXA\n'
# print(readlines[3:None:-1])
print(part1(readlines))
# file1.close()
# A:2343 wrong answer!! Correct is 2344