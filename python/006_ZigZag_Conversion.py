#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 23:49:59 2021

@author: victor
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        length = len(s)
        CenterNum = (numRows - 1)
        PeriodicNum = (numRows - 1) * 2
        order = []
        
        if numRows <= 1:
            return s
        
        else:
        
            for i in range(CenterNum + 1):
                
                k = 0
                o = []
                
                while PeriodicNum * k < length:
                    
                    if (i == 0 or CenterNum - i == 0) and CenterNum - i + PeriodicNum * k < length:
                        o = o + [CenterNum - i + PeriodicNum * k]
                        
                    else:
                        
                        if CenterNum - i + PeriodicNum * k < length:
                            o = o + [CenterNum - i + PeriodicNum * k]
                        
                        if CenterNum + i + PeriodicNum * k < length:
                            o = o + [CenterNum + i + PeriodicNum * k]
                            
                    k += 1
                    
                order.append(o)
            
            ## Reverse order
            ReverseOrder = []
            
            for x in order[::-1]:
                ReverseOrder += x
            
            String = ''
            
            for i in ReverseOrder:
                String += s[i]
                
            return String
    
if __name__ == '__main__':
    
    
    s = 'PAYPALISHIRING'
    numRows = 3
    
    ans = Solution().convert(s,numRows)
    print(ans)