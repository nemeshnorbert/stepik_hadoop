#!/usr/bin/python3
import sys


def parse_line(line):
    node, dist, children = line.strip().split("\t")
    children = children[1:-1]
    return node, dist, children.split(',') if children else []


def make_line(node, dist, children):
    return "{}\t{}\t{{{}}}".format(node, dist, ','.join(children))


for line in sys.stdin:
    print(line.strip())
    node, dist, children = parse_line(line)
    for child in children:
        print(make_line(child, "INF" if dist == "INF" else int(dist) + 1, []))
