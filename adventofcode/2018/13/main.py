with open('sample_input.txt') as f:
    sample_data = f.read().splitlines()
with open('input.txt') as f:
    data = f.read().splitlines()

data = sample_data

class Cart:
    turn_dir_order = {
        'L': 'S',
        'S': 'R',
        'R': 'L'
    }

    def __init__(self, x, y, dir_facing):
        self.x = x
        self.y = y
        self.dir_facing = dir_facing
        self.next_turn_dir = 'L'

    def update_turn_dir(self):
        self.next_turn_dir = self.turn_dir_order[self.next_turn_dir]


carts = []
for x in range(1, len(data[0])+1):
    for y in range(1, len(data)+1):
        current_char = data[y-1][x-1]
        if current_char in ('>', 'v', '<', '^'):
            new_cart = Cart(x, y, current_char)
            carts.append(new_cart)


