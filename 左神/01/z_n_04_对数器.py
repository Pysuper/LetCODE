#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# FileName ：z_n_02_对数器.py
# Author   ：zheng xingtao
# Date     ：2021/2/10 12:27

"""
对数器的用处:
    1. 验证算法是否正确
    2. 使用小样本校验
    3. 证明贪心策略
实现对数器:
    1. 有一个你想要测的方法a
    2. 实现一个绝对正确,但是复杂度不好的方法b
    3. 实现一个随机样本产生器
    4. 实现对比的方法
    5. 把方法a和方法b对比很多次, 来验证方法a是否正确
    6. 如果有一个样本,使得比对出错, 打印样本分析是哪个方法出错
    7. 当样本数量很多时, 比对测试依然正确, 可以确定方法a已经正确
"""

import random


class Logarithm():
    """对数器的实现与使用"""

    def random_(self, size, number):
        """
        生成随机样本, 不同的操作对象, 使用不同样本发生器
        生成长度随机的数组: 数组的长度, 每个值都是随机的
        """
        value = random.randint(0, size)
        # 使用随机数-随机数, 生成 可能为正 可能为负 的数
        return [random.randint(0, number) - random.randint(0, number) for num in range(value)]

    def func_(self, arr):
        """
        写一个 一定正确的方法 , 不考虑时间复杂度
        如果这个方法，还是不能确定是否正确, 也可以:
        测试的时候, 总会有两个结果不一样的时候, 这时候, 在math里面打印错误的数列, 然后校验 func_
        """
        return sorted(arr)

    def math_(self, arr):
        """这里是我们自己写的算法"""
        for i in range(len(arr) - 1):
            for j in range(len(arr) - 1 - i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    def run(self, size, value):
        """
        拿两个一样的数组, 放到绝对正确的方法 和 我们写的算法, 比较两者的输出结果
        如果结果一样, 则说明算法是正确的的, 返回对数器的结果
        """
        succeed = "True"
        for times in range(500000):
            random_list = self.random_(size, value)
            func_arr = self.func_(random_list)
            math_arr = self.math_(random_list)
            if func_arr != math_arr:
                succeed = f"False\r\nfunc_arr:{func_arr}\r\nmath_arr:{math_arr}"
                break
        print(succeed)


Logarithm().run(4, 31)
