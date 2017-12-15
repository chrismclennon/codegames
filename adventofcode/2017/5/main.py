#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def jump_maze(instructions: list, increment=lambda x: 1) -> int:
    steps = 0
    current_position = 0
    while 0 <= current_position < len(instructions):
        current_instruction = instructions[current_position]
        instructions[current_position] += increment(current_instruction)
        current_position += current_instruction
        steps += 1
    return steps


if __name__ == '__main__':
    b_increment = lambda x: -1 if x >= 3 else 1
    assert jump_maze([0, 3, 0, 1, -3]) == 5
    assert jump_maze([0, 3, 0, 1, -3], increment=b_increment) == 10

    with open('input.txt') as f:
        instructions = [int(x) for x in f.read().strip().split('\n')]
        print('Part A:', jump_maze(instructions[:]))
        print('Part B:', jump_maze(instructions[:], increment=b_increment))
