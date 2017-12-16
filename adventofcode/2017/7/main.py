#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict


class Node:

    def __init__(self, name: str, weight: int, children: list=None):
        self.name = name
        self.weight = weight
        self.children = children

    @property
    def balanced_tree(self) -> bool:
        return (len({c.carry_weight for c in self.children}) == 1
                if self.children is not None else True)

    @property
    def carry_weight(self) -> int:
        return (self.weight if self.children is None
                            else self.weight + sum(child.carry_weight
                                                   for child in self.children))


class Tree:
    
    def __init__(self, reports: list):
        self.root = self.construct_tree(reports)

    def balance_recommendation(self) -> tuple:
        def step(children: list) -> tuple:
            weights = defaultdict(list)
            oddball_node, oddball_weight, common_weight = None, None, None
            for child in children:
                weights[child.carry_weight].append(child)
            for weight, node_list in weights.items():
                if len(node_list) == 1:
                    oddball_node = node_list[0]
                    oddball_weight = weight
                else:
                    common_weight = weight
            return oddball_node, oddball_weight, common_weight

        current_node = self.root
        oddball_weight, common_weight = None, None
        while current_node.balanced_tree is False:
            current_node, oddball_weight, common_weight = step(current_node.children)
        recommendation = common_weight - oddball_weight
        return current_node, recommendation

    def construct_tree(self, reports: list) -> Node:
        nodes = {}
        for report in reports:
            name, weight, children = self.interpret_report(report)
            node = Node(name, weight, children)
            nodes[name] = node

        # Convert string representations of children to references of Node objects.
        for node in nodes.values():
            if node.children is None:
                continue
            for index, child in enumerate(node.children):
                node.children[index] = nodes[node.children[index]]
            
        # Identify root
        all_children = {child for node in nodes.values() if node.children is not None
                              for child in node.children}
        root = (set(nodes.values()) - all_children).pop()
        return root

    @staticmethod
    def interpret_report(report: str) -> tuple:
        report_parts = report.split(' ', 3)
        name = report_parts[0]
        weight = int(report_parts[1][1:-1])
        children = (report_parts[3].split(', ') 
                    if len(report_parts) > 2 else None)
        return name, weight, children


if __name__ == '__main__':
    reports = ["pbga (66)",
               "xhth (57)",
               "ebii (61)",
               "havc (66)",
               "ktlj (57)",
               "fwft (72) -> ktlj, cntj, xhth",
               "qoyq (66)",
               "padx (45) -> pbga, havc, qoyq",
               "tknk (41) -> ugml, padx, fwft",
               "jptl (61)",
               "ugml (68) -> gyxo, ebii, jptl",
               "gyxo (61)",
               "cntj (57)"]
    assert Tree.interpret_report("pbga (66)") == ("pbga", 66, None)
    assert Tree.interpret_report("padx (45) -> pbga, havc, qoyq") == ("padx", 45, ["pbga", "havc", "qoyq"])

    sample_tree = Tree(reports)
    assert sample_tree.root.name == "tknk"

    node, change = sample_tree.balance_recommendation()
    assert node.name == "ugml"
    assert change == -8

    with open('input.txt') as f:
        reports = [line.strip() for line in f]
    tree = Tree(reports)
    node, change = tree.balance_recommendation()
    recommendation_str = '{} {} -> {}'.format(node.name,
                                              node.weight,
                                              node.weight+change)
    print('Part A:', tree.root.name)
    print('Part B:', recommendation_str)
