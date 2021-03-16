#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# FileName ：z_n_01_冒泡排序.py
# Author   ：zheng xingtao
# Date     ：2021/3/16 14:04

"""
时间复杂度：最差情况下, 只要高阶项，不要低阶项，不要高阶项的系数（操作的次数表达式）
评价一个算法的好坏，先看时间复杂度的指标，然后再看系数（越小越好）


二分搜索：O(log N), log默认以2为底
外排：谁小，移动谁

冒泡排序的第一次排序就会把最大的数，丢到最后

# https://www.kuangstudy.com/bbs/1358674993168363522
"""


class BubbleSort(object):
    def sorted(self, arr):
        """
        冒泡排序
        时间复杂度为 O(N^2), 额外空间复杂度O(1)
        :param arr: 无序列表
        :return: 排序后的列表
        """
        if len(arr) > 2 or arr is not None:
            for i in range(len(arr) - 1):
                for j in range(len(arr) - i - 1):
                    # 每次选择最大的，放在最后
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print(arr)


list_ = [2, 4, 3, 5, 7, 6, 9, 8]
sort_arr = BubbleSort().sorted(list_)

"""
固定时间的操作，都是O(1)
时间复杂度：an^2 + bN + 1 ==> O(N^2)
"""
