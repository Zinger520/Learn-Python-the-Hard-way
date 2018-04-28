#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 14:56:19 2018

@author: zhaoziliang
"""

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

print "\a"
print "I am 6'2\" tall."  # 将字符串中的双引号转义
print 'I am 6\'2" tall.'  # 将字符串种的单引号转义
print "%r" %"\\" #程序员调试看到的原始字符串
print "%s" %"\\" #用户看到的字符串
'''
while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,
'''