#!/usr/bin/env python3


def factoral(n):
    combinations = 1
    while n >= 1:
        combinations = combinations * n
        n = n - 1
    return(combinations)


print(factoral(7))
print(factoral(4))
print(factoral(52))
