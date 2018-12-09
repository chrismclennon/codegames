# Part 1
# Rank: 1,051
# Time: 00:55:55
#
# Started ~30 minutes late for this problem
# so wasn't really racing but did get a decent score anyway!

num_players = 478
num_marbles = 71240

players = [0 for _ in range(num_players)]
current_player = 0
current_marble = 0
marbles = [0]

for turn_number in range(num_marbles):
    current_player = (current_player + 1) % len(players)
    marble_num = turn_number + 1

    if marble_num % 23 == 0:
        current_marble = (marble_pos - 7) % len(marbles)
        players[current_player] += (marble_num + marbles.pop(current_marble))
        continue

    marble_pos = (current_marble + 2) % len(marbles)
    if marble_pos == 0:
        marble_pos = len(marbles)
        marbles.append(marble_num)
    else:
        marbles.insert(marble_pos, marble_num)
    current_marble = marble_pos

print('Part one: ' + str(max(players)))
