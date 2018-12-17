from collections import deque
from enum import Enum
from typing import List


with open('input.txt') as f:
    battlefield = [list(row.strip()) for row in f]


class Direction(Enum):
    LEFT = (-1, 0)
    RIGHT = (1, 0)
    UP = (0, 1)
    DOWN = (0, -1)


class Coordinate:
    """Requires `battlefield` global variable."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return self.x < other.x if self.y == other.y else self.y < other.y

    def __repr__(self):
        return str(self)

    def __str__(self):
        return '({x}, {y})'.format(x=self.x, y=self.y)

    @property
    def adjacent_coordinates(self):
        """Return adjacent coordinates that are not walls."""
        adjacent_coordinates = [
            self.peek(Direction.UP),
            self.peek(Direction.DOWN),
            self.peek(Direction.LEFT),
            self.peek(Direction.RIGHT)
        ]
        return [coord
                for coord in adjacent_coordinates
                if battlefield[coord.y][coord.x] != '#']

    def move(self, direction):
        dx, dy = direction
        self.x += dx
        self.y += dy
    
    def peek(self, direction):
        dx, dy = direction.value
        x = self.x + dx
        y = self.y + dy
        return Coordinate(x, y)

    def path(self, other):
        """
        Return path to other coordinate.
        Return None if no path exists.
        """
        paths = deque([[self]])
        while True:
            if not paths:
                return None
            if len(paths) > 100000:  # If we have too many paths, there probably is no path.
                return None
            path = paths.popleft()
            adjacent = sorted(path[-1].adjacent_coordinates)
            if not adjacent:
                continue
            if any([coord == other for coord in adjacent]):
                path.append(other)
                return path
            for adjacent_coord in adjacent:
                if adjacent_coord in path:
                    continue
                if battlefield[adjacent_coord.y][adjacent_coord.x] != '.':
                    continue
                new_path = path[:]
                new_path.append(adjacent_coord)
                paths.append(new_path)


class Unit:
    """Requires `battlefield` global variable."""

    def __init__(self, coordinate, unit_type):
        self.alive = True
        self.attack_power = 3
        self.coordinate = coordinate
        self.hit_points = 200
        self.unit_type = unit_type

    def __repr__(self):
        return str(self)

    def __str__(self):
        return '[{unit_type} ({hit_points}): {coordinate}]'.format(
            unit_type=self.unit_type,
            hit_points=self.hit_points,
            coordinate=self.coordinate
        )

    def attack(self, other):
        other.hit_points -= self.attack_power
        if other.hit_points <= 0:
            other.alive = False
            battlefield[other.coordinate.y][other.coordinate.x] = '.'

    def get_closest_target(self, all_units):
        possible_targets = [target
                            for target in all_units
                            if target.unit_type != self.unit_type
                               and target != self
                               and target.alive]
        if not possible_targets:
            return None
        possible_targets.sort(key=lambda x: x.coordinate)  # Enforce reading order
        closest_target = possible_targets[0]
        closest_path = self.coordinate.path(closest_target.coordinate)
        for target in possible_targets[1:]:
            path_to_target = self.coordinate.path(target.coordinate)
            if not path_to_target:
                continue
            if not closest_path or len(path_to_target) < len(closest_path):
                closest_target = target
                closest_path = path_to_target
        return closest_target if closest_path is not None else None

    def get_weakest_adjacent_target(self, all_units):
        adjacent_coordinates = self.coordinate.adjacent_coordinates
        possible_targets = [target
                            for target in all_units
                            if target.unit_type != self.unit_type
                               and target != self
                               and target.alive
                               and target.coordinate in adjacent_coordinates]
        possible_targets.sort(key=lambda x: x.coordinate)  # Enforce reading order
        weakest_target = possible_targets[0]
        for target in possible_targets[1:]:
            if target.hit_points < weakest_target.hit_points:
                weakest_target = target
        return weakest_target

    def move(self, point):
        battlefield[self.coordinate.y][self.coordinate.x] = '.'
        battlefield[point.y][point.x] = self.unit_type
        self.coordinate = next_coordinate


# Identify units
units = []
for y in range(len(battlefield)):
    for x in range(len(battlefield[y])):
        current_char = battlefield[y][x]
        if current_char in ('E', 'G'):
            current_coordinate = Coordinate(x, y)
            unit_type = current_char
            new_unit = Unit(current_coordinate, unit_type)
            units.append(new_unit)

# Play the battle
round_number = 0
combat_ended_midturn = False
while len({unit.unit_type for unit in units if unit.alive}) > 1:
    units = [unit for unit in units if unit.alive]
    units.sort(key=lambda x: x.coordinate)
    # if round_number == 37: import pdb; pdb.set_trace()
    for unit_number, unit in enumerate(units):
        if not unit.alive:
            continue
        closest_target = unit.get_closest_target(units)
        if not closest_target:  # If there is no target, do nothing.
            if len({unit.unit_type for unit in units if unit.alive}) <= 1:
                combat_ended_midturn = True
            continue
        path_to_target = unit.coordinate.path(closest_target.coordinate)
        if not path_to_target:  # Cannot reach target. Do nothing.
            continue
        elif len(path_to_target) > 2:  # Move
            next_coordinate = path_to_target[1]
            unit.move(next_coordinate)
        if len(path_to_target)-1 <= 2:  # Attack if adjacent
            # Pick the adjacent unit with the least amount of hit points.
            closest_target = unit.get_weakest_adjacent_target(units)
            unit.attack(closest_target)
            # Check if last unit died.

    if not combat_ended_midturn:
        round_number += 1

    # Print for debugging
    print('Round {}'.format(round_number))
    for line in battlefield:
        print(''.join(line))
    units.sort(key=lambda x: x.coordinate)
    print(units)
    # import pdb; pdb.set_trace()

num_full_rounds = round_number
total_hit_points = sum([unit.hit_points for unit in units if unit.alive])
print('Part one:', num_full_rounds, total_hit_points, num_full_rounds*total_hit_points)

# -1 to num rounds or +3 to total hit points
