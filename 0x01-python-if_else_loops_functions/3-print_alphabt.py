#!/usr/bin/python3
for i in range(97, 127):
    if i == 101 and i == 113:
        continue
    else:
        char = chr(i)
        print("{leter}".format(letter=char), end="")
 