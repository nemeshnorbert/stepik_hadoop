#!/usr/bin/python3
import sys

for line in sys.stdin:
    id_, name, url = line.strip().split("\t")
    if name == 'user10':
        print(line, end='')
