#!/usr/bin/python3
import sys
import itertools


def key_getter(line):
    key, value = line.strip().split("\t", 1)
    return key


def groupper(stream):
    for key, group in itertools.groupby(stream, key=key_getter):
        yield key, group


def parse_line(line):
    nodename, page_rank, adjacency_list = line.strip().split("\t")
    adjacency_list = adjacency_list[1:-1]
    neighbours = []
    if adjacency_list:
        neighbours = adjacency_list.split(",")
    return nodename, float(page_rank), neighbours


def make_output(nodename, page_rank, neighbours):
    adjacency_list = ','.join(neighbours)
    return "{}\t{:.3f}\t{{{}}}".format(nodename, page_rank, adjacency_list)


total_nodes = 5
alpha = 0.1

for nodename, lines in groupper(sys.stdin):
    node_neighbours = None
    node_page_rank = 0.0
    for line in lines:
        _, page_rank, neighbours = parse_line(line)
        if neighbours:
            node_neighbours = neighbours
        else:
            node_page_rank += page_rank
    assert node_neighbours is not None
    node_page_rank = alpha / total_nodes + (1 - alpha) * node_page_rank
    print(make_output(nodename, node_page_rank, node_neighbours))
