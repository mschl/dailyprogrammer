#!/usr/bin/env python3
import argparse


def main():
    """The programs meat and potatos. This is the main function"""
    interactiveMode()


def interactiveMode():
    """This is interactive mode for encrypting and decrypting strings."""
    msg = input("What message would like like to (e)ncrypt or (d)ecrypt? \n")
    shift = int(input("Pick a shift value 1-25: "))

    selc = input("Select E to (E)ncrypt or D to (D)ecrypt: ").upper()

    if (shift < 25) or (shift > 1):
        if selc == "E":
            encryptString(msg, shift)
        elif selc == "D":
            decryptString(msg, shift)
        else:
            print("""You need to type 'E' or 'D'!\n
                  I will encrypt your message\n""")
    else:
        print("""
              Your value is not within the guidelines. \n Closing...
              """)


def encryptString(msg, shift=13):
    """
    encryptString rotational cypher to encrypt message, default cipher is
    rot1113
    """
    newMsg = []
    for char in msg:
        newMsg.append(shiftChar(char, shift))

    print(''.join(newMsg))


def decryptString(msg, shift=13):
    """decryptString() rotational cypher to decrypt message, default cypher
    rot13"""
    newMsg = []
    for char in msg:
        newMsg.append(shiftChar(char, (shift * -1)))

    print(''.join(newMsg))


def shiftChar(char, shift):
    """
    Uses the rotational cipher to change character value to encrypted value
    and returns the encrypted character.
    """
    if (ord(char) >= 97) and (ord(char) <= 122):
        if ((ord(char) + shift) <= 122) and ((ord(char) + shift) >= 97):
            return(str(chr(ord(char) + shift)))
        elif (ord(char) + shift) > 122:
            shift = ((ord(char) + shift) - 122)
            return(str(chr(96 + shift)))
        elif (ord(char) + shift) < 97:
            shift = ((ord(char) + shift) - 97)
            return(str(chr(123 + shift)))
    elif (ord(char) >= 65) and (ord(char) <= 90):
        if ((ord(char) + shift) <= 90) and ((ord(char) + shift) >= 65):
            char = str(chr(ord(char) + shift))
            return(char)
        elif (ord(char) + shift) > 90:
            shift = ((ord(char) + shift) - 90)
            char = str(chr(64 + shift))
            return(char)
        elif (ord(char) + shift) < 65:
            shift = ((ord(char) + shift) - 65)
            char = str(chr(91+shift))
            return(char)
    else:
        return(char)

if __name__ == '__main__':
    main()
