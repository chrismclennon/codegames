#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def spin(steps: int, step_size: int) -> list:
    state = [0]
    current_index = 0
    for step in range(1, steps+1):
        current_index = (current_index + step_size) % step
        state.insert(current_index+1, step)
        current_index += 1
    return state

def fast_spin(steps: int, step_size: int) -> int:
    current_index, value = 0, 0
    for step in range(1, steps+1):
        current_index = (current_index + step_size) % step + 1
        if current_index == 1:
            value = step
    return value


if __name__ == '__main__':
    assert spin(0, 3) == [0]
    assert spin(1, 3) == [0, 1]
    assert spin(2, 3) == [0, 2, 1]
    assert spin(3, 3) == [0, 2, 3, 1]

    assert fast_spin(3, 3) == 2
    assert fast_spin(2017, 316) == 526

    state = spin(2017, 316)
    index = state.index(2017)
    print('Part A:', state[index+1])
    print('Part B:', fast_spin(50000000, 316))
