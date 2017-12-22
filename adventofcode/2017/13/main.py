#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Scanner:

    def __init__(self, scan_range: int):
        self.last_value = None
        self.scan_range = scan_range
        self.scanner = self.generator

    def __iter__(self):
        return self

    def __next__(self):
        self.last_value = next(self.scanner)
        return self.last_value

    @property
    def generator(self):
        while True:
            for index in range(self.scan_range):
                yield index
            for index in range(self.scan_range-2, 0, -1):
                yield index


def make_scanner_dict(specifications: list) -> dict:
    scanners = {}
    for specification in specifications:
        k, v = map(int, specification.split(': '))
        scanners[k] = Scanner(v)
    return scanners

def simple_ride(scanners: dict) -> int:
    severity = 0
    for picosecond in range(max(scanners.keys())+1):
        for depth, scanner in scanners.items():
            scanner_value = next(scanner)
            if depth == picosecond and scanner_value == 0:
                severity += (depth * scanner.scan_range)
    return severity

def smart_ride(scanners: dict) -> int:
    pass


if __name__ == '__main__':
    sample = ['0: 3', '1: 2', '4: 4', '6: 4']
    sample_dict = make_scanner_dict(sample)
    assert simple_ride(sample_dict) == 24

    sample_dict = make_scanner_dict(sample)
    assert smart_ride(sample_dict) == 10

    with open('input.txt') as f:
        scanners = [line for line in f]
    scanner_dict = make_scanner_dict(scanners)
    print('Part A:', simple_ride(scanner_dict))

    scanners_dict = make_scanner_dict(scanners)
    print('Part B:', smart_ride(scanner_dict))
