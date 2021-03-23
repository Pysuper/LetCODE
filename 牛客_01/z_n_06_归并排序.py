#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# FileName ：z_n_06_归并排序.py
# Author   ：zheng xingtao
# Date     ：2021/3/17 10:46

class MergeSort(object):
    def __init__(self, arr: list):
        self.arr = arr

    def sort(self):
        if self.arr and len(self.arr) > 2:
            # sortProcess: 递归过程，排序的实质
            self.sort_process(self.arr, 0, len(self.arr) - 1)
        return self.arr

    def sort_process(self, arr: list, L: int, R: int):
        """
        归并排序, 从L~R上排好序
        :param arr: 无序数列
        :return: 有序数列
        """
        if L != R:  # L=R：数列中只有一个数
            mid = int((L + R) / 2)
            self.sort_process(arr, L, mid)
            self.sort_process(arr, mid + 1, R)
            self.merge(arr, L, mid, R)

    def merge(self, arr: list, L: int, mid: int, R: int):
        """将左右 有序的 合并 到一起"""
        i = 0
        p1 = L  # 整个左侧部分的最小值
        p2 = mid + 1  # 整个右侧的最小值
        help = [0] * (R - L + 1)

        while p1 <= mid and p2 <= R:  # 左右部分，任一部分超出边界，这部分已经填完了
            if arr[p1] < arr[p2]:
                help[i] = arr[p1]
                p1 += 1
            else:
                help[i] = arr[p2]
                p2 += 1
            i += 1

        # 有且只有一个越界了， 两个while只会有一个发生
        while p1 <= mid:
            help[i] = arr[p1]
            p1 += 1
            i += 1

        while p2 <= R:
            help[i] = arr[p2]
            p2 += 1
            i += 1

        for index in range(len(help)):
            self.arr[L + index] = help[index]


arr_ = MergeSort([2, 4, 3, 5, 10, 6, 9, 8, 7]).sort()
print(arr_)


class SmallSum(object):
    """
    小和问题：使用归并排序，每个小组在合并的同时，产生小和
    """

    # def __init__(self, arr: list):
    #     self.arr = arr

    def small_sum(self, arr):
        if arr is None or len(arr) < 2:
            return 0
        return self.merge_sort(arr, 0, len(arr) - 1)

    def merge_sort(self, arr: list, L: int, R: int):
        if L == R:
            return 0
        mid = int((L + R) / 2)

        # 左侧部分产生的小和 + 右侧部分产生的小和 + merge过程中产生的小和
        return self.merge_sort(arr, L, mid) + self.merge_sort(arr, mid + 1, R) + self.merge(arr, L, mid, R)

    def merge(self, arr: list, L: int, mid: int, R: int):
        help = [0] * (R - L + 1)
        p1 = L
        p2 = mid + 1
        i = result = 0
        while p1 <= mid and p2 <= R:
            if arr[p1] < arr[p2]:
                result += (R - p2 + 1) * arr[p1]  # 右侧比x大的数有多少个 * 当前x的数值
                help[i] = arr[p1]
                p1 += 1
            else:
                result += 0
                help[i] = arr[p2]
                p2 += 1
            i += 1

        while p1 <= mid:
            help[i] = arr[p1]
            i += 1
            p1 += 1

        while p2 <= R:
            help[i] = arr[p2]
            i += 1
            p2 += 1

        for index in range(len(help)):
            arr[L + index] = help[index]
        return result


result = SmallSum().small_sum([1, 3, 4, 2, 5])
print(result)
