from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans = []
        adj_list = [[] for _ in range(numCourses)]
        
        for dest, src in prerequisites:
            adj_list[src].append(dest)
        
        print(adj_list)
        state = [0] * numCourses
        
        def hascycle(v):
            if state[v] == 1: # Checked
                return False
            
            if state[v] == -1: # Still in progress
                return True
            
            state[v] = -1
            
            for i in adj_list[v]:
                if hascycle(i):
                    return True
                
            state[v] = 1
            ans.append(v)
            return False
        
        for i in range(numCourses):
            if hascycle(i):
                return []
        
        return ans
            
        
if __name__ == '__main__':
    
    numCourses = 5
    prerequisites = [[1,0],[2,0],[4,0],[2,1],[2,3]]
    
    ans = Solution().findOrder(numCourses, prerequisites)
    print(ans)