# Mar 27, 2016

import euler

print reduce(lambda x,y: x+y, [x+2 for x in range(3, 2000000, 2) if euler.is_prime(x)])
