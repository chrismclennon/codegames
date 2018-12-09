# Part 2
# Rank: 514
# Time: 01:06:09
#
# Started ~30 minutes late for this problem
# so wasn't really racing but did get a decent score anyway!

from collections import deque

num_players = 478
num_marbles = 71240 * 100

players = [0 for _ in range(num_players)]
current_player = 0
marbles = deque([0])

for turn_number in range(num_marbles):
    current_player = (current_player + 1) % len(players)
    marble_num = turn_number + 1

    if marble_num % 23 == 0:
        marbles.rotate(7)
        players[current_player] += (marble_num + marbles.popleft())
        continue

    marbles.rotate(-2)
    marbles.appendleft(marble_num)

print('Part two: ' + str(max(players)))
