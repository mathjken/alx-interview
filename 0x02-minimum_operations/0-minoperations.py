#!/usr/bin/python3

""" Minimum Operations """


def minOperations(n):
    """
    In a text file, there is a single character H. Your text editor can execute
    only two operations in this file: Copy All and Paste. Given a number n,
    write a python program that computes the min  no. of operations needed to
    result in exactly n H characters in the file.
    Returns an integer
    If n is impossible to achieve, returns 0
    """
    if not isinstance(n, int):
        return 0

    ops = 0
    i = 2
    while (i <= n):
        if not (n % i):
            n = int(n / i)
            ops += i
            i = 1
        i += 1
    return ops
