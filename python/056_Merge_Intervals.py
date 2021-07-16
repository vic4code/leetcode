#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 13:31:11 2021

@author: victor
"""
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
        
        
        

if __name__ == '__main__':
    
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    # intervals = [[1,4],[4,5]]
    # intervals = [[4,5],[1,4]]
    # intervals = [[1,3]]
    # intervals = [[1,4],[5,6],[7,8],[8,9]]
    # intervals = [[1,4],[4,6],[6,8],[8,9]]
    # intervals = [[1,4],[0,4]]
    # intervals = [[1,4],[0,0]]
    # intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]
    # intervals = [[0,2],[1,3],[2,4],[3,6],[5,7]]
    
    ans = Solution().merge(intervals)
    print(ans)