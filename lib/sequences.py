#!/usr/bin/env python3

def print_fibonacci(length):
    fib_list = [0, 1]
    if length == 0:
        print([])
        return
    elif length == 1:
        print([0])
        return
    for i in range(2, length):
        next_num = fib_list[-1] + fib_list[-2]
        fib_list.append(next_num)
    print(fib_list)
    pass