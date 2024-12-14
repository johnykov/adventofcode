# updates = open('input').read()
updates = open('updateExample').read()
matrix = updates.splitlines()

rules = set(matrix[:matrix.index('')])
pages = matrix[matrix.index('')+1:]
print(set(rules))
print(pages)

to_rem =[]
to_proc =[]
for row in pages:
  arr = row.split(',')
  rev = arr[::-1]
  reversed_page_pairs = [a + "|" + b for idx, a in enumerate(rev) for b in rev[idx + 1:]]
  # print(reversed_page_pairs)
  failed_rules =[]
  for pair in reversed_page_pairs:
    if pair in rules:
      failed_rules.append(pair)

  rev_failed_rules = failed_rules[::-1]
  for el in rev_failed_rules:
      l = el.split('|')
      idx0 = arr.index(l[0])
      idx1 = arr.index(l[1])
      # print(pair, row, pair.split('|'), idx0, idx1)
      tmp = arr[idx0]
      arr[idx0] = arr[idx1]
      arr[idx1] = tmp
  # print(failed_rules, arr)
      # to_rem.append(row)
  if len(failed_rules) > 0:
    to_proc.append(arr)
      # print( pair, arr)
      # break

print(to_proc)
# to_proc = [x for x in pages if x not in to_rem]
# print(to_proc)

sum=0
for le in to_proc:
  sum += int(le[len(le)//2])
  # print(le[len(le)//2])

print(sum)

# part2