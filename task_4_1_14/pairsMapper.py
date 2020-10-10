#!/usr/bin/python3
import sys

for line in sys.stdin:
    groups = line.strip().split(" ")
    n = len(groups)
    for i in range(n):
        for j in range(n):
            if groups[i] != groups[j]:
                print("{},{}\t1".format(groups[i], groups[j]))
