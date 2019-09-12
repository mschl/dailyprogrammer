#!/usr/bin/env python3

'''
File: 5-encrypted-password.py
Author: Matthew Schloepp
Description: A password protected login. Use a 'users.txt' file with passwords.
Encrypt passwords in the file.
'''

import getpass
import hashlib


def main():
    """
    The Main Portion of the program
    """

    username = getpass.getuser()
    password = getpass.getpass()

    print(username, '\n', password)


if __name__ == '__main__':
    main()


"""
Incomplete: Maybe I'll do it some other time.
"""
