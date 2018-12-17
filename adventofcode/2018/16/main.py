import re


with open('input_1.txt') as f:
    data = f.read().splitlines()

# All things assume REGISTER exists
REGISTER = [None] * 4

def addr(a, b, c):
    REGISTER[c] = REGISTER[a] + REGISTER[b]

def addi(a, b, c):
    REGISTER[c] = REGISTER[a] + b

def mulr(a, b, c):
    REGISTER[c] = REGISTER[a] * REGISTER[b]

def muli(a, b, c):
    REGISTER[c] = REGISTER[a] * b

def banr(a, b, c):
    REGISTER[c] = REGISTER[a] & REGISTER[b]

def bani(a, b, c):
    REGISTER[c] = REGISTER[a] & b

def borr(a, b, c):
    REGISTER[c] = REGISTER[a] | REGISTER[b]

def bori(a, b, c):
    REGISTER[c] = REGISTER[a] | b

def setr(a, b, c):
    REGISTER[c] = REGISTER[a]

def seti(a, b, c):
    REGISTER[c] = a

def gtir(a, b, c):
    REGISTER[c] = 1 if a > REGISTER[b] else 0

def gtri(a, b, c):
    REGISTER[c] = 1 if REGISTER[a] > b else 0

def gtrr(a, b, c):
    REGISTER[c] = 1 if REGISTER[a] > REGISTER[b] else 0

def eqir(a, b, c):
    REGISTER[c] = 1 if a == REGISTER[b] else 0

def eqri(a, b, c):
    REGISTER[c] = 1 if REGISTER[a] == b else 0

def eqrr(a, b, c):
    REGISTER[c] = 1 if REGISTER[a] == REGISTER[b] else 0

opcodes = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]


import re
from collections import defaultdict
word_regex = '[A-z]+:\s+\\[(\d+), (\d+), (\d+), (\d+)\\]'
result = 0
all_cases = defaultdict(list)
for line_number in range(0, len(data), 4):
    REGISTER = [int(x) for x in re.findall(word_regex, data[line_number])[0]]
    INPUT = [int(x) for x in data[line_number+1].split(' ')]
    EXPECTED_RESULT = [int(x) for x in re.findall(word_regex, data[line_number+2])[0]]
    ORIGINAL_REGISTER = REGISTER[:]

    possible_opcodes = []
    for opcode in opcodes:
        opcode_num, a, b, c = INPUT
        opcode(a, b, c)
        if REGISTER == EXPECTED_RESULT:
            possible_opcodes.append(opcode)
        REGISTER = ORIGINAL_REGISTER[:]
    if len(possible_opcodes) >= 3:
        result += 1
    all_cases[opcode_num].append(possible_opcodes)

print('Part one:', result)

groomed_cases = defaultdict(list)
for opcode, test_cases in all_cases.items():
    set_test_cases = [set(x) for x in test_cases]
    result = set_test_cases[0]
    for test_case in set_test_cases[1:]:
        result = result.intersection(test_case)
    groomed_cases[opcode] = result

solved_opcodes = {}
while groomed_cases:
    expired_opcodes = []
    for opcode_num, possible_opcodes in groomed_cases.items():
        if len(possible_opcodes) == 1:
            discovered_opcode = possible_opcodes.pop()
            solved_opcodes[opcode_num] = discovered_opcode
            expired_opcodes.append(opcode_num)
            for _, possible_opcodes2 in groomed_cases.items():
                if discovered_opcode in possible_opcodes2:
                    possible_opcodes2.remove(discovered_opcode)
    for expired_opcode in expired_opcodes:
        del groomed_cases[expired_opcode]


REGISTER = [0, 0, 0, 0]

with open('input_2.txt') as f:
    data = f.read().splitlines()

for line in data:
    line = [int(x) for x in line.split(' ')]
    opcode_num, a, b, c = line
    solved_opcodes[opcode_num](a, b, c)

print(REGISTER)


