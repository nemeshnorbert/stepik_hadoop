#!/usr/bin/python3
import sys

lastKey = None

for line in sys.stdin:
    key, _ = line.strip().split("\t")
    if lastKey is None:
        lastKey = key
        counter = 1
    elif key == lastKey:
        counter += 1
    else:
        if counter == 1:
            print(lastKey)
        lastKey = key
        counter = 1

if counter == 1:
    print(lastKey)
