# June 30, 2016
from collections import namedtuple

def collatz_no_cache(limit):
    Answer = namedtuple('Answer', 'n num_steps')
    ans = Answer(n=0, num_steps=0)

    for x in range(1, limit+1):
        n = x
        num_steps = 1
        while n > 1:
            n = n // 2 if n % 2 == 0 else 3 * n + 1
            num_steps += 1
        if num_steps > ans.num_steps:
            ans = Answer(n=x, num_steps=num_steps)

    return ans

def collatz_cache(limit):
    Answer = namedtuple('Answer', 'n num_steps')
    ans = Answer(n=0, num_steps=0)

    cache = [0] * (limit + 1)

    for x in range(1, limit + 1):
        n = x
        num_steps = 1
        while n > 1:
            if n < limit and cache[n] > 0:
                num_steps += cache[n] - 1
                break
            n = n // 2 if n % 2 == 0 else 3 * n + 1
            num_steps += 1
        cache[x] = num_steps
        if num_steps > ans.num_steps:
            ans = Answer(n=x, num_steps=num_steps)

    return ans

import timeit

print('Without cache:')
start = timeit.default_timer()
print(collatz_no_cache(1000000))
stop = timeit.default_timer()
print('Runtime:', stop - start, 's')

print('\nWith cache:')
start = timeit.default_timer()
print(collatz_cache(1000000))
stop = timeit.default_timer()
print('Runtime:', stop - start, 's')
