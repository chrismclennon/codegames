# Mar 30, 2016

def sum_divisible_by(n, t):
  p = int((t-1) / n)
  return n*(p*(p+1))/2

print sum_divisible_by(3, 1000) + sum_divisible_by(5, 1000) - sum_divisible_by(15, 1000)
