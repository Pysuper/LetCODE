# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/22 22:20
# @Author  : Zheng Xingtao
# @File    : z_n_02_特殊的栈.py

"""
实现一个特殊的栈，在实现栈的基本功能的基础上，再实现返回栈中最小元素的操作。
【要求】
1．pop、push、getMin操作的时间复杂度都是O(1)。
2．设计的栈类型可以使用现成的栈结构。
"""


class MyStack:
    """
    使用两个栈：data、min
    data和min同时压栈
    data中进行正常的压栈操作
    min中：
        第一个值，min和data一样操作
        后面的：
            如果值>=min中的栈顶，则在min的栈中在加一个min的栈顶，赋值一个一样的
            如果值< min中的栈顶，就在min中加入这个值
    最后返回的时候，从两个栈中，同时返回
    那么就能在min中直接获取到data中的最小值了
    """

    def __init__(self):
        self.stack_data = []
        self.stack_min = []

    def push(self, num: int):
        if len(self.stack_min) == 0:
            # 如果栈为空，则直接添加一个值
            self.stack_min.append(num)

        elif num < self.stack_min[len(self.stack_min) - 1]:
            # 如果新进来的值，比min栈中的栈顶还要小
            self.stack_min.append(num)
        else:
            # min栈中的栈顶更小,重复压入这个栈顶
            self.stack_min.append(self.stack_min[len(self.stack_min) - 1])

        # data栈中直接添加这个数
        self.stack_data.append(num)

    def pop(self):
        if len(self.stack_data) == 0:
            raise IndexError
        self.stack_min.pop()
        return self.stack_data.pop()

    def get_min(self):
        if len(self.stack_min) == 0:
            raise IndexError

        # 返回min栈的栈顶
        return self.stack_min[self.stack_min[len(self.stack_min) - 1]]