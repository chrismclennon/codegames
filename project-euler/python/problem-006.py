# Mar 27, 2016

def sum_of_squares(n):
  return sum([x**2 for x in range(n+1)])

def square_of_sums(n):
  return sum([x for x in range(n+1)])**2

print square_of_sums(100) - sum_of_squares(100)
