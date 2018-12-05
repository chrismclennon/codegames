# Part 1
# Time: 00:13:36
# Rank: 647
#
# Part 2
# Time: 00:18:43
# Rank: 404

def part_one(polymer):
    polymer = list(polymer)
    keep_going = True
    start_index = 1
    while keep_going:
        keep_going = False
        for index in range(start_index, len(polymer)):
            prev = polymer[index-1]
            current = polymer[index]
            if prev != current and prev.lower() == current.lower():
                del polymer[index]
                del polymer[index-1]
                keep_going = True
                start_index = index-1
                break
    return ''.join(polymer)

sample = 'dabAcCaCBAcCcaDA'
print('Sample:', part_one(sample))

with open('input.txt') as f:
    actual = f.read().strip()
part_one_result = part_one(actual)
print('Part one:', len(part_one_result))

lowest_length = 50000
letters = set([x.lower() for x in actual])
for target_letter in letters:
    part_two_actual = actual
    part_two_actual = (part_two_actual.replace(target_letter.upper(), '')
                                      .replace(target_letter.lower(), ''))
    result = len(part_one(part_two_actual))
    if result < lowest_length:
        lowest_length = result
print('Part two:', lowest_length)
