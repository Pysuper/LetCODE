# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author   : Zheng Xingtao
# File     : z_05_寻找两个正序数组的中位数.py
# Datetime : 2020/10/16 下午4:58


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        list_ = nums1 + nums2
        if len(list_) % 2 == 0:  # 偶数序列
            key = int(len(list_) / 2 - 1)
            num = list_[key] + list_[key + 1]
            return '%.5f' % float((num / 2))

        else:  # 奇数序列
            num = list_[len(list_) - 1] / 2 + 1
            return '%.5f' % float((list_[int(num)]))


nums1 = [1, 3]
nums2 = [2]
print(Solution().findMedianSortedArrays(nums1, nums2))
