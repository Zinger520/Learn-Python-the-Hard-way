#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 11:29:07 2018

@author: zhaoziliang
"""

i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i


print "The numbers: "

for num in numbers:
    print num

animals = ['bear', 'tiger', 'penguin', 'zebra']
print animals[0]