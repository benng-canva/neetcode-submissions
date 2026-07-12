# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []

        queue = deque([root])
        res = []

        while queue:
            currentLevel = len(queue)
            level = []
            for i in range(currentLevel):
                node = queue.popleft()

                level.append(node.val)

                if node.left != None:
                    queue.append(node.left)
                
                if node.right != None:
                    queue.append(node.right)
            res.append(level)
        
        return res


        