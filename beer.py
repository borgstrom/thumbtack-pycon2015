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
    original_digits = line.split()
    answer = float(original_digits.pop())
    digit_ops = [
        ['+', '-', '*', '/']
        for _ in range(len(original_digits) - 1)
    ]
    solutions_tried = 0
    for digits in itertools.permutations(original_digits):
        for ops in itertools.product(*digit_ops):
            op_string = ' '.join(roundrobin(digits, ops))
            total = float(eval(op_string))
            solutions_tried += 1
            if total == answer:
                return '{0} = {1}  ({2} solutions tried)'.format(op_string, int(answer), solutions_tried)
    return 'Invalid'


if __name__ == '__main__':
    for line in fileinput.input():
        print(mmmm_beer(line))

# vim: set ft=python ts=4 sw=4 et sts=4 ai :
