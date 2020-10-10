#!/usr/bin/python3
import sys

for line in sys.stdin:
    for word in line.strip().split(" "):
        if word:
            print(word + "\t1")
