#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# FileName ：z_n_09_桶排序.py
# Author   ：zheng xingtao
# Date     ：2021/3/22 13:39

"""
桶排序：
    计数排序
    基数排序
"""


class MaxGap:
    def get_max(self, arr: list):
        """启动桶排序"""
        if arr is None or len(arr) < 2:
            return 0

        # 拿到数组中的最大值最小值
        min_, max_, len_ = min(arr), max(arr), len(arr)
        for num in arr:
            min_, max_ = min(min_, num), max(max_, num)
        if min_ == max_:  # 说明只有一个相同的数
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

        result = 0
        lastMax = max_s[0]

        # 找到每一个非空桶，以及当前非空桶左侧最近的非空桶，用当前痛的最小 - 上一个桶的最大
        for i in range(1, len_):
            if has_num[i]:
                result = max(result, min_s[i] - lastMax)
                lastMax = max_s[i]
        return result

    def bucket(self, num: int, len_: int, min_: int, max_: int):
        """
        怎么确定一个数来自于哪个桶:
            # 最后的的答案一定大于等于 bucket_size
            # 因为只有这n个数均匀排列才等于bucket_size
            # 否则一定大于bucket_size
        """
        return int((num - min_) * (len_ - 1) / (max_ - min_))


list_ = [2, 10, 9, 30]
number = MaxGap().get_max(list_)
print(number)


def count_sort(arr):
    output = [0 for i in range(256)]
    count = [0 for i in range(256)]
    ans = ["0" for _ in arr]

    for i in arr:
        count[ord(i)] += 1

    for i in range(256):
        count[i] += count[i - 1]

    for i in range(len(arr)):
        output[count[ord(arr[i])] - 1] = arr[i]
        count[ord(arr[i])] -= 1

    for i in range(len(arr)):
        ans[i] = output[i]
    return ans


arr = "wwwrunoobcom"
ans = count_sort(arr)
print("字符数组排序 %s" % ("".join(ans)))
