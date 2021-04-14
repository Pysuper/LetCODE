# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/22 21:17
# @Author  : Zheng Xingtao
# @File    : z_n_01_队列和栈.py

class ArrayStack:
    """固定数组实现栈-先进后出"""

    def __init__(self, init_size):
        if init_size < 0:
            raise IndexError
        # self.arr = [0] * init_size
        self.arr = []
        self.index = 0
        self.init_size = init_size

    def peek(self):
        # 返回栈顶
        if self.index == 0:
            return None
        return self.arr[self.index - 1]

    def push(self, num: int):
        # if self.index == len(self.arr):
        if self.index == self.init_size:
            raise IndexError
        # self.arr[self.index] = num
        self.arr.append(num)
        self.index += 1
        return self.arr

    def pop(self):
        if self.index == 0:
            raise IndexError("超出索引范围")
        result = self.arr[self.index]
        self.index -= 1
        return result


result = ArrayStack(3).push(2)
print(result)


class ArrayQueue:
    """
    固定数组实现队列-先进先出：
        - 设置start、end都指向0位置
            - start：如果要拿取一个数，应该拿哪个位置上的数
            - end：如果新加一个数，应该把这个数填到哪个位置上
        - 单独设置一个size变量，来约束start、end
            - 如果数组长度为3,：
                - 如果size < 3, 新增一个数，就把这个数放在end的位置上，size -= 1
                - 只要end > 3，end就跳回到0
                - 如果size!= 0，总把start位置上的数，拿给用户，size += 1
        - 当size=0， 或者size=3的时候，就报错，不能取，不能放了
    """

    def __init__(self, init_size):
        if init_size < 0:
            raise IndexError
        self.arr = [0] * init_size
        self.end = 0
        self.size = 0  # size：目的是让end、start解耦
        self.start = 0
        self.init_size = init_size

    def peek(self):
        if self.init_size == 0:
            return None
        return self.arr[self.start]

    def push(self, num):
        """向队列中添加一个数"""
        if self.size == len(self.arr):
            # 如果size == len(arr)，则不能再向其中添加数据了
            raise IndexError

        # size != len(arr): 可以继续添加数据
        self.size += 1
        self.arr[self.end] = num  # 新添加的数放在最后一个的位置上

        if self.end == len(self.arr) - 1:
            # 如果end已经来到最后一个位置了，跳回到0
            self.end = 0
        else:
            # 否则继续向下走：end += 1
            self.end += 1
        return self.arr

    def poll(self):
        """从队列中拿走一个数"""
        if self.size == 0:
            # 队列中已经没有数了
            raise IndexError

        # 队列中还有数，拿走一个数，size -= 1
        self.size -= 1

        # 用tmp记录start的位置 ==> 拿走一个值之后，需要调整start的位置
        tmp = self.start

        if self.start == len(self.arr) - 1:
            # 如果start来到最后一个位置，start=0
            self.start = 0
        else:
            # 否则start继续向后走
            self.start += 1
        return self.arr[tmp]


result = ArrayQueue(3).push(1)
print(result)
