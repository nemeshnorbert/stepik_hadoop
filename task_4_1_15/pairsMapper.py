#!/usr/bin/python3
import sys

for line in sys.stdin:
    groups = line.strip().split(" ")
    n = len(groups)
    for i in range(n):
        stripe = {}
        for j in range(n):
            if groups[i] != groups[j]:
                stripe.setdefault(groups[j], 0)
                stripe[groups[j]] += 1
        stripe_format = ','.join([
            '{}:{}'.format(group, stripe[group])
            for group in sorted(stripe)
        ])
        print("{}\t{}".format(groups[i], stripe_format))
