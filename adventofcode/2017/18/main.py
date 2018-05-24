#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict


def execute_instructions(instructions):
    register = defaultdict(lambda: 0)
    last_sound = None
    instructions = {
        'snd': lambda x: print('Play sound: ' + register[x]),
        'set': lambda x, y: register[x] = y,
        'add': lambda x, y: register[x] += y,
        'mod': lambda x, y: register[x] %= y,
        'rcv': lambda x: last_sound if register[x] != 0 else last_sound,
        'jgz': lambda x, y: y if register[x] > 0 else 0
    }
    for instruction in instructions:
        instruction, x, y = instruction.split()
        command = instruction.split()


if __name__ == '__main__':
    print('Running script.')

