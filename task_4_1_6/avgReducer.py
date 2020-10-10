#!/usr/bin/python3
import sys

lastKey, total, count = None, 0, 0

for line in sys.stdin:
    url, time = line.strip().split("\t")
    if lastKey is None:
        lastKey, total, count = url, int(time), 1
    elif lastKey == url:
        total += int(time)
        count += 1
    else:
        print("{0}\t{1}".format(lastKey, total // count))
        lastKey, total, count = url, int(time), 1

print("{0}\t{1}".format(lastKey, total // count))
