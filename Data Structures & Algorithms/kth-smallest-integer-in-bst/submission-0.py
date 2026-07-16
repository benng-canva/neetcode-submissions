# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        tree = self.dfs(root, [])

        return tree[k - 1]
        
    def dfs(self, root, elements):
        if not root:
            return elements

        self.dfs(root.left, elements)
        elements.append(root.val)
        self.dfs(root.right, elements)

        return elements

        