#!/usr/bin/python3
for i in range(0, 8):
    for j in range(i+1, 10):
        print("{:0>2d}".format(i * 10 + j), end=', ')
print("{:d}".format(89))
