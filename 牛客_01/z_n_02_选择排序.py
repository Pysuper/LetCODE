#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# FileName ：z_n_02_选择排序.py
# Author   ：zheng xingtao
# Date     ：2021/3/16 14:27


def selection_sort(arr: []):
    """
    选择排序，主要是记录最小值的缩影
    :param arr: 无序数列
    :return: 有序数列
    """
    if len(arr) > 2 or arr is not None:
        # for i in range(len(arr) - 1):
        for i in range(len(arr)):
            min_index = i

            # 重点：从头部开始，尾部不动 ==> 过程中i不变，j增加
            for j in range(i + 1, len(arr)):
                # 每一次都找到最小的，替换min_index，最后替换最小值和当前i的数值
                # if arr[j] < arr[min_index]:
                #     min_index = j
                min_index = j if arr[j] < arr[min_index] else min_index
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


list_ = [2, 4, 3, 5, 7, 6, 9, 8]
arr = selection_sort(list_)
print(arr)
