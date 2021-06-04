#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 23:20:27 2021

@author: victor
"""

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        str2num = { '0':0,
                    '1':1,
                    '2':2,
                    '3':3,
                    '4':4,
                    '5':5,
                    '6':6,
                    '7':7,
                    '8':8,
                    '9':9,
                  }

        ## Convert Strings to Numbers
        val_a = 0
        val_b = 0

        for i in range(len(num1)):
            val_a += 10 ** i * str2num[num1[::-1][i]]

        for i in range(len(num2)):
            val_b += 10 ** i * str2num[num2[::-1][i]]

        ## Multiply Numbers
        val = val_a * val_b

        ## Convert Numbers to Strings
        return str(val)
        
if __name__ =='__main__':
    
    num1, num2 = '2', '3'
    ans = Solution().multiply(num1, num2)
    print(ans)    