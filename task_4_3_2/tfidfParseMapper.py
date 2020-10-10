#!/usr/bin/python3
import sys
import re


for line in sys.stdin:
    docname, text = line.strip().split(":", 1)
    text = re.sub(r'[^a-zA-Z0-9]', ' ', text)
    for word in text.strip().split(" "):
        if word:
            print("{0}#{1}\t1".format(word, docname))
