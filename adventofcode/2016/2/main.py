#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Keypad:
    _INSTRUCTION = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    _KEYPAD = [[None, None,   1, None, None],
               [None,    2,   3,    4, None],
               [   5,    6,   7,    8,    9],
               [None,  'A', 'B',  'C', None],
               [None, None, 'D', None, None]]
    _MAX_LEN = len(_KEYPAD) - 1

    def __init__(self, current_position=(2, 0)):
        self.current_position = current_position

    def move(self, instructions):
        for instruction in instructions:
            new_position = (max(0, min(self.current_position[0] + self._INSTRUCTION[instruction][0], self._MAX_LEN)),
                            max(0, min(self.current_position[1] + self._INSTRUCTION[instruction][1], self._MAX_LEN)))
            if self._KEYPAD[new_position[0]][new_position[1]]:
                self.current_position = new_position
        return self._KEYPAD[self.current_position[0]][self.current_position[1]]

if __name__ == '__main__':
    keypad = Keypad()
    numbers = []
    for instruction in open('2_input.txt', 'r'): 
        numbers.append(str(keypad.move(instruction.strip())))
    print(''.join(numbers))

