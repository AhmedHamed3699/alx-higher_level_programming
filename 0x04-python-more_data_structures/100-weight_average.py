#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    acc = 0
    tot_w = 0
    for i in my_list:
        acc += i[0] * i[1]
        tot_w += i[1]
    return acc/tot_w
