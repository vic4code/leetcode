#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 18:02:15 2021

@author: victor
"""
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        
        ret, power = 0, 31
        while n:
            
            # n & 1 operation to get the right-most bit:
            # 00011001    
            # 00000001   (00000001 is 1 in binary)
            #        &
            # --------
            # 00000001
            
            ret += (n & 1) << power            
            # Remove the right-most bit by dividing 2
            n = n >> 1
            power -= 1
            
        return ret
            
            
if __name__ == '__main__':
    
    # n = '00000010100101000001111010011100'
    # ans = Solution().reverseBits(n)
    
    # print(ans)
