#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 15:57:59 2018

@author: zhaoziliang
"""

age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)

'''
在命令行界面下运行你的程序，然后在命令行输入 pydoc raw_input 看它说了些什么。如果你用的是 Window，那就试一下 python -m pydoc raw_input 。
输入 q 退出 pydoc。
上网找一下 pydoc 命令是用来做什么的。
使用 pydoc 再看一下 open, file, os, 和 sys 的含义。看不懂没关系，只要通读一下，记下你觉得有意思的点就行了。
'''