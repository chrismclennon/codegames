#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def calculate_score(stream: str) -> int:
    level = 0
    total_score = 0
    skip_next = False
    garbage = False
    garbage_count = 0
    for index, character in enumerate(stream):
        if skip_next:
            skip_next = False
            continue
        if garbage and character not in ('>', '!'):
            garbage_count += 1
        if character == '<':
            garbage = True
        elif character == '>':
            garbage = False
        elif character == '!':
            skip_next = True
        elif character == '{':
            if not garbage:
                level += 1
        elif character == '}':
            if not garbage:
                total_score += level
                level -= 1
    return total_score, garbage_count



if __name__ == '__main__':
    assert calculate_score('{}')[0] == 1
    assert calculate_score('{{{}}}')[0] == 6
    assert calculate_score('{{},{}}')[0] == 5
    assert calculate_score('{{{},{},{{}}}}')[0] == 16
    assert calculate_score('{<a>,<a>,<a>,<a>}')[0] == 1
    assert calculate_score('{{<ab>},{<ab>},{<ab>},{<ab>}}')[0] == 9
    assert calculate_score('{{<!!>},{<!!>},{<!!>},{<!!>}}')[0] == 9
    assert calculate_score('{{<a!>},<a!>},{<a!>},{<ab>}}')[0] == 3

    assert calculate_score('<>')[1] == 0
    assert calculate_score('<random characters>')[1] == 17
    assert calculate_score('<<<<>')[1] == 3
    assert calculate_score('<{!>}>')[1] == 2
    assert calculate_score('<!!>')[1] == 0
    assert calculate_score('<!!!>>')[1] == 0
    assert calculate_score('<o"i!a,<{i<a>')[1] == 9

    with open('input.txt') as f:
        stream = f.read().strip()
    total_score, garbage_count = calculate_score(stream)
    print('Part A:', total_score)
    print('Part B:', garbage_count)

