#!/usr/bin/python3
import sys


for line in sys.stdin:
    word, docname, tf = line.strip().split("\t")
    print("{}\t{};{};{}".format(word, docname, tf, 1))
