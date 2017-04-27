# Mar 26, 2016

import euler

num = 600851475143

# skip even numbers
if int(num**0.5) + 1 % 2 == 0:
  r = reversed(xrange(1, int(num**0.5), 2))
else:
  r = reversed(xrange(1, int(num**0.5)+1, 2))

for i in r:
  if num % i == 0:
    if euler.is_prime(i):
      print "Prime Factor: ", i
      break
