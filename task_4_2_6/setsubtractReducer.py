#!/usr/bin/python3
import sys

lastKey, lastGroup = None, None

for line in sys.stdin:
    key, group = line.strip().split("\t")
    if lastKey is None:
        lastKey = key
        lastGroup = group
        counter = 1
    elif key == lastKey:
        counter += 1
    else:
        if counter == 1 and lastGroup == 'A':
            print(lastKey)
        lastKey = key
        lastGroup = group
        counter = 1

if counter == 1 and lastGroup == 'A':
    print(lastKey)
