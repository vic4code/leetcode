#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 01:41:03 2021

@author: victor
"""

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        summation = 0

        switcher = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        n = 1
        
        while n < len(s):

            if switcher[s[n - 1]] < switcher[s[n]]:
                substract_num = switcher[s[n]] - switcher[s[n - 1]]
                summation = summation + substract_num
                n = n + 2

            else:
                summation = summation + switcher[s[n - 1]]
                n = n + 1
        
        if n == len(s):
            summation = summation + switcher[s[-1]]
        
        return summation