# April 1, 2016

# Recursive solution using memoization
def count_routes(m,n):
  cache = [[0 for x in range(1000)] for x in range(1000)]
  if m == 0 or n == 0: return 1
  if cache[m][n] != 0: return cache[m][n]
  cache[m][n] = count_routes(m,n-1) + count_routes(m-1,n)
  return cache[m][n]

print count_routes(3,3)
