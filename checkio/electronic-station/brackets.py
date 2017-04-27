# July 27, 2016
# https://checkio.org/mission/brackets/

def checkio(expression):
    OPEN_BRACKETS, CLOSED_BRACKETS = '{[(', '}])'
    stack = []
    for character in expression:
        if character in OPEN_BRACKETS:
            stack.append(character)
        elif character in CLOSED_BRACKETS:
            if not stack or OPEN_BRACKETS.index(stack[-1]) == CLOSED_BRACKETS.index(character):
                stack.pop()
            else:
                return False
    return False if stack else True
        
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
