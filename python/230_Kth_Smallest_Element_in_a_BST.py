# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
#     def kthSmallest(self, root, k):
#         """
#         :type root: TreeNode
#         :type k: int
#         :rtype: int
#         """
        
#         List = []
#         self.dfs(root,List)
        
#         List.sort()
#         res = List[k - 1]
        
#         return res
        
        
#     def dfs(self,root,List):
        
#         if root:
#             List.append(root.val)
#             self.dfs(root.left,List)
#             self.dfs(root.right,List)

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def inorder(r):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []
    
        return inorder(root)[k - 1]
    

        

            