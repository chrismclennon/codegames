# August 12, 2017
# https://py.checkio.org/mission/long-repeat/


def long_repeat(input_string):
    if not input_string:
        return 0
    if len(input_string) <= 2:
        return input_string.count(input_string[0])

    max_streak, current_streak = 0, 1
    for index, char in enumerate(input_string[1:], start=1):
        if char == input_string[index-1]:
            current_streak += 1
        else:
            max_streak = max(max_streak, current_streak)
            current_streak = 1
    return max_streak


assert long_repeat('') == 0
assert long_repeat('a') == 1
assert long_repeat('ab') == 1
assert long_repeat('aa') == 2
assert long_repeat('sdsffffse') == 4
assert long_repeat('ddvvrwwwrggg') == 3
assert long_repeat('abababa') == 1
