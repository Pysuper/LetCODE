#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# FileName ：z_n_01.py
# Author   ：zheng xingtao
# Date     ：2021/2/8 14:53

"""
时间复杂度：只要高阶项，不要低阶项，不要高阶项的系数（操作的次数表达式）
评价一个算法的好坏，先看时间复杂度的指标，然后再看系数（越小越好）


二分搜索：O(log N), log默认以2为底
外排：谁小，移动谁

冒泡排序的第一次排序就会把最大的数，丢到最后

# https://www.kuangstudy.com/bbs/1358674993168363522
"""


def maopao():
    """冒泡排序：时间复杂度为 O(N2)"""
    arr = [2, 5, 7, 8, 1, 4]
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            # 这里是改变前后两个数据的位置
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j],
    print(arr)


def xuanze():
    """选择排序：时间复杂度为 O(N2)"""
    arr = [2, 5, 7, 8, 1, 4]
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            # 这里是修改指定下标的数据
            if arr[j] < arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
    print(arr)

# TODO：在工程上已经很少能见到了，插入排序还有用，而且用处比较大
def charu():
    """插入排序："""
    arr = [2, 5, 7, 8, 1, 4]
    for i in range(1, len(arr) - 1):
        pass


xuanze()
