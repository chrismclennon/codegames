# May 8, 2016
# https://checkio.org/mission/solution-for-anything/

class checkio:
    def __init__(self, anything):
        pass

    __ne__ = __lt__ = __gt__ = __ge__ = __le__ = __eq__ = lambda x,y: True

if __name__ == '__main__':
    import re
    import math

    assert checkio({}) != [],          'You'
    assert checkio('Hello') < 'World', 'will'
    assert checkio(80) > 81,           'never'
    assert checkio(re) >= re,          'make'
    assert checkio(re) <= math,        'this'
    assert checkio(5) == ord,          ':)'

    print('NO WAY :(')
