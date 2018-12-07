# Part 1
# Time: 00:33:32
# Rank: 878
#
# Did not race for Part 2 (went to bed), but did complete a sloppy implementation.

from __future__ import print_function
from collections import defaultdict, deque
from copy import deepcopy


with open('input.txt') as f:
    data = f.read().splitlines()

sample_data = [
    "Step C must be finished before step A can begin.",
    "Step C must be finished before step F can begin.",
    "Step A must be finished before step B can begin.",
    "Step A must be finished before step D can begin.",
    "Step B must be finished before step E can begin.",
    "Step D must be finished before step E can begin.",
    "Step F must be finished before step E can begin.",
]
# data = sample_data


def build_graph(data):
    graph = defaultdict(list)
    for line in data:
        upstream = line[5]
        downstream = line[36]
        graph[upstream].append(downstream)
    return graph

def find_leftmost_steps(graph):
    leftmost_steps = []
    for key1 in graph.keys():
        for values in graph.values():
            if key1 in values:
                break
        else:
            leftmost_steps.append(key1)
    return leftmost_steps

def requirements_met(steps, step):
    for key, value in steps.items():
        if step == key or step in value:
            return False
    return True

def part_one(data):
    graph = build_graph(data)
    answer = []
    while graph:
        leftmost_step = sorted(find_leftmost_steps(graph))[0]
        answer.append(leftmost_step)
        dependent_steps = graph[leftmost_step]
        del graph[leftmost_step]
        for value in dependent_steps:
            if requirements_met(graph, value):
                answer.append(value)
    return ''.join(answer)

print('Part one:', part_one(data))

def step_time(letter):
    return 61 + (ord(letter) - ord('A'))

class Worker:
    def __init__(self):
        self.working = False
        self.working_on = None
        self.time_remaining = 0

def part_two(data):
    graph = build_graph(data)
    num_workers = 5
    workers = [Worker() for _ in range(num_workers)]
    current_second = 0
    steps_completed = set()
    all_steps = {key for key in graph.keys()}.union({x for value in graph.values() for x in value})
    order_of_tasks = part_one(data)
    
#    import pdb; pdb.set_trace()
    while all_steps != steps_completed:
#        from time import sleep
#        sleep(0.1)
        print('== Second:', current_second)
        for worker in workers:
            if worker.working:
                worker.time_remaining -= 1
                if worker.time_remaining == 0:
                    print('Task complete:', worker.working_on)
                    worker.working = False
                    steps_completed.add(worker.working_on)
        for step in all_steps:
            if step in steps_completed:
                continue
            all_dependencies = {k for k, v in graph.items() if step in v}
            current_dependencies = all_dependencies - steps_completed
            tasks_being_worked_on = {worker.working_on for worker in workers if worker.working}
            print('== Checking step:', step)
            print('== Current deps:', current_dependencies)
            if not current_dependencies and step not in tasks_being_worked_on:
                for worker in workers:
                    if not worker.working:
                        print('Task assigned:', step)
                        worker.working = True
                        worker.working_on = step
                        worker.time_remaining = step_time(step)
                        break
        current_second += 1
    return current_second-1

print('Part two:', part_two(data))

