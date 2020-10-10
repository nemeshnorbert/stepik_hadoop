#!/usr/bin/python3
import sys

for line in sys.stdin:
    id_, group = line.strip().split(",")
    print("{0}\t1".format(group))
