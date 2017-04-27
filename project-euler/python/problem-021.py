# April 15, 2016

import euler

amicable_numbers = list()

for n in range(1,10000):
  b = sum(euler.factors(n)[:-1])
  if n != b and sum(euler.factors(b)[:-1]) == n and n not in amicable_numbers:
    amicable_numbers.append(n)
    if b <= 10000:
      amicable_numbers.append(b)

print sorted(amicable_numbers)
print '\n'+str(sum(amicable_numbers))

