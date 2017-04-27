# July 12, 2016
# https://checkio.org/mission/triangle-angles/

import math

def checkio(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        return [0, 0, 0]
    calculate_angle = lambda a, b, c: round(math.degrees(math.acos((b**2 + c**2 - a**2)/(2*b*c))))
    return sorted([calculate_angle(a, b, c), calculate_angle(b, c, a), calculate_angle(c, a, b)])

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"

