# -*- coding: utf-8 -*-

def operate_red(num, x):
    next_red = num
    curr_blue = num * x
    return (next_red, curr_blue)


def operate_blue(num, y):
    next_red = num
    next_blue = num * y
    return (next_red, next_blue)


n, x, y = [int(v) for v in input().split()]

red_stone = 1
blue_stone = 0
for lank in reversed(range(2, n + 1)):
    next_red1, curr_blue = operate_red(red_stone, x)
    blue_stone += curr_blue
    next_red2, next_blue = operate_blue(blue_stone, y)

    red_stone = next_red1 + next_red2
    blue_stone = next_blue

print(blue_stone)

