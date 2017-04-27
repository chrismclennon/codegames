def checkio(str_number, radix):
    import string
    result, value = 0, (string.digits + string.ascii_uppercase)[:radix].index
    for exponent, digit in enumerate(reversed(str_number)):
        try:
            result += value(digit) * radix**exponent
        except ValueError:
            return -1
    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A > 10"
