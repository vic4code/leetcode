#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 12:44:35 2021

@author: victor
"""

class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        
        res = address.replace('.','[.]')
        return res
        
if __name__ == '__main__':
    
    address = "1.1.1.1"
    address = "255.100.50.0"
    
    ans = Solution().defangIPaddr(address)
    print(ans)