#!/usr/bin/python3
import sys

lastKey = None

for line in sys.stdin:
    key, group = line.strip().split("\t")
    if key != lastKey:
        lastKey = key
    else:
        print(key)
