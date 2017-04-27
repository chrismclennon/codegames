# April 25, 2016

# Fermat's Little Theorem
# 1/d has a cycle of n digits if 10^n - 1 mod d = 0 for prime d

from euler import prime_sieve

for d in list(prime_sieve(1000))[::-1]:
  period = 1
  while pow(10,period,d) != 1:
    period += 1
  if d-1 == period: 
    break

print d
