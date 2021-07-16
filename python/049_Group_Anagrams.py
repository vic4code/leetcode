#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 17:43:37 2021

@author: victor
"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        res = []
        
        while strs:
            target = strs[0]
            
            target_key = []
            target_val = []
            for s in target:
                if s in target_key:
                    target_val[target_key.index(s)] += 1
                
                else:
                    target_key.append(s)
                    target_val.append(1)
            
            target_dict = dict(zip(target_key,target_val))
            
            sub_res = []
            remove_item = []
            
            for str in strs:
                count = 0
                current_key = []
                current_val = []
                
                # if str:
                for s in str:
                    if s in current_key:
                        current_val[current_key.index(s)] += 1
                    
                    else:
                        current_key.append(s)
                        current_val.append(1)
                
                current_dict = dict(zip(current_key,current_val))
                
                if current_dict == target_dict:
                    sub_res.append(str)
                    remove_item.append(str)
                
                # else:
                #     sub_res.append(str)
                #     remove_item.append(str)
                
            for rm in remove_item:
                strs.remove(rm)
            
            res.append(sub_res)
            
        return res
    
    def groupAnagrams(self, strs):
        d = {}
        for w in sorted(strs):
            key = tuple(sorted(w))
            print(key)
            # get value of key, if does not exist, return []
            d[key] = d.get(key, []) + [w]
        
        # print(d)
        return d
                    
if __name__ == '__main__':
    
    strs = ["eat","tea","tan","ate","nat","bat"]
    # strs = ["","b"]
    # strs = ["ddddddddddg","dgggggggggg"]
    # strs = ["",""]
    # strs = ["stop","pots","reed","","tops","deer","opts",""]
    

    ans = Solution().groupAnagrams(strs)
    print(ans)

            
    
    
    
    
    