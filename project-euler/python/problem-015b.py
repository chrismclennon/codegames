# April 1, 2016

# Recursive solution
# MUCH slower
def count_routes(m,n):
  if m == 0 or n == 0: return 1
  return count_routes(m,n-1) + count_routes(m-1,n)

print count_routes(20,20)
