# August 15, 2017
# https://py.checkio.org/mission/hamming-distance2/


def checkio(n: int, m: int) -> int:
    return bin(n ^ m).count('1')


if __name__ == '__main__':
    assert checkio(117, 17) == 3
    assert checkio(1, 2) == 2
    assert checkio(16, 15) == 5
