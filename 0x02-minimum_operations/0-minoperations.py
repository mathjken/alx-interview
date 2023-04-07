#!/usr/bin/python3
'''
this is a python program to compute the minimum number of processes required
to create a certain number of characters.
'''



def minOperations(n):
    x = 0

    if n <= 1:
        return x

    for i in range(2, n + 1):
        while (0 == n % i):
            x = x + i
            n = n / i
            if n < i:
                break
    return x
