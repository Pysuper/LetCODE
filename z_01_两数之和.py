# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author   : Zheng Xingtao
# File     : z_01_两数之和.py
# Datetime : 2020/10/16 下午4:24


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # 暴力枚举
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if nums[i] + nums[j] == target and i != j:
        #             return [i, j]

        # 哈希表
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []


nums = [3, 2, 4]
target = 6

li_ = Solution().twoSum(nums, target)
print(li_)
