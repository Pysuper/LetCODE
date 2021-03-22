#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# FileName ：z_n_09_桶排序.py
# Author   ：zheng xingtao
# Date     ：2021/3/22 13:39


class MaxGap:
    def get_max(self, arr: list):
        """启动桶排序"""
        if arr is None or len(arr) < 2:
            return

        min_ = min(arr)
        max_ = max(arr)
        len_ = len(arr)

        """
        # 遍历数组，找到数组的min和max
        for i in range(len(arr)):
            # 遍历数组，用每个数和当前的min_比较，并更新min_、max
            min_ = min(min_, arr[i])
            max_ = max(min_, arr[i])
        """

        if min_ == max_:
            # 说明只有一个相同的数
            return 0

        min_s = [0] * (len(arr) + 1)  # 每个桶的最小值
        max_s = [0] * (len(arr) + 1)  # 每个桶的最大值
        has_num = [0] * (len(arr) + 1)  # 当前桶中是否有数值

        # 当前数去第几号桶，修改这个桶的最小值，最大值，是否有值
        for i in range(len(arr)):
            bid = self.bucket(arr[i], len_, min_, max_)  # TODO: 几号桶
            min_s[bid] = min(min_s[bid], arr[i]) if has_num[bid] else arr[i]
            max_s[bid] = max(max_s[bid], arr[i]) if has_num[bid] else arr[i]
            has_num[bid] = True

        print(min_s, max_s)
        result = 0
        lastMax = max_s[0]

        # 找到每一个非空桶，以及当前非空桶左侧最近的非空桶，用当前痛的最小 - 上一个桶的最大
        for i in range(1, len_):
            if has_num[i]:
                result = max(result, min_s[i] - lastMax)
                lastMax = max_s[i]

        return result

    def bucket(self, num: int, len_: int, min_: int, max_: int):
        """怎么确定一个数来自于哪个桶"""
        print(int((num - min_) * len_ / (max_ - min_)))
        return int((num - min_) * len_ / (max_ - min_))


list_ = [2, 10, 9, 20]
number = MaxGap().get_max(list_)
print(number)
