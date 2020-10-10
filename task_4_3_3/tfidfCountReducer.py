#!/usr/bin/python3
import sys


def print_output(key, count):
    word, docname = key.split("#")
    print("{}\t{}\t{}".format(word, docname, count))


last_key = None

counter = 0

for line in sys.stdin:
    key, count = line.strip().split("\t")
    if last_key is None:
        last_key = key
        counter += int(count)
    elif last_key == key:
        counter += int(count)
    else:
        print_output(last_key, counter)
        last_key = key
        counter = int(count)

print_output(last_key, counter)
