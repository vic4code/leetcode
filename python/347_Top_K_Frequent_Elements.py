from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        table = {}
        
        for num in nums:
            if num not in table:
                table[num] = 1
            
            else:
                table[num] += 1
        
        
        counts = [item[1] for item in table.items()]
        counts.sort()
        
        top_counts = counts[::-1][:k]
         
        
        for k, v in table.items():
            
            if v in top_counts:    
                top_counts.remove(v)
                res.append(k)
            
            if not top_counts:
                return res
            

if __name__ == '__main__':

    nums = [1,2,3,3,4,5,5,6]
    k = 2

    ans = Solution().topKFrequent(nums, k)
    print(ans)