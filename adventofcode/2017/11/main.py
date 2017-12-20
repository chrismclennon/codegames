#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This is an immensely helpful resource:
# https://www.redblobgames.com/grids/hexagons/

DIRECTIONS = {'n': (1, 0, -1), 's': (-1, 0, 1),
              'ne': (1, -1, 0), 'sw': (-1, 1, 0),
              'nw': (0, 1, -1), 'se': (0, -1, 1)}

def hex_distance(steps: str) -> tuple:
    current_hex = (0, 0, 0)
    steps = steps.split(',')
    add_coordinates = lambda a, b: [sum(x) for x in zip(a, b)]
    max_distance = 0
    for step in steps:
        current_hex = add_coordinates(current_hex, DIRECTIONS[step])
        distance = sum(map(abs, current_hex)) // 2
        max_distance = max(max_distance, distance)
    return distance, max_distance


if __name__ == '__main__':
    assert hex_distance('ne,ne,ne')[0] == 3
    assert hex_distance('ne,ne,sw,sw')[0] == 0
    assert hex_distance('ne,ne,s,s')[0] == 2
    assert hex_distance('se,sw,se,sw,sw')[0] == 3

    with open('input.txt') as f:
        steps = f.read().strip()
    distance, max_distance = hex_distance(steps)
    print('Part A:', distance)
    print('Part B:', max_distance)
