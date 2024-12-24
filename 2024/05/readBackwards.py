updates = open('input').read()
# updates = open('updatedExample').read()
matrix = updates.splitlines()

rules = set(matrix[:matrix.index('')])
pages = matrix[matrix.index('')+1:]
print(set(rules))
print(pages)

to_rem =[]
for row in pages:
    arr = row.split(',')
    rev = arr[::-1]
    reversed_page_pairs = [a + "|" + b for idx, a in enumerate(rev) for b in rev[idx + 1:]]
    # print(reversed_page_pairs)
    for pair in reversed_page_pairs:
        if pair in rules:
            to_rem.append(row)
            print(pair, row)
            break
# print(to_rem)
to_proc = [x for x in pages if x not in to_rem]
# print(to_proc)

sum=0
for le in to_proc:
    arr = le.split(',')
    sum += int(arr[len(arr)//2])
    print(arr[len(arr)//2])

print(sum)