# April 1, 2016

# Combinatorial Solution
# n choose k: n!/(k!(n-k)!)
# m+n choose n. m=n so 2n choose n

import math

dim = 20
ans = math.factorial(2*dim)/math.factorial(dim)**2
print ans
