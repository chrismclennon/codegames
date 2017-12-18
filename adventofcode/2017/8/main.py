#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict
import operator


class Register:

    OPERATOR_TRANSLATION = {'<': operator.lt, '<=': operator.le,
                            '>': operator.gt, '>=': operator.ge,
                            '==': operator.eq, '!=': operator.ne}

    def __init__(self):
        self.register = defaultdict(int)
        self.historical_max = None

    def execute_instructions(self, instructions: list):
        for instruction in instructions:
            interpretation = self.interpret_instruction(instruction)
            operand = self.OPERATOR_TRANSLATION[interpretation['influencer_op']]
            if operand(self.register[interpretation['influencer']],
                       interpretation['influencer_amt']):
                subject = interpretation['subject']
                mod = interpretation['mod']
                amount = interpretation['amount']
                if mod == 'inc':
                    self.register[subject] += amount
                elif mod == 'dec':
                    self.register[subject] -= amount
            self.historical_max = (max(self.historical_max, self.max_register)
                                   if self.historical_max is not None
                                   else self.max_register)

    @staticmethod
    def interpret_instruction(instruction: str) -> dict:
        parts = instruction.split()
        subject, mod, amount = parts[:3]
        influencer, influencer_op, influencer_amt = parts[4:]
        return {'subject': subject,
                'mod': mod,
                'amount': int(amount),
                'influencer': influencer,
                'influencer_op': influencer_op,
                'influencer_amt': int(influencer_amt)}

    @property
    def max_register(self):
        return max(self.register.values())


if __name__ == '__main__':
    sample_instructions = ['b inc 5 if a > 1',
                           'a inc 1 if b < 5',
                           'c dec -10 if a >= 1',
                           'c inc -20 if c == 10']
    sample = Register()
    sample.execute_instructions(sample_instructions)
    expected = {'subject': 'b', 'mod': 'inc', 'amount': 5, 'influencer': 'a',
                'influencer_op': '>', 'influencer_amt': 1}
    assert sample.interpret_instruction('b inc 5 if a > 1') == expected
    assert sample.max_register == 1
    assert sample.historical_max == 10

    with open('input.txt') as f:
        instructions = [line.strip() for line in f]
    register = Register()
    register.execute_instructions(instructions)
    print('Part A:', register.max_register)
    print('Part B:', register.historical_max)
