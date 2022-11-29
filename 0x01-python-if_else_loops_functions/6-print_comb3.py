#!/usr/bin/python3
for i in range(10):
    for j in range(i+1, 10):
        if i == 8 and j == 9:
            print("{1}{0}".format(j, i))
        else:
            print("{}{}".format(i, j), end=", ")
