# July 27, 2016
# https://checkio.org/mission/boolean-algebra/

def boolean(x, y, operation):
    if operation == 'conjunction':
        return x and y
    elif operation == 'disjunction':
        return x or y
    elif operation == 'implication':
        return y or not x
    elif operation == 'exclusive':
        return (x or y) and (x != y)
    elif operation == 'equivalence':
        return x == y


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, u"conjunction") == 0, "and"
    assert boolean(1, 0, u"disjunction") == 1, "or"
    assert boolean(1, 1, u"implication") == 1, "material"
    assert boolean(0, 1, u"exclusive") == 1, "xor"
    assert boolean(0, 1, u"equivalence") == 0, "same?"



