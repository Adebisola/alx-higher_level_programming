#!/usr/bin/python3
for lowerCase in range(97, 123):
    if lowerCase not in [101, 113]:
        print("{}".format(chr(lowerCase)), end="")
