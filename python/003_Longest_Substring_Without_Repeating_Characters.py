#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 00:52:46 2021

@author: victor
"""

class Solution:
    
        # def lengthOfLongestSubstring(self, s: str) -> int:
            
        #     length = len(s)
            
        #     max_front_index = 0
        #     max_tail_index = 0
        #     max_substring = ''
            
        #     front_index = 0
        #     tail_index = 0
        #     substring = ''
            
        #     i = 0

        #     while i < length:
        #         if s[i] not in substring:
        #             tail_index += 1

        #             if (tail_index - front_index) > (max_tail_index - max_front_index):
        #                 max_tail_index = tail_index
        #                 max_front_index = front_index
                
        #         elif s[i - 1] != s[i]:
        #             i -= 1
        #             front_index = max_front_index + 1
        #             # Won't cause index out of range, because if else happen, it means there is st
        #             # tail_index = i + 1
                    
                    
        #         else:                    
        #             front_index = i 
        #             # Won't cause index out of range, because if else happen, it means there is st
        #             tail_index = i + 1

        #         i += 1

        #         substring = s[front_index:tail_index]
                
        #         print(substring)
                
        #     max_substring = s[max_front_index:max_tail_index]
        #     print(max_substring)
        #     return len(max_substring)
        
        def lengthOfLongestSubstring(self, s):

            str_list = []
            max_length = 0
        
            for x in s:
                if x in str_list:
                    str_list = str_list[str_list.index(x)+1:]
                    
                str_list.append(x)    
                print(str_list)
                max_length = max(max_length, len(str_list))

            return max_length
            
if __name__ == '__main__':
    
    # s = "abcabcbb"
    # s = "pwwkew"
    # s = " "
    # s = "au"
    # s = "cdd"
    # s = "dvdf"
    s = "anviaj"
    
    ans = Solution().lengthOfLongestSubstring(s)
    print(ans)
    