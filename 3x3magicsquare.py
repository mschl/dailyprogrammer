#! /usr/bin/env Python3


def test_one():
    square1 = [8, 1, 6, 3, 5, 7, 4, 9, 2]
    square2 = [2, 7, 6, 9, 5, 1, 4, 3, 8]
    square3 = [3, 5, 7, 8, 1, 6, 4, 9, 2]
    square4 = [8, 1, 6, 7, 5, 3, 4, 9, 2]
    square5 = [9, 9]

    print(is_magicsquare(square1))
    print(is_magicsquare(square2))
    print(is_magicsquare(square3))
    print(is_magicsquare(square4))
    print(is_magicsquare(square5))


def is_magicsquare(square):
    if len(square) % 3 != 0:
        return('This is not a valid magic square')
    else:
        if checkRows(square) & checkColumns(square) & checkDiagonals(square):
            return(True)
        else:
            return(False)


def checkRows(square):
    if is_rowfifteen(square[:3]) & is_rowfifteen(square[3:6]) & \
            is_rowfifteen(square[6:]):
        return(True)
    else:
        return(False)


def checkColumns(square):
    column1 = [square[0], square[3], square[6]]
    column2 = [square[1], square[4], square[7]]
    column3 = [square[2], square[5], square[8]]

    if is_rowfifteen(column1) & is_rowfifteen(column2) & is_rowfifteen(column3):
        return(True)
    else:
        return(False)


def checkDiagonals(square):
        diagonal1 = [square[0], square[4], square[8]]
        diagonal2 = [square[6], square[4], square[2]]

        if is_rowfifteen(diagonal1) & is_rowfifteen(diagonal2):
            return(True)
        else:
            return(False)


def is_rowfifteen(row):
    x = 0

    for i in row:
        x = x + i

    if x == 15:
        return True
    else:
        return False


if __name__ == '__main__':
    test_one()
