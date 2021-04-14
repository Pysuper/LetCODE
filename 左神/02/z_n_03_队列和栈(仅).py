# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/22 22:27
# @Author  : Zheng Xingtao
# @File    : z_n_03_队列和栈(仅).py

"""
如何仅用队列结构实现栈结构？
如何仅用栈结构实现队列结构？
"""


class QueueStack:
    """
    使用两个队列data、heap
    data队列记录数据
    需要返回数据的时候：
        把data队列中的其他数据放入heap队列中，只留最后一个数
        把data队列中的值拿出来
        再调换data队列和heap队列的引用
    """

    def __init__(self):
        pass


class StackQueue:
    """
    使用两个栈：push、pop
    所有进来的数都放在push栈中，取数的时候都从pop栈中获取
    push中放了进来的数之后，全部倒入pop栈中：
        一次性必须全部倒完，否则pop栈获取数据的时候，获取的值不对
        pop栈中有数据的时候，一定不能想pop栈中倒入数据，否则pop中数据的顺序就乱了
    """

    def __init__(self):
        pass
