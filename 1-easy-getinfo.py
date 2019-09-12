#!/usr/bin/env python3

'''
File: 1-easy-getinfo.py
Author: Matthew Schloepp
Description: The first challenge from http://www.reddit.com/r/dailyprogrammer.

Ask a user for the name, reddit username, and age and return it in a string:
    "your name is (blank), you are (blank) years old, and your username is
    (blank)"

Bonus: Save the information to a file.

'''


name = input("What is your name? ")
age = input("How old are you? ")
username = input("What is your reddit username? ")

print("your name is %s, you are %s years old, and your username is %s" %
      (name, age, username))

filename = open("userlog.txt", 'a')

lastuser = "%r, %r, %r\n" % (name, age, username)

filename.write(lastuser)
filename.close()
