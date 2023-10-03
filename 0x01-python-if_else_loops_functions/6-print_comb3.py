#!/usr/bin/python3
for i in range(0, 8):
    for j in range(i+1, 10):
        print(f"{(i * 10 + j):0>2d}", end=', ')
print(89)
