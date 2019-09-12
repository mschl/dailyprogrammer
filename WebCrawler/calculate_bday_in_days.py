#!/usr/bin/env python3

"""
Take input of birthday and output the current age in days for the current date.

second date must not be less than first date

must use gregorian calendar (15 Oct 1582)
"""


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    days = 0
    if (year1, month1, day1) > (year2, month2, day2):
        return('undefined')
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days = days + 1

    return(days)


def nextDay(year, month, day):
    """  This procedure incorrectyly assumes all months have 30 days """
    if day < 30:
        return(year, month, day + 1)
    else:
        if month < 12:
            return(year, month + 1, 1)
        else:
            return(year + 1, 1, 1)


def dateIsBefore(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False


print(daysBetweenDates(2012, 12, 7, 2012, 12, 7))  # should return '0'
print(daysBetweenDates(2012, 12, 7, 2012, 12, 8))  # should return '1'
print(daysBetweenDates(2012, 11, 2, 2012, 12, 9))  # should return '37'
print(daysBetweenDates(2012, 1, 1, 2012, 12, 30))  # should return '360'
print(daysBetweenDates(2012, 12, 8, 2012, 12, 7))  # should return undefined
print(daysBetweenDates(2012, 6, 29, 2013, 6, 29))  # should return 365
print(daysBetweenDates(2012, 6, 29, 2013, 6, 31))  # should return undefined
