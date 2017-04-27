# July 27, 2016
# https://checkio.org/mission/boolean-algebra/

def boolean(x, y, operation):
    OPERATIONS = {'conjunction': lambda x, y: x and y,
                  'disjunction': lambda x, y: x or y,
                  'implication': lambda x, y: y or not x,
                  'exclusive': lambda x, y: x ^ y,
                  'equivalence': lambda x, y: x == y
    }
    return OPERATIONS[operation](x, y)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, u"conjunction") == 0, "and"
    assert boolean(1, 0, u"disjunction") == 1, "or"
    assert boolean(1, 1, u"implication") == 1, "material"
    assert boolean(0, 1, u"exclusive") == 1, "xor"
    assert boolean(0, 1, u"equivalence") == 0, "same?"



