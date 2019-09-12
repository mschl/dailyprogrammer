#!/usr/bin/env python3


def bigger(a, b):
    if a > b:
        return(a)
    else:
        return(b)


def biggest(a, b, c):
    return(bigger(a, b), c)


def smaller(a, b):
    if a < b:
        return a
    else:
        return b


def median(a, b, c):
    return(smaller(bigger(a, b), c))


print(median(1, 2, 3))
print(median(9, 3, 6))
print(median(7, 8, 7))
