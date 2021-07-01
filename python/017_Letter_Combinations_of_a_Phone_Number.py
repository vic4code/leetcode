#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 17:24:54 2021

@author: victor
"""

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        dict_map = {'2':['a','b','c'],
                    '3':['d','e','f'],
                    '4':['g','h','i'],
                    '5':['j','k','l'],
                    '6':['m','n','o'],
                    '7':['p','q','r','s'],
                    '8':['t','u','v'],
                    '9':['w','x','y','z']}        
        
        res = []
        alphabets = [[] for x in range(4)]
        
        for i in range(len(digits)):
            alphabets[i] = dict_map[digits[i]]
            
        
        if alphabets[0]:
            for a1 in alphabets[0]:
                
                if alphabets[1]:
                    for a2 in alphabets[1]:
                        
                        if alphabets[2]:
                            for a3 in alphabets[2]:
                                
                                if alphabets[3]:
                                    for a4 in alphabets[3]:
                                        res.append(a1 + a2 + a3 + a4)
                                
                                else:
                                    res.append(a1 + a2 + a3)
                                       
                        else:
                            res.append(a1 + a2)
                            
                else:
                    res.append(a1)
            
        else:
            return []

        return res
  
if __name__ == '__main__':
    
    digits = "2345"
    ans = Solution().letterCombinations(digits)
    
    print(ans)