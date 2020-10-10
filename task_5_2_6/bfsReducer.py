#!/usr/bin/python3
import sys


def parse_line(line):
    node, dist, children = line.strip().split("\t")
    children = children[1:-1]
    return node, dist, children.split(',') if children else []


def get_updated_children(old_children, new_children):
    if children:
        if old_children:
            assert old_children == children
        return children
    return old_children


def get_updated_dist(old_dist, new_dist):
    if old_dist == "INF":
        return new_dist
    elif new_dist == "INF":
        return old_dist
    return old_dist if int(old_dist) < int(new_dist) else new_dist


def make_line(node, dist, children):
    return "{}\t{}\t{{{}}}".format(node, dist, ','.join(children))


last_node = None
last_dist = None
last_children = None

for line in sys.stdin:
    node, dist, children = parse_line(line)
    if last_node is None:
        last_node = node
        last_dist = dist
        last_children = children
    elif node == last_node:
        last_dist = get_updated_dist(last_dist, dist)
        last_children = get_updated_children(last_children, children)
    else:
        print(make_line(last_node, last_dist, last_children))
        last_node = node
        last_dist = dist
        last_children = children

print(make_line(last_node, last_dist, last_children))
