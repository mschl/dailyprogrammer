#!/usr/bin/env python3


def print_multiplication_table(n):
    x = 1
    while x <= n:
        i = 1
        while i < n:
            print(x, '*', i, '=', x * i)
            i = i + 1
        print(x, '*', i, '=', x * i)
        x = x + 1

print_multiplication_table(5)
print('---------------------')
print_multiplication_table(2)
print('---------------------')
print_multiplication_table(3)
