#!/usr/bin/python3
def uniq_add(my_list=[]):
    tmp_set = set()
    sum = 0
    for i in my_list:
        if i not in tmp_set:
            tmp_set.add(i)
            sum += i
    return sum
