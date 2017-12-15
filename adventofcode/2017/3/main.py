#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import ceil, sqrt


def calculate_layer_width(square: int) -> int:
    layer = ceil(sqrt(square))
    if layer % 2 == 0:
        layer += 1
    return layer

def spiral(target: int) -> int:
    layer_width = calculate_layer_width(target)
    layer_distance = (layer_width - 1) // 2
    max_divergence = layer_width // 2
    start_value = (layer_width - 2) ** 2 + 1
    divergence = max_divergence - 1
    shift = -1
    for current_value in range(start_value+1, target+1):
        if divergence == 0:
            shift = 1
        elif divergence == max_divergence:
            shift = -1
        divergence += shift
    return max(layer_distance + divergence, 0)

class SpiralStressTest:

    DIRECTIONS = {'up': (0, -1), 'down': (0, 1),
                  'left': (-1, 0), 'right': (1, 0),
                  'upleft': (-1, -1), 'upright': (1, -1),
                  'downleft': (-1, 1), 'downright': (1, 1)}

    def __init__(self):
        self.coordinates = {(0,0): 1, (1, 0): 1}
        self.direction = self.DIRECTIONS['up']
        self.last_coordinate = (1, 0)
        self.last_value = 1

    def set_direction(self, coordinate):
        x, y = self.last_coordinate
        layer = max(abs(x), abs(y))
        if x == layer and y == -layer:
            self.direction = self.DIRECTIONS['left']
        elif x == -layer and y == -layer:
            self.direction = self.DIRECTIONS['down']
        elif x == -layer and y == layer:
            self.direction = self.DIRECTIONS['right']
        elif x == layer and y == (layer-1):
            self.direction = self.DIRECTIONS['up']

    def step(self):
        x, y = self.last_coordinate
        dx, dy = self.direction
        self.last_coordinate = (x+dx, y+dy)
        self.last_value = self.sum_neighbors(self.last_coordinate)
        self.coordinates[self.last_coordinate] = self.last_value
        self.set_direction(self.last_coordinate)

    def stress_test(self, target: int) -> int:
        while self.last_value <= target:
            self.step()
        result = min({x for x in self.coordinates.values()
                      if x > target})
        return result

    def sum_neighbors(self, coordinate: tuple) -> int:
        result = 0
        x, y = coordinate
        for direction in self.DIRECTIONS.values():
            dx, dy = direction
            current_coordinate = (x+dx, y+dy)
            result += self.coordinates.get(current_coordinate, 0)
        return result


if __name__ == '__main__':
    assert spiral(1) == 0
    assert spiral(12) == 3
    assert spiral(23) == 2
    assert spiral(1024) == 31

    sst = SpiralStressTest()
    assert sst.stress_test(1) == 2
    assert sst.stress_test(3) == 4
    assert sst.stress_test(22) == 23
    assert sst.stress_test(149) == 304
    assert sst.stress_test(747) == 806
    assert sst.stress_test(331) == 351

    print('Part A:', spiral(361527))
    print('Part B:', sst.stress_test(361527))
