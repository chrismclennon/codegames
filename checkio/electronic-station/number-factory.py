# Aug 27, 2016
# https://checkio.org/mission/number-factory/

def checkio(number):
    factor, factors = 9, []
    while number > 1 and factor > 1:
        if number % factor == 0:
            number = number / factor
            factors.append(factor)
        else:
            factor -= 1
    return int(''.join(map(str, factors[::-1]))) if number == 1 else 0

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(20) == 45, "1st example"
    assert checkio(21) == 37, "2nd example"
    assert checkio(17) == 0, "3rd example"
    assert checkio(33) == 0, "4th example"
    assert checkio(3125) == 55555, "5th example"
    assert checkio(9973) == 0, "6th example"
    assert checkio(560) == 2578, "Reorder example"
