#!/usr/bin/python3
'''
this is a python program to compute the minimum number of processes required
to create a certain number of characters.
'''


def minOperations(n):

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
