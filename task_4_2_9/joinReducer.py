#!/usr/bin/python3
import sys


def parse_info(info):
    return info.split(':')


def add_to_report(report, group, content):
    assert(group in ('query', 'url'))
    report[group].append(content)


def print_output(user, report):
    for query in report['query']:
        for url in report['url']:
            print("{}\t{}\t{}".format(user, query, url))


def clear_report(report):
    report['url'].clear()
    report['query'].clear()


last_user = None
report = {'url': [], 'query': []}


for line in sys.stdin:
    user, info = line.strip().split("\t")
    if last_user is None:
        last_user = user
    elif user != last_user:
        print_output(last_user, report)
        last_user = user
        clear_report(report)
    add_to_report(report, *parse_info(info))


print_output(last_user, report)
