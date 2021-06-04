#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 02:51:18 2021

@author: victor
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # rev_digits = digits[::-1]
    
        # i = 0
        # while i < len(digits):
        #     carry = 0
        #     last_val = rev_digits[i] + 1
        #     rev_digits[i] = last_val % 10
        #     carry = last_val // 10 

        #     while carry == 1:

        #         i += 1
        #         if i == len(digits):
        #             rev_digits = rev_digits + [1]
        #             break

        #         else:
        #             last_val = rev_digits[i] + 1
        #             rev_digits[i] = last_val % 10
        #             carry = last_val // 10 

        #     else:
        #         break

        # return rev_digits[::-1]
        
        length = len(digits)
        
        for i in reversed(range(length)):
            if digits[i] != 9:
                digits[i] = digits[i] + 1
                return digits
                break
            
            else:
                digits[i] = 0
 
        digits = [1] + digits
        
        return digits
                
if __name__ =='__main__':
    
    digits = [2,3,9]

    ans = Solution().plusOne(digits)
    print(ans)
    
    