#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 17:16:42 2021

@author: victor
"""

class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        """
        :type firstWord: str
        :type secondWord: str
        :type targetWord: str
        :rtype: bool
        """

        firstVal = self.alphabet_to_integer(firstWord)
        secondVal = self.alphabet_to_integer(secondWord)
        targetVal = self.alphabet_to_integer(targetWord)
            
        if firstVal + secondVal == targetVal:
            return True
        
        else:
            return False
        
    def alphabet_to_integer(self,alphabet):
        
        dictionary = {'a':'0',
                      'b':'1',
                      'c':'2',
                      'd':'3',
                      'e':'4',
                      'f':'5',
                      'g':'6',
                      'h':'7',
                      'i':'8',
                      'j':'9',
                      }
        
        alphabet_to_string = ''
        
        for s in alphabet:
            alphabet_to_string = alphabet_to_string + dictionary[s]
        
        return int(alphabet_to_string)
            
        
if __name__ == '__main__':
    
    firstWord = "acb"
    secondWord = "cba"
    targetWord = "cdb"
    
    ans = Solution().isSumEqual(firstWord, secondWord, targetWord)
    print(ans)
    
    