#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# FileName ：z_n_08_堆排序.py
# Author   ：zheng xingtao
# Date     ：2021/3/22 13:38

class HeapSort:
    def sort(self, arr: list):
        """启动堆排序"""
        if arr is None or len(arr) < 2:
            return

        # 0~i 上形成大根堆
        for i in range(len(arr)):
            self.heap_insert(arr, i)

            # 最后一个数和第一个数交换
        heap_size = len(arr) - 1
        arr[0], arr[heap_size] = arr[heap_size], arr[0]

        # 直到大根堆的长度为0，所有的数就都有序了
        while heap_size > 0:
            self.heapify(arr, 0, heap_size)
            arr[0], arr[heap_size - 1] = arr[heap_size - 1], arr[0]

            # 进过上述操作之后，把heap_size - 1
            heap_size -= 1

        return arr

    def heap_insert(self, arr: list, index: int):
        """在大根堆的基础上添加一个元素，heapInsert使其依然是大根堆"""

        # 这个while是为了能 找到所有的父节点
        while arr[index] > arr[int((index - 1) / 2)]:
            # 只要我比我当前父节点的值大，我就和它完成交换
            arr[index], arr[int((index - 1) / 2)] = arr[int((index - 1) / 2)], arr[index]

            # 同时index向上走
            # 当i走到0的时候，会出现arr[0] = arr[(0-1)/2], while也会停止
            index = int((index - 1) / 2)

    def heapify(self, arr: list, index: int, heap_size: int):
        """heap_size: 已经形成的堆的大小"""
        # 当前元素的左节点
        left = index * 2 + 1

        # 这个while是为了能 找到所有的子节点
        while left < heap_size:

            # 找到左右节点中的 较大值(largest)
            if left + 1 < heap_size and arr[left + 1] > arr[left]:
                # 右节点也不越界，且 右节点>左节点
                largest = left + 1
            else:
                largest = left

            # 我和左右两个节点比较，如果还是我最大，就不用交换
            largest = largest if arr[largest] > arr[index] else index
            if largest == index:
                break
            arr[largest], arr[index] = arr[index], arr[largest]

            index = largest
            left = index * 2 + 1


list_ = [2, 4, 3, 6, 5, 8, 7, 10, 9]
arr = HeapSort().sort(list_)
print(arr)
