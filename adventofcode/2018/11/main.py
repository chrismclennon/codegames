# Part 1
# Time: 00:19:28
# Rank: 803
#
# Part 2
# Time: 00:30:35
# Rank: 441

serial_number = 4172
row_dim = 300
col_dim = 300

grid = [[None] * col_dim for _ in range(row_dim)]
for row in range(1, row_dim+1):
    for col in range(1, col_dim+1):
        rack_id = col + 10
        power_level = int(str((rack_id * row + serial_number) * rack_id)[-3]) - 5
        grid[row-1][col-1] = power_level

max_total_power = 0
max_x, max_y = 0, 0
for y in range(row_dim-3):
    for x in range(col_dim-3):
        total_power = sum(grid[y][x:x+3]) + sum(grid[y+1][x:x+3]) + sum(grid[y+2][x:x+3])
        if total_power > max_total_power:
            max_total_power = total_power
            max_x = x
            max_y = y

print('Part one:', max_x+1, max_y+1)


# Decided to go with the dirty brute force solution for Part B
max_size = 0
max_total_power = 0
for size in range(1, 115): #301):
    print('Sizing up:', size)
    for y in range(row_dim-size):
        for x in range(col_dim-size):
            total_power = 0
            for _y in range(size):
                total_power += sum(grid[y+_y][x:x+size])
                if total_power > max_total_power:
                    max_total_power = total_power
                    max_size = size
                    max_x = x
                    max_y = y

print('Part two:', max_x+1, max_y+1, max_size)
