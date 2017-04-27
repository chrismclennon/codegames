#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Coordinate:
    _RIGHT_MOVES = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
    _LEFT_MOVES = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}
    _DIR_COORD = {'N': (1, 0), 'E': (0, 1), 'S': (-1, 0), 'W': (0, -1)}

    def __init__(self, coordinate=[0, 0], direction='N'):
        self.coordinate = coordinate
        self.direction = direction

    def __repr__(self):
        return str(self.coordinate)

    def right(self, steps):
        self.direction = self._RIGHT_MOVES[self.direction]
        self.coordinate[0] = self.coordinate[0] + self._DIR_COORD[self.direction][0] * steps
        self.coordinate[1] = self.coordinate[1] + self._DIR_COORD[self.direction][1] * steps

    def left(self, steps):
        self.direction = self._LEFT_MOVES[self.direction]
        self.coordinate[0] = self.coordinate[0] + self._DIR_COORD[self.direction][0] * steps
        self.coordinate[1] = self.coordinate[1] + self._DIR_COORD[self.direction][1] * steps

    def distance_from_root(self):
        return abs(self.coordinate[0]) + abs(self.coordinate[1])

if __name__ == '__main__':
    coord = Coordinate()
    instructions = 'R2, L1, R2, R1, R1, L3, R3, L5, L5, L2, L1, R4, R1, R3, L5, L5, R3, L4, L4, R5, R4, R3, L1, L2, R5, R4, L2, R1, R4, R4, L2, L1, L1, R190, R3, L4, R52, R5, R3, L5, R3, R2, R1, L5, L5, L4, R2, L3, R3, L1, L3, R5, L3, L4, R3, R77, R3, L2, R189, R4, R2, L2, R2, L1, R5, R4, R4, R2, L2, L2, L5, L1, R1, R2, L3, L4, L5, R1, L1, L2, L2, R2, L3, R3, L4, L1, L5, L4, L4, R3, R5, L2, R4, R5, R3, L2, L2, L4, L2, R2, L5, L4, R3, R1, L2, R2, R4, L1, L4, L4, L2, R2, L4, L1, L1, R4, L1, L3, L2, L2, L5, R5, R2, R5, L1, L5, R2, R4, R4, L2, R5, L5, R5, R5, L4, R2, R1, R1, R3, L3, L3, L4, L3, L2, L2, L2, R2, L1, L3, R2, R5, R5, L4, R3, L3, L4, R2, L5, R5'.split(', ')
    for instruction in instructions:
        direction = instruction[0]
        steps = int(instruction[1:])
        if direction == 'R':
            coord.right(steps)
        else:
            coord.left(steps)
    else:
        print(coord.distance_from_root())

