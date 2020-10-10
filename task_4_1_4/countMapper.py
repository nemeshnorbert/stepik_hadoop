#!/usr/bin/python3
import sys

counter = {}
for line in sys.stdin:
    for word in line.strip().split(" "):
        counter.setdefault(word, 0)
        counter[word] += 1
    for word, count in counter.items():
        print("{0}\t{1}".format(word, count))
    counter.clear()
