#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def connections(pipes: dict, subject: int=0) -> set:
    check_programs = [subject]
    connected_programs = {subject}
    while check_programs:
        current_program = check_programs.pop()
        connections = pipes[current_program]
        for connection in connections:
            if connection not in connected_programs:
                check_programs.append(connection)
                connected_programs.add(connection)
    return connected_programs

def groups(pipes: dict) -> int:
    groups = []
    all_programs = set(pipes.keys())
    while all_programs:
        current_subject = all_programs.pop()
        group = connections(pipes, current_subject)
        groups.append(group)
        all_programs -= group
    return groups

def make_pipe_dict(pipes: list) -> dict:
    pipe_dict = {}
    for pipe in pipes:
        program_id, connection = pipe.split(' <-> ')
        pipe_dict[int(program_id)] = set(map(int, connection.split(', ')))
    return pipe_dict


if __name__ == '__main__':
    sample = ['0 <-> 2',
              '1 <-> 1',
              '2 <-> 0, 3, 4',
              '3 <-> 2, 4',
              '4 <-> 2, 3, 6',
              '5 <-> 6',
              '6 <-> 4, 5']
    sample_dict = make_pipe_dict(sample)
    assert len(connections(sample_dict)) == 6
    assert len(groups(sample_dict)) == 2

    with open('input.txt') as f:
        pipes = [line for line in f]
    pipe_dict = make_pipe_dict(pipes)
    print('Part A:', len(connections(pipe_dict)))
    print('Part A:', len(groups(pipe_dict)))
