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

def binary_count(hexstring: str) -> int:
    binary = int(hexstring, 16)
    count = 0
    while binary > 0:
        count += 1
        binary &= (binary-1)
    return count

def build_matrix(input_string: str) -> tuple:
    matrix = []
    for num in range(128):
        current_string = f'{input_string}-{num}'
        hexstring = knot_hash(list(range(256)), current_string)
        binary_string = bin(int(hexstring, 16))[2:]
        matrix.append(binary_string)
    return matrix

def count_regions(matrix: list) -> int:
    raise NotImplementedError

def used_squares(input_string: str) -> int:
    count = 0
    for num in range(128):
        current_string = f'{input_string}-{num}'
        hexstring = knot_hash(list(range(256)), current_string)
        count += binary_count(hexstring)
    return count


if __name__ == '__main__':
    assert binary_count('0xFFFF') == 16
    assert used_squares('flqrgnkx') == 8108

    print('Part A:', used_squares('amgozmfv'))
