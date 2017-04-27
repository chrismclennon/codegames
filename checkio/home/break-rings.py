# July 10, 2016
# https://checkio.org/mission/break-rings/
from itertools import combinations

def break_rings(rings):
    # Break all combinations of n rings until a broken ring is present in all edges
    unique_rings = set.union(*rings)
    for n in range(1, len(unique_rings)):
        for broken_rings in combinations(unique_rings, n):
            if all(ring & set(broken_rings) for ring in rings):
                return n

def break_rings_1(rings):
    # Choose an edge and take the minimum outcome between breaking each ring
    if len(rings) == 0:
        return 0
    r1, r2 = rings[0]
    return min(1 + break_rings(tuple(ring for ring in rings if r1 not in ring)),
            1 + break_rings(tuple(ring for ring in rings if r2 not in ring)))
    

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert break_rings(({'a', 'b'}, {'b', 'c'}, {'c', 'd'}, {'c', 'e'}, {'e', 'd'}, {'e', 'f'}, {'d', 'f'}, {'d', 'g'})) == 3, "CLRS"
    assert break_rings(({1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {4, 6})) == 3, "example"
    assert break_rings(({1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4})) == 3, "All to all"
    assert break_rings(({5, 6}, {4, 5}, {3, 4}, {3, 2}, {2, 1}, {1, 6})) == 3, "Chain"
    assert break_rings(({8, 9}, {1, 9}, {1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {8, 7})) == 5, "Long chain"
