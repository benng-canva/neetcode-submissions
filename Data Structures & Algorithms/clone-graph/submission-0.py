"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clones = {}
        def dfsClone(original):
            if original == None:
                return None

            if original in clones:
                return clones[original]

            cur = Node(original.val)
            clones[original] = cur

            for nb in original.neighbors:
                cloneNb = dfsClone(nb)
                if cloneNb != None:
                    cur.neighbors.append(cloneNb)

            return cur

        if not node:
            return

        return dfsClone(node)

        