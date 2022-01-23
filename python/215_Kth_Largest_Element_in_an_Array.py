from typing import List
import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        
        return nums[-k]
    
    def findKthLargest(self, nums, k):
        if not nums: return
        pivot = random.choice(nums)
        left =  [x for x in nums if x > pivot]
        mid  =  [x for x in nums if x == pivot]
        right = [x for x in nums if x < pivot]
        
        L, M = len(left), len(mid)
        
        if k <= L:
            return self.findKthLargest(left, k)
        elif k > L + M:
            return self.findKthLargest(right, k - L - M)
        else:
            return mid[0]
        
if __name__ == '__main__':
    
    nums = [3,4,6,8,1]
    k = 2
    ans = Solution().findKthLargest(nums, k)
    