#!/usr/bin/env python3

'''
File: 3-easy-password-generator.py
Author: Matthew Schloepp
Description: Simple password generator. Select the amount of passwords you want
to generate and the length of those passwords.
'''

from random import randint


def main():
    """
    Main function.
    """
    i = 0
    passwords = []
    passwordsToGenerate = getPasswordSizes()

    while i < int(passwordsToGenerate[0]):
        passwords.append(generatePassword(int(passwordsToGenerate[1])))
        i += 1

    print('\n'.join(passwords))
    saveToFile('\n'.join(passwords))


def getPasswordSizes():
    """Get input from the user on length and amount of passwords to generate"""

    howMany = input("How many passwords would you like to generate? \n")
    passLength = input("How long should the passwords be? \n")

    return(howMany, passLength)


def generatePassword(passLength=8):
    """Generates and returns password. Takes passLength as arguement: Default
    is 8"""

    i = 0
    password = ''
    while i < passLength:
        password += chr(randint(33, 125))
        i += 1

    return(password)


def saveToFile(passwords, filename="passwords.txt"):
    """
    Save generated passwords to file.
    """
    txtFile = open(filename, 'a')
    txtFile.write(passwords)
    txtFile.write('\n')
    txtFile.close()


if __name__ == '__main__':
    main()
