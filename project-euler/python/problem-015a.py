# April 1, 2016

# Iterative solution
dim = 21 # 20x20 grid is 21x21 nodes
m = [[0 for x in range(dim)] for x in range(dim)]

for x in range(dim):
  m[0][x], m[x][0] = 1, 1

for r in range(1, dim):
  for c in range(1, dim):
    m[r][c] = m[r-1][c] + m[r][c-1]

print m[dim-1][dim-1]
