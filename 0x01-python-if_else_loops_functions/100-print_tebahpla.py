#!/usr/bin/python3
for c in range(ord('Z'), ord('A') - 1, -1):
    print("{}".format(chr(c) if c % 2 else chr(c + 32)), end='')
