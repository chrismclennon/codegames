#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def generator(start: int, multiply: int, divide: int=2147483647,
              factor: int=1) -> int:
    while True:
        start = start * multiply % divide
        if start % factor == 0:
            yield start

def judge_pairs(gen_a, gen_b, num_pairs: int) -> int:
    next_binary = lambda x: next(x) & 0xFFFF
    return sum(next_binary(gen_a) == next_binary(gen_b)
               for _ in range(num_pairs))


if __name__ == '__main__':
    sample_a = generator(65, 16807)
    sample_b = generator(8921, 48271)
    assert [next(sample_a) for _ in range(5)] == [1092455, 1181022009,
                                                  245556042, 1744312007,
                                                  1352636452]
    assert [next(sample_b) for _ in range(5)] == [430625591, 1233683848,
                                                  1431495498, 137874439,
                                                  285222916]
    sample_a = generator(65, 16807)
    sample_b = generator(8921, 48271)
    assert judge_pairs(sample_a, sample_b, 5) == 1

    sample_a = generator(65, 16807)
    sample_b = generator(8921, 48271)
    assert judge_pairs(sample_a, sample_b, 40000000) == 588

    sample_a = generator(65, 16807, factor=4)
    sample_b = generator(8921, 48271, factor=8)
    assert [next(sample_a) for _ in range(5)] == [1352636452, 1992081072,
                                                  530830436, 1980017072,
                                                  740335192]
    assert [next(sample_b) for _ in range(5)] == [1233683848, 862516352,
                                                  1159784568, 1616057672,
                                                  412269392]

    sample_a = generator(65, 16807, factor=4)
    sample_b = generator(8921, 48271, factor=8)
    assert judge_pairs(sample_a, sample_b, 5000000) == 309

    gen_a = generator(516, 16807)
    gen_b = generator(190, 48271)
    print('Part A:', judge_pairs(gen_a, gen_b, 40000000))

    gen_a = generator(516, 16807, factor=4)
    gen_b = generator(190, 48271, factor=8)
    print('Part B:', judge_pairs(gen_a, gen_b, 5000000))
