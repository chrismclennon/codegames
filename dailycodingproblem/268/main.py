# Given a 32-bit positive integer N, determine whether it is a 
# power of four in faster than O(log N) time.

# Explanation:
#   * x & (x - 1) == 0 for powers of 2
#   * If you XOR all valid powers of 4 in 32-bit you get
#     1431655765 as a mask value.
# Runtime: O(1)
# Space: O(1)
def power_of_four(x: int) -> bool:
    return x != 0 and x & (x - 1) == 0 and x & 1431655765 == x

assert power_of_four(0) == False
assert power_of_four(2) == False
assert power_of_four(5) == False
assert power_of_four(8) == False
assert power_of_four(40) == False

assert power_of_four(1) == True
assert power_of_four(4) == True
assert power_of_four(16) == True
assert power_of_four(64) == True

