#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# FileName ：z_n_07_随机快排.py
# Author   ：zheng xingtao
# Date     ：2021/3/19 11:12

class HeLanGuoQi(object):
    """荷兰国旗问题"""

    def partition(self, arr: list, num: int):
        cur = 1
        less = - 1
        more = len(arr) - 1 + 1
        while cur < more:
            if arr[cur] < num:
                arr[less], arr[cur] = arr[cur], arr[less]
                less += 1
                cur += 1
            elif arr[cur] > num:
                arr[more], arr[cur] = arr[cur], arr[more]
                more -= 1
                # cur -= 1 # TODO: 注意这里cur不动
            else:
                cur += 1

        # 返回等与区域的左边界和右边界
        return [less + 1, more - 1]


# list_ = [1, 2, 3, 4, 3]
# HeLanGuoQi().partition(list_, 3)


class QuickSort(object):
    """
    快排
        经典快排
        随机快排
    """

    def run(self, arr: list):
        if arr is None or len(arr) < 2:
            return
        self.quick_sort(arr, 0, len(arr) - 1)

    def quick_sort(self, arr, L, R):
        p = self.partition(arr, L, R)
        self.quick_sort(arr, L, p[0] - 1)
        self.quick_sort(arr, p[0] - 1, R)

    def partition(self, arr: list, L: int, R: int):
        less = L - 1
        more = R
        while L < more:
            if arr[L] < arr[R]:
                arr[less], arr[R] = arr[R], arr[less],
                less += 1
                L += 1
            elif arr[L] > arr[R]:
                arr[more], arr[R] = arr[R], arr[more]
                more -= 1
            else:
                L += 1
            arr[more], arr[R] = arr[R], arr[more],
            return [less + 1, more]


list_ = [1, 3, 3, 5, 4, 2, 1, 5, 8, 7, 9]
s = QuickSort().run(list_)
print(s)
