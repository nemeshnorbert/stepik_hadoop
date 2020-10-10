#!/usr/bin/python3
import sys

current_user_id, groups = None, set()

counter = {}

for line in sys.stdin:
    user_id, group = line.strip().split("\t")
    if current_user_id is None:
        current_user_id = user_id
        groups.add(group)
    elif current_user_id == user_id:
        groups.add(group)
    else:
        for grp in groups:
            counter.setdefault(grp, 0)
            counter[grp] += 1
        current_user_id = user_id
        groups.clear()
        groups.add(group)

for grp in groups:
    counter.setdefault(grp, 0)
    counter[grp] += 1

for grp, count in counter.items():
    print("{}\t{}".format(grp, count))
