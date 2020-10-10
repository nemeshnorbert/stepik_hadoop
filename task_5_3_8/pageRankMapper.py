#!/usr/bin/python3
import sys


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


for line in sys.stdin:
    line = line.strip()
    nodename, page_rank, neighbours = parse_line(line)
    print(line)
    assert(len(neighbours) > 0)
    odds = page_rank / len(neighbours)
    for neighbour in neighbours:
        print(make_output(neighbour, odds, []))
