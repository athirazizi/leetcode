# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def addOneRow(self, root, val, depth):
        """
        :type root: TreeNode
        :type val: int
        :type depth: int
        :rtype: TreeNode
        """
        if depth == 1:
            newRoot = TreeNode(val)
            newRoot.left = root
            return newRoot
        
        queue = [(root, 1)]                 
        
        while queue:
            node, level = queue.pop(0)
            
            if level == depth - 1:
                leftChild = node.left 
                rightChild = node.right 
                
                node.left = TreeNode(val)
                node.right = TreeNode(val)
                
                node.left.left = leftChild 
                node.right.right = rightChild 
            
            else:
                if node.left:
                    queue.append((node.left, level + 1))
                    
                if node.right:
                    queue.append((node.right, level + 1))
                    
        return root