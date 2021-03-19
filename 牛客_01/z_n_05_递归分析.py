#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# FileName ：z_n_03_递归分析.py
# Author   ：zheng xingtao
# Date     ：2021/2/10 13:51

"""
使用递归的方式, 在一个数组中找最大值
找左边的最大值, 再找右边的最大值, 这两个最大的数据, 就是最大值 ==> 分治

递归函数的时间复杂度：
    子问题规模一样的时候，使用master公式推理时间复杂度
    只分析父问题到子问题的这一步
"""


class GetMax(object):
    def get_max(self, arr: list, L: int, R: int):
        """
        无限的缩小, 把大问题 化解 成小问题
        递归要有终止条件
        这个方法里面, 数组自己没有发生变化, 是取值的索引一直在变
        :param arr: 数组本身
        :param L: 左边界
        :param R: 右边界
        :return:
        """
        # 终止条件
        if L == R:
            return arr[L]

        # 程序会帮我们实现压栈
        # 一个函数调用子过程之前,会把自己的所有过程全部压到 栈 中, 信息完全保存,
        # 子过程返回之后, 会利用这些信息,彻底还原现场.继续执行了
        # 就这样完成子过程和父过程的通信
        #
        # TODO: ==> 任何非递归行为都可以改为递归
        mid = int((L + R) / 2)
        max_left = self.get_max(arr, L, mid)
        max_right = self.get_max(arr, mid + 1, R)
        return max(max_left, max_right)


arr = [2, 5, 3, 6]
max_num = GetMax().get_max(arr, 0, len(arr) - 1)
print(max_num)
