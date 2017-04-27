# Mar 27, 2016
import euler

found, i = 0, 0

while True:
  if euler.is_prime(i): found += 1
  if found == 10001:
    print i
    break
  i += 1
