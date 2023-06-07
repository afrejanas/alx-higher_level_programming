#!/usr/bin/python3
k = 0
for i in range(0, 10):
    k = k + 1
    for j in range(k, 10):
        if i == 8 and j == 9:
            print("{:d}{:d}".format(i, j))
        else:
            print("{:d}{:d}, ".format(i, j), end='')

