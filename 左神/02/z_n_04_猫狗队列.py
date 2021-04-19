# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/22 22:57
# @Author  : Zheng Xingtao
# @File    : z_n_04_猫狗队列.py

"""
猫狗队列 【题目】 宠物、狗和猫的类如下：

public class Pet { private String type;
    public Pet(String type) { this.type = type; }
    public String getPetType() { return this.type; }
}

public class Dog extends Pet { public Dog() { super("dog"); } }
public class Cat extends Pet { public Cat() { super("cat"); } }

实现一种狗猫队列的结构，要求如下：
1、用户可以调用add方法将cat类或dog类的实例放入队列中
2、用户可以调用pollAll方法，将队列中所有的实例按照 进队列的先后顺序 依次弹出
3、用户可以调用pollDog方法，将队列中dog类的实例按照 进队列的先后顺序 依次弹出
4、用户可以调用pollCat方法，将队列中cat类的实例按照 进队列的先后顺序 依次弹出
5、用户可以调用isEmpty方法，检查队列中是否还有dog或cat的实例
6、用户可以调用isDogEmpty方法，检查队列中是否有dog类的实例
7、用户可以调用isCatEmpty方法，检查队列中是否有cat类的实例。
"""

