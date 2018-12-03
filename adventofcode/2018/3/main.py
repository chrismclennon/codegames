# Part 1
# Time: 00:26:44
# Rank: 1,289
#
# Part 2
# Time: 1:20:51
# Rank: 2,440

import re


class Claim:
    def __init__(self, claim: str):
        self.claim = claim
        self.x, self.y = self.get_coordinate(claim)
        self.width, self.length = self.get_edges(claim)

    def get_coordinate(self, claim):
        regex = re.compile('@ ([0-9]+),([0-9]+)')
        match = regex.search(claim)
        x_coord = int(match.group(1))
        y_coord = int(match.group(2))
        return (x_coord, y_coord)

    def get_edges(self, claim):
        regex = re.compile(': ([0-9]+)x([0-9]+)')
        match = regex.search(claim)
        width = int(match.group(1))
        length = int(match.group(2))
        return (width, length)


# Sample data
# data = ['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']

with open('input.txt') as f:
    data = [x.strip() for x in f.readlines()]
claims = [Claim(claim) for claim in data]

# Part one
fabric = [[0 for _ in range(1000)] for _ in range(1000)]

for claim in claims:
    for y in range(claim.y, claim.y + claim.length):
        for x in range(claim.x, claim.x + claim.width):
            fabric[y][x] += 1

count = 0
for y in range(len(fabric)):
    for x in range(len(fabric[y])):
        current = fabric[y][x]
        if current > 1:
            count += 1

print('Part one:', count)

# Part two
def claims_overlap(claim1, claim2):
    claim1_topleft = (claim1.x, claim1.y)
    claim1_bottomright = (claim1.x + claim1.width - 1, claim1.y + claim1.length - 1)
    claim2_topleft = (claim2.x, claim2.y)
    claim2_bottomright = (claim2.x + claim2.width - 1, claim2.y + claim2.length - 1)

    # claim1 is completely on the right of claim2
    if claim1_topleft[0] > claim2_bottomright[0]:
        return False
    # claim1 is completely on the left of claim2
    if claim1_bottomright[0] < claim2_topleft[0]:
        return False
    # claim1 is completely under claim2
    if claim1_topleft[1] > claim2_bottomright[1]:
        return False
    # claim1 is completely above claim2
    if claim1_bottomright[1] < claim2_topleft[1]:
        return False
    return True


all_claims = set(claims)
overlapping = set()
for index, claim1 in enumerate(claims):
    for claim2 in claims[index+1:]:
        if claims_overlap(claim1, claim2):
            overlapping.add(claim1)
            overlapping.add(claim2)

print('Part two:', (all_claims - overlapping).pop().claim)
