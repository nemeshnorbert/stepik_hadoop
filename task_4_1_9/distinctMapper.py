#!/usr/bin/python3
import sys

for line in sys.stdin:
    id_, groups = line.strip().split("\t")
    for group in groups.strip().split(","):
        print("{},{}\t1".format(id_, group))
