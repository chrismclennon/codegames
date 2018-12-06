# Part 1
# Time: 00:49:53
# Rank: 753      
# 
# Part 2
# Time: 00:57:15 
# Rank: 479

# Oh goodness this got messy.

class Coordinate:
    def __init__(self, coord, index):
        self.x, self.y = map(int, coord.split(', '))
        self.name = index

    def __repl__(self):
        return self.name

    def __str__(self):
        return self.name

def manhattan_distance(x, y, coordinate):
    dx = abs(coordinate.x - x)
    dy = abs(coordinate.y - y)
    distance = dx + dy
    return distance

with open('input.txt') as f:
    data = f.read().splitlines()

sample_data = ['1, 1', '1, 6', '8, 3', '3, 4', '5, 5', '8, 9']
# data = sample_data  # TODO

coordinates = [Coordinate(data_point, index) for index, data_point in enumerate(data)]
max_x = max(coordinates, key=lambda x: x.x)
max_y = max(coordinates, key=lambda x: x.y)
matrix_dim = max(max_x.x, max_y.y)+1
matrix = [[None for _ in range(matrix_dim)] for _ in range(matrix_dim)]
for index, coordinate in enumerate(coordinates):
    matrix[coordinate.y][coordinate.x] = index
for y in range(matrix_dim):
    for x in range(matrix_dim):
        min_distance = None
        min_distance_coordinate = None
        count = 0
        for coordinate in coordinates:
            distance = manhattan_distance(x, y, coordinate)
            if min_distance is None or distance < min_distance:
                min_distance = distance
                min_distance_coordinate = coordinate
                count = 1
            elif min_distance == distance:
                count += 1
        if count > 1:
            matrix[y][x] = '.'
        else:
            matrix[y][x] = min_distance_coordinate.name

from collections import defaultdict
frequencies = defaultdict(int)
for y in range(matrix_dim):
    for x in range(matrix_dim):
        value = matrix[y][x]
        frequencies[value] += 1

# Identify edge coordinates
edge_top = set(matrix[0])
edge_bottom = set(matrix[matrix_dim-1])
edge_left = set(matrix[y][0] for y in range(matrix_dim))
edge_right = set(matrix[y][matrix_dim-1] for y in range(matrix_dim))
all_edge_coordinates = edge_top.union(edge_bottom).union(edge_left).union(edge_right)
for coordinate in coordinates:
    if coordinate.name in all_edge_coordinates:
        coordinate.is_edge = True
    else:
        coordinate.is_edge = False

# Identify max non-edge coordinate area
max_value = None
for key, value in frequencies.items():
    skip = False
    for coordinate in coordinates:
        if coordinate.name == key:
            if coordinate.is_edge:
                skip = True
    if skip:
        continue
    if max_value is None or value > max_value:
        max_value = value
print('Part one:', max_value)

count = 0
for x in range(matrix_dim):
    for y in range(matrix_dim):
        distances = []
        for coordinate in coordinates:
            distances.append(manhattan_distance(x, y, coordinate))
        if sum(distances) < 10000:
            count += 1
print('Part two:', count)
