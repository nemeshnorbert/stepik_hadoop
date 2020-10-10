#!/usr/bin/python3
import sys

key, total = None, 0

for line in sys.stdin:
    k, value = line.strip().split("\t")
    if key is None:
        key, total = k, int(value)
    elif k == key:
        total += int(value)
    else:
        print("{0}\t{1}".format(key, total))
        key, total = k, int(value)

print("{0}\t{1}".format(key, total))
