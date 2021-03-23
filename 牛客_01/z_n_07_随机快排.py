#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# FileName ：z_n_07_随机快排.py
# Author   ：zheng xingtao
# Date     ：2021/3/19 11:12


class HeLanGuoQi(object):
    """荷兰国旗问题"""

    def partition(self, arr: list, num: int):
        cur = 0
        less = - 1
        more = len(arr) - 1 + 1
        while cur < more:
            if arr[cur] < num:
                less += 1
                arr[less], arr[cur] = arr[cur], arr[less]
                cur += 1
            elif arr[cur] > num:
                more -= 1
                arr[more], arr[cur] = arr[cur], arr[more]
                # cur -= 1 # TODO: 注意这里cur不动
            else:
                cur += 1

        # 返回等与区域的左边界和右边界
        return [less + 1, more - 1]


# list_ = [1, 2, 3, 4, 3]
# result = HeLanGuoQi().partition(list_, 3)
# print(result)


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
        if L < R:
            p = self.partition(arr, L, R)
            self.quick_sort(arr, L, p[0] - 1)
            self.quick_sort(arr, p[0] + 1, R)

    def partition(self, arr: list, L: int, R: int):
        less = L - 1
        more = R
        while L < more:
            if arr[L] < arr[R]:
                arr[less], arr[L] = arr[L], arr[less]
                less += 1
                L += 1
            elif arr[L] > arr[R]:
                arr[more], arr[L] = arr[L], arr[more]
                more -= 1
            else:
                L += 1
        arr[more], arr[R] = arr[R], arr[more]
        return [less + 1, more]


# list_ = [1, 3, 3, 5, 4, 2, 1, 5, 8, 7, 9]
# result = QuickSort().run(list_)
# print(result)


class QuickSortPython:

    def partition(self, arr, low, high):
        i = low - 1  # 最小元素索引
        pivot = arr[high]
        # pivot = random.choice(arr)  # 随机快排

        for j in range(low, high):
            if arr[j] <= pivot:  # 当前元素小于或等于 pivot
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def sort(self, arr, low, high):
        """
        :param arr: 排序数组
        :param low: 起始索引
        :param high: 结束索引
        :return:
        """
        if low < high:
            pi = self.partition(arr, low, high)
            self.sort(arr, low, pi - 1)
            self.sort(arr, pi + 1, high)
        return arr


list_ = [1, 3, 3, 5, 4, 2, 1, 5, 8, 7, 9]
result = QuickSortPython().sort(list_, 0, len(list_) - 1)
print(result)
