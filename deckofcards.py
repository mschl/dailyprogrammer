#! /usr/bin/env Python3

suits = ['Spades', 'Clubs', 'Hearts', 'Diamonds']

cards = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
         'Ten', 'Jack', 'Queen', 'King', 'Ace']

deck = [[]]
x = 0
for i in cards:
    deck.append(i[])
    for z in suits:
        deck[x].append(suits)
    print(i)
    x = x + 1

print(deck)
