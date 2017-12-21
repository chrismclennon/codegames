#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from string import ascii_lowercase


def promenade_cycle(programs: str, instructions: list) -> tuple:
    cycles = []
    while programs not in cycles:
        cycles.append(programs)
        programs = promenade(programs, instructions)
    return cycles

def exchange(programs: list, pos_a: int, pos_b: int) -> list:
    programs[pos_a], programs[pos_b] = programs[pos_b], programs[pos_a]
    return programs

def partner(programs: list, prog_a, prog_b) -> list:
    index_a, index_b = programs.index(prog_a), programs.index(prog_b)
    programs[index_a], programs[index_b] = programs[index_b], programs[index_a]
    return programs

def promenade(programs: str, instructions: list) -> str:
    programs = list(programs)
    for instruction in instructions:
        first_char = instruction[0]
        if first_char == 's':
            programs = spin(programs, int(instruction[1:]))
        elif first_char == 'x':
            pos_a, pos_b = map(int, instruction[1:].split('/'))
            programs = exchange(programs, pos_a, pos_b)
        elif first_char == 'p':
            prog_a, prog_b = instruction[1:].split('/')
            programs = partner(programs, prog_a, prog_b)
    return ''.join(programs)

def spin(programs: list, move: int) -> list:
    return programs[-move:] + programs[:-move]


if __name__ == '__main__':
    sample = list(ascii_lowercase[:5])
    assert spin(sample, 3) == list('cdeab')

    sample = list(ascii_lowercase[:5])
    assert spin(sample, 1) == list('eabcd')

    sample = list(ascii_lowercase[:5])
    assert exchange(sample, 3, 4) == list('abced')

    sample = list(ascii_lowercase[:5])
    assert partner(sample, 'a', 'b') == list('bacde')

    sample = list(ascii_lowercase[:5])
    assert promenade(sample, ['s1', 'x3/4', 'pe/b']) == 'baedc'

    sample = list(ascii_lowercase[:5])
    for _ in range(2):
        sample = promenade(sample, ['s1', 'x3/4', 'pe/b'])
    assert sample == 'ceadb'

    with open('input.txt') as f:
        instructions = f.read().strip().split(',')
    print('Part A:', promenade(ascii_lowercase[:16], instructions))

    cycle = promenade_cycle(ascii_lowercase[:16], instructions)
    print('Part B:', cycle[1000000000 % len(cycle)])

