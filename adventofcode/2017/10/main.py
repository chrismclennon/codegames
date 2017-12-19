#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def compute_dense_hash(numbers: list) -> list:
    dense_hash = []
    rolling_xor = 0
    for index, value in enumerate(numbers, start=1):
        rolling_xor ^= value
        if index % 16 == 0:
            dense_hash.append(rolling_xor)
            rolling_xor = 0
    return dense_hash

def knot_hash(start_list: list, lengths: str) -> list:
    lengths = list(map(ord, lengths)) + [17, 31, 73, 47, 23]
    sparse = sparse_hash(start_list, lengths, repeat=64)
    dense = compute_dense_hash(sparse)
    hexstring = ''.join('{:02x}'.format(i) for i in dense)
    return hexstring

def sparse_hash(start_list, lengths, repeat=1):
    current_index, skip = 0, 0
    wrap_index = lambda index: (current_index+index) % len(start_list)
    for _ in range(repeat):
        for length in lengths:
            sublist = [start_list[wrap_index(index)]
                       for index in range(length)][::-1]
            for index in range(length):
                start_list[wrap_index(index)] = sublist[index]
            current_index += (length+skip)
            skip += 1
    return start_list


if __name__ == '__main__':
    multiply_first_two = lambda x: x[0]*x[1]
    assert multiply_first_two(sparse_hash(list(range(5)), [3, 4, 1, 5])) == 12
    assert knot_hash(list(range(256)), '') == 'a2582a3a0e66e6e86e3812dcb672a272'
    assert knot_hash(list(range(256)), 'AoC 2017') == '33efeb34ea91902bb2f59c9920caa6cd'
    assert knot_hash(list(range(256)), '1,2,3') == '3efbe78a8d82f29979031a4aa0b16a9d'
    assert knot_hash(list(range(256)), '1,2,4') == '63960835bcdc130f0b66d7ff4f6a5a8e'

    with open('input.txt') as f:
        lengths = [int(x) for x in f.read().strip().split(',')]
        print('Part A:', multiply_first_two(sparse_hash(list(range(256)), lengths)))
    with open('input.txt') as f:
        text = f.read().strip()
        print('Part B:', knot_hash(list(range(256)), text))
