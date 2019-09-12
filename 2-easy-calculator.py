#!/usr/bin/env python3

import math
from decimal import Decimal

'''
File: 2-easy-calculator.py
Author: Matthew Schloepp
Description: Reddit's /r/DailyProgrammer 2nd easy challenge. Create a calculator
that you can use. Bonus: Have multiple functions.

I'm going to create a simple interest, compound annual interest calculator, and
maybe a quarterly compound interest calculator.

'''


def main():
    selection = getSelection()
    if selection == "1":
        p = float(input("How much money are you starting with? "))
        r = .01 * float(input("What is your annual interest rate? "))
        t = float(input("How many years will you let it sit? "))

        print(simpleInterest(p, r, t))
    elif selection == "2":
        p = float(input("How much money are you starting with? "))
        r = .01 * float(input("What is your annual interest rate? "))
        t = float(input("How many years will you let it sit? "))
        n = float(input("How many times is interest compounded per year? "))

        print(annualCompoundInterest(p, r, t, n))
    elif selection == "3":
        quarterlyCompoundInterest()
    elif selection.lower() == "q":
        print("Thank you!")
    else:
        print("You need to select one of the numbers!")

    return()


def simpleInterest(p, r, t):
    # A = P(1 + rt)
    return(p*(1.00+r*t))


def annualCompoundInterest(p, r, t, n):
    # A = P(1 + r/n) ^ nt
    return(round(p * (1 + r / n) ** (n*t), 2))


def quarterlyCompoundInterest():
    print("This feature is incomplete. Sorry.")


def getSelection():
    print(
        """
        1.) Simple Interest Calculator.
        2.) Annual Compound Interest Calculator.
        3.) Quarterly Compound Interest Calculator.\n
        Enter 'Q' to Quit\n
        """
    )
    selection = input("Enter number: ")
    return(selection)


if __name__ == '__main__':
    main()
