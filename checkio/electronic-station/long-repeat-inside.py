# August 12, 2017
# https://py.checkio.org/mission/long-repeat-inside/


def identify_pattern(input_string: str) -> str:
    charset = {input_string[0]}
    pattern = [input_string[0]]
    for char in input_string[1:]:
        if char in charset:
            return ''.join(pattern)
        charset.add(char)
        pattern.append(char)
    return ''.join(pattern)


def count_pattern(input_string: str, pattern: str) -> int:
    count = 1
    pattern_index = 0
    for index in range(len(pattern)-1, len(input_string)):
        if input_string[index] == pattern[pattern_index]:
            pattern_index += 1
            if pattern_index > len(pattern):
                count += 1
                pattern_index = 0
        else:
            break
    return count


def repeat_inside(input_string: str) -> str:
    if not input_string:
        return None
    output = ''
    for index, char in enumerate(input_string[:-1]):
        pattern = identify_pattern(input_string[index:])
        pattern_frequency = count_pattern(input_string, pattern)
        if (pattern_frequency > 1 and
                pattern_frequency * len(pattern) > len(output)):
            output = pattern * pattern_frequency
    return output


assert repeat_inside('aaaaa') == 'aaaaa'
assert repeat_inside('aabbff') == 'aa'
assert repeat_inside('aababcc') == 'abab'
assert repeat_inside('abc') == ''
assert repeat_inside('abcabcabab') == 'abcabc'
