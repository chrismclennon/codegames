# Jul 6, 2016
# https://checkio.org/mission/box-probability/

def checkio(marbles, step):
    if step == 1:
        return marbles.count('w') / len(marbles)
    if marbles.count('b') == 0:
        return checkio(marbles.replace('w', 'b', 1), step-1)
    elif marbles.count('w') == 0:
        return checkio(marbles.replace('b', 'w', 1), step-1)
    else:
        return marbles.count('b') / len(marbles) * checkio(marbles.replace('b', 'w', 1), step-1) \
            + marbles.count('w') / len(marbles) * checkio(marbles.replace('w', 'b', 1), step-1)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio('bbw', 3) == 0.48, "1st example"
    assert checkio('wwb', 3) == 0.52, "2nd example"
    assert checkio('www', 3) == 0.56, "3rd example"
    assert checkio('bbbb', 1) == 0, "4th example"
    assert checkio('wwbb', 4) == 0.5, "5th example"
    assert checkio('bwbwbwb', 5) == 0.48, "6th example"

