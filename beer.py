#!/usr/bin/env python3
"""
Mmmmm Beer
"""

import fileinput
import itertools

def roundrobin(*iterables):
    "roundrobin('ABC', 'D', 'EF') --> A D E B F C"
    # Recipe credited to George Sakkis
    pending = len(iterables)
    nexts = itertools.cycle(iter(it).__next__ for it in iterables)
    while pending:
        try:
            for _next in nexts:
                yield _next()
        except StopIteration:
            pending -= 1
            nexts = itertools.cycle(itertools.islice(nexts, pending))

def mmmm_beer(line):
    """
    Thanks for the beer mugs Thumbtack
    """
    digits = line.split()
    answer = float(digits.pop())
    digit_ops = [
        ['+', '-', '*', '/']
        for _ in range(len(digits) - 1)
    ]
    for ops in itertools.product(*digit_ops):
        op_string = ' '.join(roundrobin(digits, ops))
        total = float(eval(op_string))
        if total == answer:
            return op_string
    return 'Invalid'


if __name__ == '__main__':
    for line in fileinput.input():
        print(mmmm_beer(line))

# vim: set ft=python ts=4 sw=4 et sts=4 ai :
