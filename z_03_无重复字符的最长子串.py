# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author   : Zheng Xingtao
# File     : z_03_无重复字符的最长子串.py
# Datetime : 2020/10/16 下午4:41


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # if not s: return 0
        # left = 0
        # lookup = set()
        # n = len(s)
        # max_len = 0
        # cur_len = 0
        # for i in range(n):
        #     cur_len += 1
        #     while s[i] in lookup:
        #         lookup.remove(s[left])
        #         left += 1
        #         cur_len -= 1
        #     if cur_len > max_len: max_len = cur_len
        #     lookup.add(s[i])
        # return max_len

        # 哈希集合，记录每个字符是否出现过
        occ = set()
        n = len(s)

        # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                # 左指针向右移动一格，移除一个字符
                occ.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in occ:
                # 不断地移动右指针
                occ.add(s[rk + 1])
                rk += 1

            # 第 i 到 rk 个字符是一个极长的无重复字符子串
            ans = max(ans, rk - i + 1)
        return ans


print(Solution().lengthOfLongestSubstring("pwwwpasd"))
