#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import itertools

def checksum(rows: list) -> int:
    return sum(max(row) - min(row) for row in rows)

def checksum_evenly_divisible(rows: list) -> int:
    checksum = 0
    for row in rows:
        for x, y in itertools.combinations(row, 2):
            big, small = max(x, y), min(x, y)
            if big % small == 0:
                checksum += (big // small)
                break
    return checksum

def translate_tsv(raw_text: str) -> list:
    return [list(map(int, row.split('\t')))
            for row in raw_text.split('\n')]


if __name__ == '__main__':
    with open('input.txt') as f:
        input_value = f.read().strip()
    translated_tsv = translate_tsv(input_value)
    print('Part A: ' + str(checksum(translated_tsv)))
    print('Part B: ' + str(checksum_evenly_divisible(translated_tsv)))
