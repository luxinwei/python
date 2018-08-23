# -*- coding:utf-8 -*-

# 演示数字猜谜游戏
import sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

number = 7
guess = -1

print("数字猜谜游戏！")
while guess != number:
    guess = int(input("请输入你要猜的数字："))

    if guess == number:
        print("恭喜你，猜对了！")
    elif guess < number:
        print("猜的数字小了...")
    elif guess > number:
        print("猜的数字大了...")



