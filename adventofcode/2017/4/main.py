#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def validate_passphrase(passphrase: str, key=lambda x: x) -> bool:
    phrases = passphrase.split()
    phrase_set = set()
    for phrase in phrases:
        phrase = key(phrase)
        if phrase in phrase_set:
            return False
        phrase_set.add(phrase)
    return True


if __name__ == '__main__':
    assert validate_passphrase('aa bb cc dd ee') == True
    assert validate_passphrase('aa bb cc dd aa') == False
    assert validate_passphrase('aa bb cc dd aaa') == True

    sort = lambda x: ''.join(sorted(x))
    assert validate_passphrase('abcde fghij', key=sort) == True
    assert validate_passphrase('abcde xyz ecdab', key=sort) == False
    assert validate_passphrase('a ab abc abd abf abj', key=sort) == True
    assert validate_passphrase('iiii oiii ooii oooi oooo', key=sort) == True
    assert validate_passphrase('oiii ioii iioi iiio', key=sort) == False

    with open('input.txt') as f:
        res_a = sum(1 for line in f if validate_passphrase(line))
        f.seek(0)
        res_b = sum(1 for line in f if validate_passphrase(line, key=sort))
    print('Part A:', res_a)
    print('Part B:', res_b)
