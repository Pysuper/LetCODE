# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/8 上午10:46
# @Author  : Zheng Xingtao
# @File    : z_02_反转字符串.py

class Solution_str(object):
    def reverseString(self, strings):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        if len(strings) == 2:
            return strings[1] + strings[0]
        else:
            return strings[-1] + self.reverseString(strings[:-1])

    def my_code(self, strings):
        while len(strings) > 1:
            return strings[-1] + self.my_code(strings[:-1])
        return strings[-1]


class Solution_list(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        beg = 0
        end = len(s) - 1
        while beg < end:
            s[beg], s[end] = s[end], s[beg]
            beg += 1
            end -= 1
        return s


string = '1234567890'
string_list = ["h", "e", "l", "l", "o"]

print(Solution_str().my_code(string))
print(Solution_list().reverseString(string_list))
