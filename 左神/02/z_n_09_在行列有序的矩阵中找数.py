# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/15 22:14
# @Author  : Zheng Xingtao
# @File    : z_n_09_在行列有序的矩阵中找数.py

"""
在行列都排好序的矩阵中找数
【题目】 给定一个有 N*M 的整型矩阵matrix和一个整数K，matrix的每一行和每一列都是排好序的。实现一个函数，判断K是否在matrix中。
例如： 0 1 2 5 2 3 4 7 4 4 4 8 5 7 7 9，如果K为7，返回true；如果K为6，返回false。

【要求】 时间复杂度为O(N+M)，额外空间复杂度为O(1)。
"""