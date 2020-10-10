#!/usr/bin/python3
import sys

for line in sys.stdin:
    id_, name, url = line.strip().split("\t")
    print(url)
