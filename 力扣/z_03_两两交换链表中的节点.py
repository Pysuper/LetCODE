# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/8 下午1:25
# @Author  : Zheng Xingtao
# @File    : z_03_两两交换链表中的节点.py

# Definition for singly-linked list.
class ListNode(object):
    """定义单链列表"""
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        while pre.next and pre.next.next:
            n1 = pre.next  # 所以pre是先导指针，其后3个指针都是由pre来决定的
            n2 = n1.next
            tmp = n2.next

            # 交换过程
            pre.next = n2
            n2.next = n1
            n1.next = tmp

            pre = n1

    def swapPairs_2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        while pre.next and pre.next.next:
            # 初始化要交换的2个指针
            first = pre.next
            second = first.next

            # 进入交换过程
            first.next = second.next
            second.next = first
            pre.next = second

            pre = first  # 更新pre，进入下一轮

        return dummy.next


result = Solution().swapPairs([1, 2, 3, 4])
print(result)
