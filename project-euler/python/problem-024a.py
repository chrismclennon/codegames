# April 23, 2016

import itertools
print ''.join(sorted(list(itertools.permutations([str(x) for x in range(10)])))[999999])
