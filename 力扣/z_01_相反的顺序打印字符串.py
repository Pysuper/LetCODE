# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/8 上午10:33
# @Author  : Zheng Xingtao
# @File    : z_01_相反的顺序打印字符串.py
word = "Hello Word!"


def func(length):
    """
    通过递归, 以相反的顺序打印字符串
    :param length: 字符串的长度
    :return: 相反顺序的字符串
    """
    if length == 0:  # 当变量的长度是0时，返回
        return ''
    else:  # 否则返回字符串的位置向后移1位，直到变量的长度为0
        return word[length - 1] + func(length - 1)


result = func(len(word))
print(result)
