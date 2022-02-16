from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        arr = sorted(nums)
        for i in range(1, len(nums), 2): nums[i] = arr.pop() 
        for i in range(0, len(nums), 2): nums[i] = arr.pop() 

if __name__ == '__main__':

    nums = [1,5,1,1,6,4] 
    ans = Solution().wiggleSort(nums)
    print(nums)