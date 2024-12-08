import sys

# ROW COL

alternatives = [
  (-1,-1), # bottom-left 385
  (-1,0), # down 222
  (-1,1), # bottom right 406
  (0,-1), #left 199
  (0,1),# right 198
  (1,-1), # top left 391
  (1,0),  # top 196
  (1,1) # top right 347
]

def look(i,j,mat, delta, wish):
  #print("look", i,j,delta, wish)
  if len(wish)==0:
    #print("true len")
    return True
  if i<0 or i>=len(mat):
    #print('i')
    return False
  if j<0 or j>=len(mat[i]):
    #print('j')
    return False
  if mat[i][j]!=wish[0]:
    #print('wish', wish, mat[i][j])
    return False
  return look(i+delta[0], j+delta[1], mat, delta, wish[1:])

def test(i,j,mat):
  count=0
  for d in alternatives:
    if look(i,j,mat,d, 'XMAS'):
    # if look(i,j,mat,d, ['X','M','A','S']):
      file1.write(f"{i} {j}\n")
      # if i == 82:
        # SAMXAXMASAMMSMXAAAXMXMAMAMASAASAMMMAMXAMXMAMAXXAAXAMXXXAASXSMSASMAXXSMMMAMAMASMXSAASMSMMMSSMMAMAMXXAMXAXMSSMMSSMXXMMMAMXMMMMMSMSAMXSAMXXXAXA
        # print(mat[i])
      count+=1
  return count


# mat = [l.strip() for l in sys.stdin]
mat = [l.strip() for l in open("input","r")]
# mat = [l.strip() for l in open("inputMissing","r")]
# print(mat)
count = 0
file1 = open('mateush.txt', 'w')
for i in range(len(mat)):
  for j in range(len(mat[i])):
    if mat[i][j]=='X':
      # print(i, j)
      count+=test(i,j,mat)
print(count)
# 2344 Correct
file1.close()