with open('sample.txt') as f:
    battlefield = f.read().splitlines()
battlefield = [list(row) for row in battlefield]


class Coordinate:
    LEFT = (-1, 0)
    RIGHT = (1, 0)
    UP = (0, 1)
    DOWN = (0, -1)

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
    def adjacent_points(self):
        return sorted([
            self.peek(Coordinate.UP),
            self.peek(Coordinate.DOWN),
            self.peek(Coordinate.LEFT),
            self.peek(Coordinate.RIGHT)
        ])

    def distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def move(self, direction):
        dx, dy = direction
        self.x += dx
        self.y += dy
    
    def peek(self, direction):
        dx, dy = direction
        x = self.x + dx
        y = self.y + dy
        return Coordinate(x, y)
    

class Unit:
    def __init__(self, battlefield, coordinate, unit_type):
        self.alive = True
        self.attack_power = 3
        self.battlefield = battlefield
        self.coordinate = coordinate
        self.hit_points = 200
        self.unit_type = unit_type

    def __eq__(self, other):
        return self.coordinate == other.coordinate

    def __lt__(self, other):
        return self.coordinate < other.coordinate

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
            self.battlefield[other.coordinate.y][other.coordinate.x] == '.'

    def get_closest_target(self, all_units):
        possible_targets = [target
                            for target in units
                            if target.unit_type != self.unit_type
                                and target != self
                                and target.alive]
        if not possible_targets:
            return None
        possible_targets.sort()  # Enforce reading order
        closest_target = possible_targets[0]
        closest_distance = self.walking_distance(closest_target.coordinate)
        for target in possible_targets[1:]:
            target_distance = self.walking_distance(target.coordinate)
            if target_distance < closest_distance:
                closest_target = target
                closest_distance = target_distance
        return closest_target

    def get_closest_point(self, target):
        # TODO: Get closest _REACHABLE_ point?
        eligible_coordinates = target.get_open_adjacent_coordinates()
        if not eligible_coordinates:
            return None
        eligible_coordinates.sort()  # Enforce reading order
        closest_point = eligible_coordinates[0]
        closest_distance = self.walking_distance(closest_point)
        if not closest_distance:
            return None
        for point in eligible_coordinates[1:]:
            distance = self.walking_distance(point)
            if not distance:
                return None
            if distance < closest_distance:
                closest_point = point
                closest_distance = distance
        return closest_point

    def get_open_adjacent_coordinates(self):
        eligible_coordinates = self.coordinate.adjacent_points
        return [coord
                for coord in eligible_coordinates
                if self.battlefield[coord.y][coord.x] == '.']

    def move(self, point):
        eligible_coordinates = self.get_open_adjacent_coordinates()
        min_coordinate = eligible_coordinates[0]
        min_distance = min_coordinate.distance(point)
        for coordinate in eligible_coordinates[1:]:
            distance = coordinate.distance(point)
            if distance < min_distance:
                min_distance = distance
                min_coordinate = coordinate
        self.battlefield[self.coordinate.y][self.coordinate.x] = '.'
        self.battlefield[min_coordinate.y][min_coordinate.x] = self.unit_type
        self.coordinate = min_coordinate

    def walking_distance(self, point):
        walking_distance = 0
        current_point = self.coordinate
        while current_point != point:
            if walking_distance > 10:
                import pdb; pdb.set_trace()
            eligible_coordinates = [
                current_point.peek(Coordinate.UP),
                current_point.peek(Coordinate.DOWN),
                current_point.peek(Coordinate.LEFT),
                current_point.peek(Coordinate.RIGHT)
            ]
            eligible_coordinates = [
                coord 
                for coord in eligible_coordinates 
                if self.battlefield[coord.y][coord.x] != '#'
                   and self.battlefield[coord.y][coord.x] != self.unit_type
            ]
            if not eligible_coordinates:
                return None
            eligible_coordinates.sort()
            min_coordinate = eligible_coordinates[0]
            min_distance = min_coordinate.distance(point)  # TODO: Compare walking distance not distance?
            for coordinate in eligible_coordinates[1:]:
                distance = coordinate.distance(point)
                if distance < min_distance:
                    min_distance = distance
                    min_coordinate = coordinate
            current_point = min_coordinate
            walking_distance += 1
        return walking_distance


# Identify units
units = []
for y in range(len(battlefield)):
    for x in range(len(battlefield[y])):
        current_char = battlefield[y][x]
        if current_char in ('E', 'G'):
            current_coordinate = Coordinate(x, y)
            unit_type = current_char
            new_unit = Unit(battlefield, current_coordinate, unit_type)
            units.append(new_unit)

# Play the battle
round_number = 0
while len({unit.unit_type for unit in units if unit.alive}) > 1:
    units.sort()
    for unit in units:
        if unit.coordinate.x == 3 and unit.coordinate.y == 4:
            import pdb; pdb.set_trace()
        closest_target = unit.get_closest_target(units)
        if not closest_target: # If there is no target, the combat has ended.
            break
        if unit.coordinate.distance(closest_target.coordinate) == 1:  # Attack if adjacent
            unit.attack(closest_target)
        else:  # Move
            closest_point = unit.get_closest_point(closest_target)
            if not closest_point:
                continue
            unit.move(closest_point)
        for line in battlefield:
            print(''.join(line))
        import pdb; pdb.set_trace()

    round_number += 1
    print('Round {}'.format(round_number))
    for line in battlefield:
        print(''.join(line))
    print(units)
    import pdb; pdb.set_trace()

