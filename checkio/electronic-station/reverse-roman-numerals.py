# August 12, 2017
# https://py.checkio.org/mission/reverse-roman-numerals/


def reverse_roman(roman_numeral: str) -> int:
    if not roman_numeral:
        return None

    arabic = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV',
             'I']
    translator = dict(zip(roman, arabic))
    output, index = 0, 0

    while index < len(roman_numeral):
        one_char = roman_numeral[index]
        two_char = roman_numeral[index:index+2]

        if two_char in translator:
            output += translator[two_char]
            index += 2
        elif one_char in translator:
            output += translator[one_char]
            index += 1
        else:
            raise ValueError('Invalid character: ' + one_char)

    return output


if __name__ == '__main__':
    assert reverse_roman('VI') == 6
    assert reverse_roman('LXXVI') == 76
    assert reverse_roman('CDXCIX') == 499
    assert reverse_roman('MMMDCCCLXXXVIII') == 3888
