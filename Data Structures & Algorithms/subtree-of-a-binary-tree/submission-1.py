# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None and subRoot == None:
            return True
        
        if root == None or subRoot == None:
            return False

        if self.isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, rootA, rootB):
        if rootA == None and rootB == None:
            return True

        if rootA == None or rootB == None:
            return False

        if rootA.val != rootB.val:
            return False

        return self.isSameTree(rootA.left, rootB.left) and self.isSameTree(rootA.right, rootB.right)

        