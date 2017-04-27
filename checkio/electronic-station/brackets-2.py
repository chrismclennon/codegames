# July 27, 2016
# https://checkio.org/mission/brackets/

def checkio(expression):
    stripped_expression = ''.join([c for c in expression if c in '()[]{}'])
    while any(set_of_brackets in stripped_expression for set_of_brackets in ('()', '[]', '{}')):
        stripped_expression = stripped_expression.replace('()', '').replace('[]', '').replace('{}', '')
    return not stripped_expression

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
