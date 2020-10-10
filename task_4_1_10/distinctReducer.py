#!/usr/bin/python3
import sys

lastKey = None

for line in sys.stdin:
    key, _ = line.strip().split("\t")
    if lastKey != key:
        lastKey = key
        print("{0}".format(lastKey))
