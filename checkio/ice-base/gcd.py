# July 12, 2016
# https://checkio.org/mission/gcd/solve/

def greatest_common_divisor(*args):
    x, y = args[0], args[1]
    while y:
        x, y = y, x % y
    if len(args) > 2:
        return greatest_common_divisor(x, *args[2:])
    return x

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert greatest_common_divisor(6, 4) == 2, "Simple"
    assert greatest_common_divisor(2, 4, 8) == 2, "Three arguments"
    assert greatest_common_divisor(2, 3, 5, 7, 11) == 1, "Prime numbers"
    assert greatest_common_divisor(3, 9, 3, 9) == 3, "Repeating arguments"

