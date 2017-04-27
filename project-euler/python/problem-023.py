# April 17, 2016

import euler

limit = 28123

abundant_numbers = list()
for n in xrange(12,limit+1):
  if sum(euler.factors(n)[:-1]) > n:
    abundant_numbers.append(n)

all_sums = list()
for j in range(len(abundant_numbers)-1):
  for k in range(j,len(abundant_numbers)-1):
    if abundant_numbers[j]+abundant_numbers[k] > limit:
      break
    all_sums.append(abundant_numbers[j]+abundant_numbers[k])

all_sums = sorted(list(set(all_sums)))
ans, k = 0,0
for n in range(1,limit+1):
  if n not in all_sums[k:]:
    ans += n
  if n > all_sums[k] and k < len(all_sums)-1:
    k += 1

print ans
