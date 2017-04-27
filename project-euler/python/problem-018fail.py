# April 12, 2016

import re

def sum_nodes_below(flat_triangle, r=0, c=0):
  dim = len(flat_triangle)
  sum_nodes = 0

  i = 1
  for row in range(r,dim):
    for col in range(c,c+i):
      # print '(row,col):',row,col #DEL
      # print 'Element: ',flat_triangle[row][col] #DEL
      sum_nodes += int(flat_triangle[row][col])
    i += 1

  return sum_nodes

triangle = \
"""
3
7 4
2 4 6
8 5 9 3
"""

flat_triangle = re.split('\n',triangle)[1:-1]
dim = len(flat_triangle)

for r in range(len(flat_triangle)):
  flat_triangle[r] = re.split('\s',flat_triangle[r])

print flat_triangle 

r, c = 0, 0
ans = int(flat_triangle[r][c])
print "Starting at:",ans
while r < dim-1:
  left = sum_nodes_below(flat_triangle,r+1,c)
  right = sum_nodes_below(flat_triangle,r+1,c+1)

  print "\nChecking left vs. right" 
  print "Left:",str(flat_triangle[r+1][c])
  print "Right:",str(flat_triangle[r+1][c+1])
  print "Sum left:",left 
  print "Sum right:",right 

  if left >= right:
    r += 1
  else:
    r += 1
    c += 1

  ans += int(flat_triangle[r][c])
  print "Added:",int(flat_triangle[r][c]) 

print '\n'+str(ans)
