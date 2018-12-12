# Part 1
# Time: 00:32:04
# Rank: 541
#
# Part 2
# Time: 00:51:09
# Rank: 419

pots = '##..#..##....#..#..#..##.#.###.######..#..###.#.#..##.###.#.##..###..#.#..#.##.##..###.#.#...#.##..'
# pots = '#..#.#..##......###...###'
pots = '.' * 5 + pots + '.' * 7500
pot_zero_index = 5
pots = list(pots)

with open('input.txt') as f:
    f.readline()
    f.readline()
    rules = [rule.strip().split(' => ') for rule in f]

pot_history = []
print('Generation 0:', ''.join(pots))
for generation in range(1, 256):
    # print(generation)
    toggle_pots = dict()
    for index in range(2, len(pots)-2):
        nearby_pots = ''.join(pots[index-2:index+3])
        for rule, outcome in rules:
            if rule == nearby_pots:
                # import pdb; pdb.set_trace()
                toggle_pots[index] = outcome
                break
    for toggle_index, toggle_outcome in toggle_pots.items():
        pots[toggle_index] = toggle_outcome

    ans = 0
    for index, pot in enumerate(pots):
        if pot == '#':
            pot_num = index - pot_zero_index
            ans += pot_num
    pot_history.append(''.join(pots))
    # print('Generation {}:'.format(generation), ''.join(pots), ans)
    print('Generation: {}:'.format(generation), ans)
print('Part one:', ans)   # This only prints correct answer to part one when generation ends on 20.
                          # This changed during the exercise as part of me investigating part 2.
