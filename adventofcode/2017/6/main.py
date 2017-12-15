#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def reallocation(bank: list) -> int:
    cycles = 0
    current_state = tuple(bank)
    all_states = set()
    while current_state not in all_states:
        cycles += 1
        all_states.add(tuple(bank))
        index, blocks = max(enumerate(bank), key=lambda x: x[1])
        bank[index] = 0
        for _ in range(blocks):
            index = 0 if index+1 >= len(bank) else index+1
            bank[index] += 1
        current_state = tuple(bank)
    return cycles, current_state

if __name__ == '__main__':
    assert reallocation([0, 2, 7, 0])[0] == 5

    with open('input.txt') as f:
        bank = [int(x) for x in f.read().strip().split('\t')]
        ans = reallocation(bank[:])
        print('Part A:', ans[0])
        print('Part B:', reallocation(list(ans[1]))[0])
