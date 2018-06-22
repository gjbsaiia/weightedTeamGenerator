import sys
import os
import threading


def readData(filename):
    readdata = []
    file = open(filename)
    lines = file.read().splitlines()
    for line in lines:
        try:
            readdata.append(float(line.split(',')[1]))
        except ValueError:
            print('none')


if __name__ == "__main__":
    readData('auth_amt.csv')