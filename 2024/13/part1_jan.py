
from pprint import pprint

file = './example'
grid = [[int(char) for char in line.strip()] for line in open(file)]
pprint(grid)
