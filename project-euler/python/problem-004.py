# Mar 26, 2016

import euler

ans = -1

def palin_gen():
  for j in xrange(999,900,-1):
    for k in xrange(999,900,-1):
      n = j * k
      if euler.is_palindrome(n):
        yield n

print max(list(palin_gen()))
