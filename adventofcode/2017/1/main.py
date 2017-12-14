#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def sum_sequence(sequence: str, interval: int=1) -> int:
    if len(sequence) <= 1:
        return 0
    rolling_sum = 0
    for index, digit in enumerate(sequence):
        compare_digit = (sequence[index+interval] 
                         if index+interval < len(sequence) 
                         else sequence[index+interval-len(sequence)])
        if digit == compare_digit:
            rolling_sum += int(digit)
    return rolling_sum


if __name__ == '__main__':
    assert sum_sequence('1122') == 3
    assert sum_sequence('1111') == 4
    assert sum_sequence('1234') == 0
    assert sum_sequence('91212129') == 9

    midway = lambda x: len(x) // 2
    assert sum_sequence('1212', interval=midway('1212')) == 6
    assert sum_sequence('1221', interval=midway('1221')) == 0
    assert sum_sequence('123425', interval=midway('123425')) == 4
    assert sum_sequence('123123', interval=midway('123123')) == 12
    assert sum_sequence('12131415', interval=midway('12131415')) == 4

    with open('input.txt') as f:
        value = f.read().strip()
        print('Part A: ' + str(sum_sequence(value)))
        print('Part B: ' + str(sum_sequence(value, interval=midway(value))))
