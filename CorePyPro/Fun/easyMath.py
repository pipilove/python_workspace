#!/usr/bin/env python
# coding=gbk
'''
__title__ = '11.2 - 算术游戏'
__author__ = 'pi'
__mtime__ = '2014.10.14'
'''
from operator import add, sub, mul, div
from random import choice, randint

MAX_TRY = 3 - 1
ops = {'+': add, '-': sub, '*': mul, '/': div}
RAND_MAX = 10
RAND_MIN = 0


def doProb():
    op = choice('+-*/')
    nums = [randint(RAND_MIN, RAND_MAX) for i in range(2)]  #产生两个随机操作数
    # nums.sort(reverse=True)
    ans = ops[op](*nums)  #*tuple_grp_nonkw_args

    try_counter = 0
    try:
        while int(input('%d %c %d = ' % (nums[0], op, nums[1]))) != ans:  #raw_input输入的是str
            if try_counter == MAX_TRY:
                print('wrong! the right ans = %d ' % ans)
                return
            print('wrong, try again ... ')
            try_counter += 1
        print('correct!')
        return
    except(KeyboardInterrupt, EOFError, ValueError):
        print('invalid input, input again!')


def main():
    while True:
        doProb()
        try:
            opt = input('try another ? y/n  ').lower()
            if opt and opt[0] == 'n':
            #opt and 为了防止无输入IndexError: string index out of range
                break
        except(KeyboardInterrupt, EOFError):
            break


if __name__ == '__main__':
    main()
