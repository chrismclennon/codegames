# Mar 27, 2016

import euler

primes = [2]

for p in range(3, 2000000, 2):
  if euler.is_prime(p):
    primes.append(p)

print sum(primes)
