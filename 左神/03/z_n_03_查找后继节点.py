# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/15 22:27
# @Author  : Zheng Xingtao
# @File    : z_n_03_查找后继节点.py

"""
在二叉树中找到一个节点的后继节点
在二叉树的中序遍历的序列中，node的下一个节点叫作node的后继节点。

【题目】 现在有一种新的二叉树节点类型如下：
public class Node {
    public int value;
    public Node left;
    public Node right;
    public Node parent;
    public Node(int data) {this.value = data;}
}
该结构比普通二叉树节点结构多了一个指向父节点的parent指针。
假设有一棵Node类型的节点组成的二叉树，树中每个节点的parent指针都正确地指向自己的父节点，头节点的parent指向null。
只给一个在二叉树中的某个节点node，请实现返回node的后继节点的函数。
"""