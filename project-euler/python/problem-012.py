# Mar 29, 2016

import euler

n, new_num = 1, 1
while len(euler.factors(new_num)) < 500:
  n += 1
  new_num = int((n * (n+1))/2)

print "Ans:",new_num
