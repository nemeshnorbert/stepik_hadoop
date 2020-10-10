#!/usr/bin/python3
import sys

lastKey, total, counter = None, 0, 0

for line in sys.stdin:
    url, time_count = line.strip().split("\t")
    time, count = time_count.split(";")
    if lastKey is None:
        lastKey, total, counter = url, int(time), int(count)
    elif lastKey == url:
        total += int(time)
        counter += int(count)
    else:
        print("{0}\t{1};{2}".format(lastKey, total, counter))
        lastKey, total, counter = url, int(time), int(count)

print("{0}\t{1};{2}".format(lastKey, total, counter))
