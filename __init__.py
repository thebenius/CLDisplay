#!/usr/bin/env python3

import math


class BetterDisplay:

    def __init__(self):
        self.showBar = False
        self.barValue = 0

    def __del__(self):
        print()

    def activateBar(self):
        self.showBar = True

    def deactivateBar(self):
        if self.showBar:
            print('\r',end='')
            print(' '*107,end='')
            print('\r', end='')
        self.showBar = False

    def copyBar(self):
        if self.showBar:
            print()

    def print(self, msg):
        if self.showBar:
            print('\r',end='')
            print(' '*107,end='')
            print('\r', end='')
        print(msg)
        if self.showBar:
            self.setBar()


    def setBar(self, value=None):

        if (value==None):
            value = self.barValue

        self.barValue = value

        if (value>100 or value < 0):
            raise ValueError
        value = math.floor(value)

        print('\r',end='')
        print('[',end='')
        for _ in range(value):
            print("=", end='')
        for _ in range(value+1,101):
            print("-",end='')
        print(f"] {value}%",end='')


if __name__ == "__main__":
    import time

    display = BetterDisplay()
    display.activateBar()

    for i in range(20):
        display.print(f"This is value {i}")
        display.setBar(i)
        if i==10:
            display.copyBar()
        time.sleep(0.1)

    display.copyBar()
    display.deactivateBar()

    print("Test")

