# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        return self.dfs(root, p, q)
    
    def dfs(self, node, p, q):
        
        if node == p or node == q:
            return node
        
        left = right = False
        if node.left:
            left = self.dfs(node.left, p, q)
            
        if node.right:
            right = self.dfs(node.right, p ,q)
        
     
        if left and right:
            return node
            
        else:
            return left or right

