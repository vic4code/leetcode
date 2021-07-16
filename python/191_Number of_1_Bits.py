#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 20:13:47 2021

@author: victor
"""
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        res, bits = 0, 32
        
        for i in range(bits):
            if n & 1 == 1:
                res += 1
                
            n = n >> 1
            
        return res