#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# FileName ：z_n_03_插入排序.py
# Author   ：zheng xingtao
# Date     ：2021/3/16 15:39


def insert_sort(arr: []):
    """
    插入排序：（选择排序、冒泡排序是不考虑数列情况的，是否有排序）
        最好情况
        最差情况
        平均情况, 都按照最差的情况来算 O(N^2)
    """
    if len(arr) > 2 or arr is not None:

        # 这里从第2个数开始（index=1）, 0~i-1上已经有序
        for i in range(1, len(arr)):

            # 第二个循环，是向前比较
            index = i
            while index > 0 and arr[index - 1] > arr[i]:
                # 如果index > 0， 当前数一直向前比较
                # 如果前一个数比当前数大，则交换
                # 同事index - 1
                arr[index], arr[index - 1] = arr[index - 1], arr[index]
                index -= 1
    return arr


list_ = [2, 4, 3, 5, 7, 6, 9, 8]
arr = insert_sort(list_)
print(arr)
