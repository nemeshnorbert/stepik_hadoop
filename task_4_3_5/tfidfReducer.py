#!/usr/bin/python3
import sys
import itertools


def key_getter(line):
    key, _ = line.strip().split("\t")
    return key


def groupper(stream):
    for key, group in itertools.groupby(stream, key=key_getter):
        yield key, group


def make_output(word, docname, tf, count):
    return "{}#{}\t{}\t{}".format(word, docname, tf, count)


for word, lines in groupper(sys.stdin):
    values = []
    for line in lines:
        _, value = line.split("\t")
        docname, tf, count = value.split(";")
        values.append((docname, tf, count))
    word_count_in_corpus = len(list(values))
    for docname, tf, count in values:
        print(make_output(word, docname, tf, word_count_in_corpus))
