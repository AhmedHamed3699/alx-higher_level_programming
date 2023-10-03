#!/usr/bin/python3
def uppercase(str):
    tmp = ''
    for c in str:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            tmp += chr(ord(c) - 32)
        else:
            tmp += c
    print(tmp)
