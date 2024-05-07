#!/usr/bin/python3
""" H => Copy All => Paste => HH => Paste =>HHH => Copy All =>... """


def minOperations(n):
    """ H => Copy All =>Paste=>HH=>Paste=>HHH=>Copy All=>... """
    if n <= 1:
        return 0

    operations = 0
    current_length = 1
    clipboard = 0

    while current_length < n:
        if n % current_length == 0:
            clipboard = current_length
            operations += 2
        else:
            operations += 1

        current_length += clipboard

    return operations
